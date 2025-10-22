import dash_bootstrap_components as dbc
from dash import html,Dash


def create_layout():
    buttons = html.Div(
        [
            dbc.Button("7", color="success", className="me-1"),
            dbc.Button("8", color="success", className="me-1"),
            dbc.Button("9", color="success", className="me-1"),
            dbc.Button("%", color="success", className="me-1"),
            dbc.Button("√", color="success", className="me-1"),
            dbc.Button("4", color="success", className="me-1"),
            dbc.Button("5", color="success", className="me-1"),
            dbc.Button("6", color="success", className="me-1"),
            dbc.Button("X", color="success", className="me-1"),
            dbc.Button("÷", color="success", className="me-1"),
            dbc.Button("1", color="success", className="me-1"),
            dbc.Button("2", color="success", className="me-1"),
            dbc.Button("3", color="success", className="me-1"),
            dbc.Button("+", color="success", className="me-1"),
            dbc.Button("-", color="success", className="me-1"),
            dbc.Button("0", color="success", className="me-1"),
            dbc.Button(".", color="success", className="me-1"),
            dbc.Button("+/=", color="success", className="me-1"),
            dbc.Button("=", color="success", className="me-1")
        ],
        style={
        "display": "grid",
        "gridTemplateColumns": "repeat(5, 1fr)",  # 3列
        "gap": "10px",
        "width": "200px",
        "margin": "auto"
    }
)
    return html.Div([buttons], style={"padding": "20px"})

