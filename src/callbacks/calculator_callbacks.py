import dash_bootstrap_components as dbc
from dash import html,Dash,Input,Output
from src.callbacks.calculator_callbacks import create_layout

create_layout().n_clicks=0