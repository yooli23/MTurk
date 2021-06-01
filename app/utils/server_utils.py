from flask import render_template

from utils.settings import Settings
from utils.compile import Compile
from utils.build_utils import Task
from database.database import Database


class TaskHelper:

    @classmethod
    def parse_mturk_args(cls, args):
        request_args = dict(args)
        result = {}
        for key, value in request_args.items():
            result[key.replace("amp;", "").replace('Id', '_id')] = value
        return result

    @classmethod
    def get_end_point(cls):
        if Settings().is_sandbox:
            return "https://workersandbox.mturk.com/mturk/externalSubmit"        
        return "https://mturk.com/mturk/externalSubmit"

    @classmethod
    def compile(cls):
        compiler = Compile(Settings().task_build)
        return compiler.task

    @classmethod
    def agent_names(cls, layout):
        names = []
        for element in layout:            
            if element['type'] == 'task':
                for agent in element['data']:                                   
                    names.append(agent['data']['name'])
        return names

    @classmethod
    def convo_map(cls, task_id, agent_names):
        mapping = {}
        for name in agent_names:            
            mapping[name] = Database().load_messages_for_html(task_id, name)
        return mapping


class Task:

    def __init__(self, task_id: str, args):
        #Debug
        # self.assignment_id = None
        # self.hit_id = None
        # self.worker_id = None

        self.task_id = task_id
        self.__dict__.update(**TaskHelper.parse_mturk_args(args))  
        self.__dict__.update(Settings().__dict__)

        #Debug
        # if not self.assignment_id:
        #     self.assignment_id = "abc"
        # if not self.hit_id:
        #     self.hit_id = "abcd"
        # if not self.worker_id:
        #     self.worker_id = "dcba"

        self.end_point = TaskHelper.get_end_point()
        self.layout = TaskHelper.compile()
        self.socket_path = Settings().front_end_socketio_path   
        self.task_complete = False
        self.current_section = Database().task_section(self.task_id)
        self.agent_names = TaskHelper.agent_names(self.layout)        
        self.previous_messages = TaskHelper.convo_map(self.task_id, self.agent_names)     
        self.agents_resigned = Database().agents_resigned(self.task_id, self.agent_names)
        

    @property
    def template(self):
        return render_template(
            'task.html',
            socket_path=self.socket_path,
            task_id=self.task_id,    
            layout=self.layout,
            end_point=self.end_point,
            task_instructions=self.task_instructions,
            task_complete=self.task_complete,
            current_section=self.current_section,
            human_speaks_first=self.human_speaks_first,
            user_accepted_task=self.user_accepted,          
            previous_messages=self.previous_messages,
            agents_resigned=self.agents_resigned,
            assignment_id=self.assignment_id,
            move_instructions_to_top=self.move_instructions_to_top,
            move_instructions_to_bottom=not self.move_instructions_to_top,
            prefix_message=self.prefix_message,
            show_page_number=self.show_page_number,
        )

    @property
    def user_accepted(self):        
        # This condition means we are on the preview page
        if 'assignment_id' in self.__dict__ and 'hit_id' in self.__dict__ and not 'worker_id' in self.__dict__:
            return False             
        return True