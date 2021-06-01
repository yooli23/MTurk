"""
You can ignore this class. You do not need to change or
configure anything inside of this class.
"""

from collections import defaultdict
from enum import Enum, auto
import json

from config.settings import task


# Page

class Page:

    def __init__(self, title="Welcome task!", text="Please click next button.", text_font_size=15, next_button_text="Next"):
        super().__init__()
        self.title = title
        self.text = text.replace("\n", "<br>").strip()
        self.next_button_text = next_button_text
        self.text_font_size = text_font_size

    @property
    def content(self):
        return {'type': 'page', 'data': {'title': self.title, 'text': self.text, 'next_button_text': self.next_button_text, 'text_font_size': self.text_font_size}}

class WelcomePage(Page):

    def __init__(self, text_font_size=15):        
        super().__init__(title=task['task_name'], text=task['task_instructions'], next_button_text='Begin Task', text_font_size=text_font_size)

class FinishPage(Page):

    def __init__(self):
        super().__init__(title="Task Complete!", text="Thank you for completing the task.", next_button_text='Submit HIT')


# Form
    
class QuestionType(Enum):
    Unknown = auto()
    FreeResponse = auto()
    MultiChoice = auto()
    CheckBox = auto()
    Likert = auto()

class SurveyQuestion:
    
    def __init__(self, title:str, question_type : QuestionType, required : bool):
        self._title = title.replace("\n", "\\n").strip()
        self._question_type = question_type
        self._required = required

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def question_type(self):
        return self._question_type

    @question_type.setter
    def question_type(self, value):
        self._question_type = value

    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value

    def meta_data(self):
        return {"title":self.title, "type":self.question_type.name, "required":self.required}

class Form:
    """
    Questions: a list of dictionary objects.
    """

    def __init__(self, title, *args):     
        self.title = title.replace("\n", "\\n").strip()   
        self.sections = []
        for item in args:                                    
            self.sections.append(item.content)
    
    @property
    def content(self):
        return {'title':self.title, 'data': self.sections, 'type': 'form'}

class Section:

    def __init__(self, title, *args):
        self.title = title.replace("\n", "\\n").strip()
        self.questions = []
        for item in args:                                    
            self.questions.append(item.content)

    @property
    def content(self):
        return {'title':self.title, 'data': self.questions, 'type': 'section'}

class FreeResponse(SurveyQuestion):
    """
    Title: the title of the question
    Placeholder: the placeholder value of the free response 
    """

    def __init__(self, title:str="", required=True):
        super().__init__(title=title,  question_type=QuestionType.FreeResponse, required=required)
        
    @property
    def content(self):        
        return self.meta_data()   

class CheckBox(SurveyQuestion):
    
    def __init__(self, title:str="", items: list = [], required=True):
        super().__init__(title=title,  question_type=QuestionType.CheckBox, required=required)
        self.items = items
        
    @property
    def content(self):   
        data = self.meta_data()
        data['items'] = self.items
        return data               

class MultiChoice(SurveyQuestion):
    """
    Title : the title of the question
    Items : a list of strings
    """
    
    def __init__(self, title:str="", items:list=[], required=True):
        super().__init__(title, QuestionType.MultiChoice, required=required)
        self.items = items

    @property
    def content(self):   
        data = self.meta_data()
        data['items'] = self.items
        return data        

class Likert(SurveyQuestion):

    def __init__(self, title:str="", min_rating: int = 1, max_rating: int = 5, min_desc: str = "", max_desc: str = "", required=True):
        super().__init__(title, QuestionType.Likert, required=required)
        self.min_rating = min_rating
        self.max_rating = max_rating
        self.min_desc = min_desc
        self.max_desc = max_desc

    @property
    def content(self):   
        data = self.meta_data()
        data['min_rating'] = self.min_rating
        data['max_rating'] = self.max_rating
        data['min_desc'] = self.min_desc.replace("\n", "\\n").strip()
        data['max_desc'] = self.max_desc.replace("\n", "\\n").strip()
        return data 


# Task

class Task:
    
    def __init__(self, *args):
        super().__init__()

        if type(args[0]) is str:
            self.default_instructions = False
            self.instructions = args[0]
        else:
            self.default_instructions = True    
            self.instructions = task['task_instructions']        

        self.items = []
        for item in args:
            if type(item) is str:
                continue
            if type(item) is not Agent:
                raise Exception("Tasks can only contain Agents.")
            self.items.append(item)
    
    @property
    def content(self):
        agents = []
        for agent in self.items:
            agents.append({'type': 'agent', 'data': agent.to_json()})
        return {'type': 'task', 'data': agents, 'instructions': self.instructions.replace("\n", "<br>").strip()}

class AgentColor(Enum):
    RED = auto()
    BLUE = auto()
    YELLOW = auto()
    GREEN = auto()
    PURPLE = auto()
    ORANGE = auto()
    CYAN = auto()
    MINT = auto()

class Agent:

    def __init__(self, color: AgentColor = AgentColor.BLUE, name: str = "", title: str = ""):
        super().__init__()
        self.color = color        
        self.name = name
        self.title = title

    def to_json(self):
        return {'color': self.color.name.lower(), 'name': self.name, 'title': self.title.replace("\n", "\\n").strip()}

