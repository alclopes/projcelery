# PRJ02 - Celery Project Comands - English
- [Celery Project Comands (ENG)](#eng)
- [Celery Project Comands (PT)](https://github.com/alclopes/projCelery/blob/master/proj02/README_PT.md)

<div id='eng'/>  

## Terminal 01 => Run Worker

### By default
     $ cd proj02
     $ celery -A proj worker --loglevel = info

### Alternative for Windows to work with celery 4.
     $ cd proj02
     $ celery -A proj worker --pool = solo -l info

## Terminal 02 => Run Task
     $ cd proj02
     $ python ./manage.py shell
     >>> from myapp.tasks import add
     >>> res = add.delay (2,3)
     >>> res.get ()

