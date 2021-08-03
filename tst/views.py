from django.shortcuts import render, HttpResponse
from django_q.tasks import async_task, schedule, AsyncTask, Schedule
from django.core import management




def index(request):
    async_task(
        'tst.commands.hi_index',
        'Alex'
    )
    return HttpResponse('Index')

def schedul(request):
    schedule(
        'tst.commands.hi_sched',
        'Alex',
        name='Sheduller - hi_shed'
    )
    return HttpResponse('<h1>Shedule</h1>')

def task(request):
    pass

def cancell(request):
    async_task(
        'django.core.management.call_command',
        'clearsessions',
    )
    print('Asunc task dane!')
    return HttpResponse('Must be cancelled all')

# wrapping `manage.py clearsessions`
def clear_sessions_command(request):
    return management.call_command('clearsessions')