from celery import shared_task


@shared_task  #shared task são tarefas a quais chamando na sua view e colocar .delay()
def add(x, y):
    pass