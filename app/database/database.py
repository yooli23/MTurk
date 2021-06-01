import os
import threading

import sqlite3

from utils.settings import Settings

    
class Inspector:

    def __init__(self, task_id=None):
        self.task_id = task_id
        self.database = Database()

    @property
    def task_ids(self):        
        try:
            result = self.database.cursor.execute(f"SELECT task_id FROM task_info")
            result = [x[0] for x in list(result)]
        except:
            result = []        
        return result

    @property
    def hit_info(self):        
        try:
            result = self.database.cursor.execute(f"SELECT worker_id, assignment_id, hit_id FROM HIT_INFO WHERE task_id = '{self.task_id}'")            
            result = [{'hit_id':x[2], 'assignment_id': x[1], 'worker_id': x[0]} for x in list(result)][0]
            result['task_group_id'] = self.database._get_task_group_id(result['hit_id'])
        except Exception as error:   
            print(error)         
            result = {}        
        return result    

    @property
    def task_info(self):        
        try:
            result = self.database.cursor.execute(f"SELECT complete, human_speaks_first FROM task_info WHERE task_id = '{self.task_id}'")            
            result = [{'complete':bool(x[0]), 'human_speaks_first': x[1]} for x in list(result)][0]
            if result['human_speaks_first'] == 'False':
                result['human_speaks_first'] = False
            else:
                result['human_speaks_first'] = True
        except Exception as error:            
            result = {}        
        return result        

    @property
    def agents(self):        
        try:
            result = self.database.cursor.execute(f"SELECT agent_name FROM conversation_info WHERE task_id='{self.task_id}'")
            result = [x[0] for x in list(result)]
        except:
            result = []        
        return result    

    @property
    def forms(self):        
        try:
            result = self.database.cursor.execute(f"SELECT form_title FROM form_info WHERE task_id='{self.task_id}'")
            result = [x[0] for x in list(result)]
        except Exception as error:
            print("Error when trying to view form data:", error)
            result = []        
        return result 
        
    def form_data(self, form_title):        
        try:
            result = self.database.cursor.execute(f"SELECT result_json FROM form_info WHERE task_id='{self.task_id}' AND form_title='{form_title}' ")
            result = [x[0] for x in list(result)][0]
        except Exception as error:
            result = []        
        return result    

    def task_id_from_hit_id(self, hit_id):        
        res = self.database.cursor.execute(f"SELECT task_id FROM hit_info WHERE hit_id = '{hit_id}' ")
        try:
            res = list(res)[0][0]
        except:
            res = None              
        return res

    @property
    def linked_hit_ids(self):        
        results = self.database.cursor.execute(f"SELECT hit_id FROM task_group_id_info")
        try:
            results = [x[0] for x in list(results)]
        except:
            results = []        
        return results

class Database:

    @property
    def cursor(self):
        if self.conn_active:
            return self.conn.cursor()
        else:
            raise Exception("Trying to access a non-active cursor!")

    def _is_task_initialized(self, task_id):
        result = list(self.cursor.execute(f"SELECT task_id TEXT, hit_id TEXT, assignment_id TEXT, worker_id TEXT FROM hit_info WHERE task_id = '{task_id}'"))
        if len(result) == 0:
            return False
        return True

    def _create_initial_task_tables(self, task):
        self.cursor.execute(f"INSERT INTO hit_info (task_id, hit_id, assignment_id, worker_id) VALUES ('{task.task_id}', '{task.hit_id}', '{task.assignment_id}', '{task.worker_id}')")
        self.cursor.execute(f"INSERT INTO task_info (task_id, complete, human_speaks_first, current_section) VALUES ('{task.task_id}', 0, '{task.human_speaks_first}', 0)")        
        for name in task.agent_names:
            self.cursor.execute(f"INSERT INTO conversation_info (task_id, agent_name, complete) VALUES ('{task.task_id}', '{name}', 0)")
        self.commit()
    
    def _try_extract_task_section(self, task_id):
        res = self.cursor.execute(f"SELECT current_section FROM task_info WHERE task_id = '{task_id}'")                
        try:            
            return list(res)[0][0]
        except:
            return 0

    def _is_agent_resigned(self, task_id, agent_name):
        results = self.cursor.execute(f"SELECT complete FROM conversation_info WHERE task_id = '{task_id}' AND agent_name = '{agent_name}'")
        try:            
            for i in results:                
                return bool(i[0])
            return False
        except Exception as error:
            raise Exception("Agent does not exist in database.")

    def _get_task_group_id(self, hit_id):        
        res = self.cursor.execute(f"SELECT task_group_id FROM task_group_id_info WHERE hit_id = '{hit_id}' ")
        try:
            res = list(res)[0][0]
        except:
            res = "unknown"        
        return res

    def _parse_context(self, messages, human_speaks_first):
        if len(messages) == 0:
            if human_speaks_first: return [{'human': '', 'bot': ''}]
            return []
        result = []
        data = list(zip(*messages))
        if human_speaks_first == True:
            bot_utt = [""] + list(data[0])
            human_utt = list(data[1]) + [""]
        else:
            bot_utt = data[0]
            human_utt = list(data[1])[1:] + ['']
        for bot, human in zip(bot_utt, human_utt):
            result.append({'bot': bot, 'human': human})
        return result

    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.conn_active = False
        self.conn = {}
        if not os.path.exists(self.settings.database_path):
            self.create()

    def __del__(self):
        self._get_connection().close()

    def _get_connection(self):
        """
        Returns a singular database connection to be shared amongst all calls.
        """
        curr_thread = threading.get_ident()        
        if curr_thread not in self.conn or self.conn[curr_thread] is None:
            try:
                conn = sqlite3.connect(self.settings.database_path)
                conn.row_factory = sqlite3.Row
                self.conn[curr_thread] = conn
            except sqlite3.Error as e:                
                print("Error trying to get connection.")
                print(curr_thread)
                print(self.conn)
                raise e
        return self.conn[curr_thread]

    @property
    def cursor(self):        
        connection = self._get_connection()
        c = connection.cursor()        
        return c

    def commit(self):
        self._get_connection().commit()

    def create(self):        
        self.cursor.execute('''CREATE TABLE hit_info (task_id TEXT, hit_id TEXT, assignment_id TEXT, worker_id TEXT)''')
        self.cursor.execute('''CREATE TABLE task_info (task_id TEXT, complete BOOLEAN, human_speaks_first BOOLEAN, current_section INTEGER)''')
        self.cursor.execute('''CREATE TABLE conversation_info (task_id TEXT, agent_name TEXT, complete BOOLEAN)''')
        self.cursor.execute('''CREATE TABLE messages (task_id TEXT, agent_name TEXT, bot_utt TEXT, human_utt TEXT)''')
        self.cursor.execute('''CREATE TABLE form_info (task_id TEXT, form_title TEXT, result_json TEXT)''')
        self.cursor.execute('''CREATE TABLE task_group_id_info (hit_id TEXT, task_group_id TEXT)''')
        self.commit()
        
    def destory(self):
        try:
            os.remove(self.settings.database_path)
        except Exception as error:
            print(error)

    def reset(self):
        self.destory()
        self.create()

    def init_task(self, task):        
        task_exists = self._is_task_initialized(task.task_id)
        if not task_exists:
              self._create_initial_task_tables(task)

    def save_message(self, task_id, agent_name, bot_utt, human_utt):        
        bot_utt = bot_utt.replace("'", "")        
        human_utt = human_utt.replace("'", "")        
        self.cursor.execute(f"INSERT INTO messages (task_id, agent_name, bot_utt, human_utt) VALUES ('{task_id}', '{agent_name}', '{bot_utt}', '{human_utt}')")
        self.commit()
        
    def load_messages(self, task_id, agent_name):        
        messages = self.cursor.execute(f"SELECT bot_utt, human_utt FROM messages WHERE task_id = '{task_id}' AND AGENT_NAME = '{agent_name}'")
        messages = list(messages)
        try:
            speaks_first = Inspector(task_id=task_id).task_info['human_speaks_first']
        except:
            speaks_first = Settings().human_speaks_first
        context = self._parse_context(messages, speaks_first)            
        return context

    def load_messages_for_html(self, task_id, agent_name):
        result = []        
        messages = self.cursor.execute(f"SELECT bot_utt, human_utt FROM messages WHERE task_id = '{task_id}' AND AGENT_NAME = '{agent_name}'")
        messages = list(messages)
        for bot, human in messages:
            result.append({'bot': bot, 'human': human})        
        return result

    def resign_agent(self, task_id, agent_name):        
        self.cursor.execute(f"UPDATE conversation_info SET complete = 1 WHERE task_id = '{task_id}' AND agent_name = '{agent_name}'")
        self.commit()
        
    def agents_resigned(self, task_id, agent_names):
        result = {}
        for name in agent_names:
            result[name] = self._is_agent_resigned(task_id, name)        
        return result

    def save_form(self, task_id, title, result):
        title = title.replace("-", "_")
        title = title.replace(" ", "_").lower()
        title = ''.join(x for x in title if x.isalpha() or x == '_' or x.isnumeric())        
        try:
            self.cursor.execute(f"INSERT INTO form_info (task_id, form_title, result_json) VALUES ('{task_id}', '{title}', '{result}')")        
            self.commit()
        except Exception as error:
            print('--------------------------------')
            print("Line 253, database.py")
            print(error)
            print(f"INSERT INTO form_info (task_id, form_title, result_json) VALUES ('{task_id}', '{title}', '{result}')")
            print('--------------------------------')
        

    def task_section(self, task_id):        
        res = self._try_extract_task_section(task_id)                        
        return res

    def update_task_section(self, task_id, section):        
        self.cursor.execute(f"UPDATE task_info SET current_section = {section} WHERE task_id = '{task_id}'")
        self.commit()
        
    def mark_task_as_complete(self, task_id):        
        self.cursor.execute(f"UPDATE task_info SET complete = 1 WHERE task_id = '{task_id}'")
        self.commit()
        
    def link_task_group_id(self, hit_id, task_group_id):        
        self.cursor.execute(f"INSERT INTO task_group_id_info (hit_id, task_group_id) VALUES ('{hit_id}', '{task_group_id}')")        
        self.commit()