from database.database import Database, Inspector
from database.hit import HIT


def all():
    hits = [HIT(task_id) for task_id in Inspector().task_ids]
    all_hit_ids = Inspector().linked_hit_ids
    for hit_id in all_hit_ids:
        if hit_id not in [x.hit_id for x in hits]:
            hits.append(HIT(hit_id=hit_id))
    return hits


def hit(task_id=None, hit_id=None):
    if task_id is not None:
        return HIT(task_id)
    elif hit_id is not None:
        try:
            return HIT(task_id=Inspector().task_id_from_hit_id(hit_id))
        except:
            raise Exception("Could not find 'hit' from the given 'hit_id'.")
    raise Exception("Please provide a task_id or hit_id to retrieve a 'hit' from the database.")