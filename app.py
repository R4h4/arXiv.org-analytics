# -*- coding: utf-8 -*-
import dash
import os
from random import randint

external_stylesheets = ["https://fonts.googleapis.com/icon?family=Material+Icons",
                        'https://unpkg.com/material-components-web@latest/dist/material-components-web.min.css']

external_scripts = ['https://unpkg.com/material-components-web@latest/dist/material-components-web.min.js']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, external_scripts=external_scripts)
app.config.suppress_callback_exceptions = True
server = app.server
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
