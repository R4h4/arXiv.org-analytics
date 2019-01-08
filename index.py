# -*- coding: utf-8 -*
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app, server  # Import server for Gunicorn
from apps import app_overview

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return app_overview.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True, threaded=True)
