#all imports
import os
import sqlite3
from flask import *


app=Flask(__name__)
app.config.from_object(__name__)

#load default config and override config from an environemnt variable

app.config.update(dict(
    DATABASE=os.path.join(app.root_path,'triny.db'),
    SECRET KEY='developemnet key',
    USERNAME='ADMIN',
    PASSWORD='DEFAULT'
))

def connect_db():
    rv=sqlite3.connect(app.config['DATABASE])
    rv.row_factory=sqlite3.Row
    return rv

def get_db():
    #opens a new db connection if there is none yet for the current application context
    if not hasattr(g,'sqlite_db'):
        g.sqlite_db=connect_db()
    return g.sqlite-db