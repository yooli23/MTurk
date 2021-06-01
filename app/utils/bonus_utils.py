from mturk.api import API
from database import view
from config.bonus import should_pay_worker_bonus


def pay_bonus(task_id: str):
    hit = view.hit(task_id=task_id)
    pay_bonus = should_pay_worker_bonus(task_id)
    try:
        mturk_api = API()
        mturk_api.worker_complete_task(hit.worker_id, hit.assignment_id, hit.hit_id, hit.task_group_id, pay_bonus=pay_bonus)
    except Exception as error:
        print("Error calling 'worker_complete_task':", error)