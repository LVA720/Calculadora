from dash import Dash
from layout.calculator_layout import Layout
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = Layout.create_layout()

if __name__ == "__main__":
    app.run(debug=True)
