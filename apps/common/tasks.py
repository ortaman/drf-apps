
from celery import shared_task


@shared_task
def test_celery_task():
    print('Hello celery task')
    return 'test_celery_task'


@shared_task
def test_celery_beat_task():
    print('Hello celery beat')
    return 'test_celery_beat_task'
