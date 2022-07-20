import logging
from flask import Flask
from logging.config import dictConfig
from flask.logging import  default_handler

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'WARNING',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
app.logger.removeHandler(default_handler)
wsgi_app = app.wsgi_app



import FlaskExercise.views