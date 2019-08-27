from __future__ import absolute_import
from celery import Celery

import os
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

# app = Celery('proj',
#              broker='amqp://guest:guest@localhost//',
#              backend='amqp://guest:guest@localhost//',
#              include=['proj.tasks'])

app = Celery('proj',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0',
             include=['proj.tasks'])


# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
    app.start()
