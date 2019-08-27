# PRJ02 - Comandos Celery Project - Português
- [Comandos Celery Project (ENG)](https://github.com/alclopes/projCelery/blob/master/proj02/README.md)
- [Comandos Celery Project (PT)](#pt)

<div id='pt'/>  

## Terminal 01 => Rodar o Worker
### Por padrão
    $ cd proj02
    $ celery -A proj worker --loglevel=info

### Alternativa para o Windos trabalhar com celery 4.
    $ cd proj02
    $ celery -A proj worker --pool=solo -l info

## Terminal 02 => Rodar a Task
    $ cd proj02
    $ python ./manage.py shell
    >>> from myapp.tasks import add
    >>> res = add.delay(2,3)
    >>> res.get()

