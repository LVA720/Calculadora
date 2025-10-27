
import dash_bootstrap_components as dbc
from dash import Dash

from layout.calculator_layout import Layout
import callbacks.calculator_callbacks 

from layout.calculator_layout import create_layout,Layout



app = Dash(__name__,external_stylesheets=[dbc.themes.DARKLY])
app.layout = Layout.create_layout()


if __name__=="__main__":
    app.run(debug=True)
