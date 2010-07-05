#!/usr/local/python
# encoding:utf-8
from juno import *

Person = model('Person', name='string')


@route('/')
def index(web):
    return template("index.html", {
        'messages':'Juno says hi',
    })


@route('/hello')
def index(web):
    return 'Hello!'


@route('/create')
def create(web):
    return template("create.html", {})


@post('/create2')
def createProcess(web):

    user = Person()
    user.name = web.input('user')
    user.save()
    return 'Done!'


@route('/list')
def showList(web):
    users = Person.find().all()
    return template('list.html', {'users':users})



run()
