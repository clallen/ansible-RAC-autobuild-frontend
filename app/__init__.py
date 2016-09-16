from flask import Flask, session
from flask_session import Session

app = Flask(__name__)
app.config.from_object('config')

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

from app import views
