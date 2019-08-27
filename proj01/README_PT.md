
# PRJ01 - Comandos Celery Project - Português
- [Celery Project (ENG)](https://github.com/alclopes/projCelery/blob/master/proj01/README.md)
- [Celery Project (PT)](#pt)

<div id='pt'/>  

# Terminal 01 => Rodar o Worker

## Por padrão
    $ cd proj01
    $ celery -A proj worker --loglevel=info

## Alternativa para o Windows trabalhar com celery 4.
    $ cd proj01
    $ celery -A proj worker --pool=solo -l info

# Terminal 02 => Rodar a Task
    $ cd proj01
    $ python test.py

