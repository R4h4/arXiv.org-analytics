# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, Event
import plotly.graph_objs as go
import pandas as pd
import json

from app import app

app.title = 'arXiv.org Analytics Dashboard'

with open('data/arXiv_categories.json') as json_file:
    categories = json.load(json_file)

df = pd.read_csv('data/20190105_arXiv_monthly_submissions.csv')

layout = html.Div(
    className='app-layout',
    children=[
        html.H1(
            children='arXiv.org Overview'
        ),
        html.Div(
            children=(
                dcc.Graph(
                    figure={
                        'data': [
                            go.Scatter(
                                x=df.iloc[:-1]['month'],
                                y=df.iloc[:-1]['submissions']
                            )
                        ],
                        'layout': {
                            'title': "Monthly submissions"
                        }
                    }
                )
            )
        )
    ]
)
