import json

from database.database import Database, Inspector


class HIT:

    def __init__(self, task_id=None, hit_id=None):
        super().__init__()
        if task_id is not None:
            self.task_id = task_id
            self.inspector = Inspector(task_id)
            self.__dict__.update(self.info)
            self.task_group_id = self.inspector.hit_info['task_group_id']
        if hit_id is not None:
            self.hit_id = hit_id

    @property
    def info(self):
        try:
            data = self.inspector.hit_info
            del data['task_group_id']
            return data
        except:
            return {}

    @property
    def complete(self):
        try:
            return self.inspector.task_info['complete']
        except:
            return False

    @property
    def human_speaks_first(self):
        try:
            return self.inspector.task_info['human_speaks_first']
        except:
            return None

    @property
    def dialog(self):
        try:
            result = {}
            for agent in self.inspector.agents:            
                result[agent] = Database().load_messages(self.task_id, agent)
            return result
        except:
            return {}

    @property
    def forms(self):
        try:
            result = {}
            for form in self.inspector.forms:            
                result[form] = self.inspector.form_data(form).replace('""', '"').replace("''", "'").replace('\n', '')
                result[form] = json.loads(result[form])
            return result
        except Exception as error:
            print("Error retreiving form data in hit.py:", error)
            return {}