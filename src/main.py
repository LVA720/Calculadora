from dash import Dash
from layout import calculator_layout
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = calculator_layout.create_layout()

if __name__ == "__main__":
    app.run(debug=True)
