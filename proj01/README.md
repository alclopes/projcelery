# PRJ01 - Celery Project Comands - English
- [Celery Project Comands (ENG)](#eng)
- [Celery Project Comands (PT)](https://github.com/alclopes/projCelery/blob/master/proj01/README_PT.md)

<div id='eng'/>  

# Terminal 01 => Run Worker

## By default
    $ cd proj01
    $ celery -A proj worker --loglevel=info

## Alternative for Windows to work with celery 4.
    $ cd proj01
    $ celery -A proj worker --pool=solo -l info

# Terminal 02 => Run Task
    $ cd proj01
    $ python test.py


