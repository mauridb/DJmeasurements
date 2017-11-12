# -*- coding: utf-8 -*-
from __future__ import with_statement
from fabric.api import *

import time
import thread


def pull():
    local('git pull origin master')


def install():
    local('pip install -r requirements.txt')


# VCS fab track_dev:COMMIT MESSAGE
def track_dev(message):
    print message
    '''
    track branch dev to VCS
    :param message: 
    '''
    local('git add .')
    local('git commit -am "{}"'.format(message))
    local('git push origin dev')


def prepare_master():
    local('git checkout master')
    local('git merge dev')
    local('git push origin master')
    local('git checkout dev')


# fab start_app:'APPLICATION-NAME'
def start_app(message):
    local('python manage.py startapp {}'.format(message))


def migrate():
    local('python manage.py makemigrations')
    local('python manage.py migrate')


def create_superuser():
    local('python manage.py createsuperuser')


# $ fab start
def start():
    local('python manage.py runserver')


# $ fab start
def start_rpi3():
    local('python multithread.py')



