import time
import os
from threading import Thread


def start_server(s):
    print 'INFO: Thread {} enabled'.format(s)
    time.sleep(0)
    os.system('python manage.py runserver')


def get_request(s):
    print 'INFO: Thread {} enabled'.format(s)
    time.sleep(5)
    os.system('python getrequest.py')


t1 = Thread(target=start_server, args=('runserver',))
t2 = Thread(target=get_request, args=('get request',))

t2.start()
t1.start()
