"""An Import Wrapper for settings.py in config."""

from config import settings
from config.build import task_build


class Settings:

    def __init__(self):
        # Update task instructions        
        self.__dict__.update(**settings.database)
        self.__dict__.update(**settings.task)
        self.__dict__.update(**settings.server)
        self.__dict__.update(**settings.mturk)
        self.task_build = task_build
        self.task_instructions = [x for x in self.task_instructions.strip().replace("    ", "").split("\n") if x != ""]