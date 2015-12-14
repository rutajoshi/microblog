
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views    #This app is not the same as the variable app. This is a package.
