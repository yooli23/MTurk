from mturk.api import API
from database import view


def should_pay_worker_bonus(task_id: str):    
    hit = view.hit(task_id=task_id)
    data = hit.forms
    # if data['survey_1']['likes_movies'] == True:
    #   return True
    # return False
    return hit.complete