from dash import html
import dash_bootstrap_components as dbc

def create_buttom():
    buttons = html.Div(
        [
            dbc.Button("ON/C", color="dark", className="me-1",style={"color": "#058105"}),
            dbc.Button("CE", color="dark", className="me-1",style={"color": "#058105"}),
            dbc.Button("MRC", color="dark", className="me-1",style={"color": "#058105"}),
            dbc.Button("M-", color="dark", className="me-1",style={"color": "#058105"}),
            dbc.Button("M+", color="dark", className="me-1",style={"color": "#058105"}),
            dbc.Button("7", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("8", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("9", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("%", color="dark", className="me-1",style={"color": "#058105"}),
            dbc.Button("√", color="dark", className="me-1",style={"color": "#058105"}),
            dbc.Button("4", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("5", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("6", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("X", color="dark", className="me-1",style={"color": "#058105"}),
            dbc.Button("÷", color="dark", className="me-1",style={"color": "#058105"}),
            dbc.Button("1", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("2", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("3", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("+", color="dark", className="me-1",style={"color": "#058105"}),
            dbc.Button("-", color="dark", className="me-1",style={"color": "#058105"}),
            dbc.Button("0", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button(".", color="dark", className="me-1",style={"color": "#058105"}),
            dbc.Button("+/-", color="dark", className="me-1",style={"color": "#058105"}),
            dbc.Button("=", color="dark", className="me-1",style={"color": "#058105"})
        ],
        style={
        "display": "grid",
        "gridTemplateColumns": "repeat(5, 1fr)",  # 3列
        "gap": "10px",
        "width": "100%",
        "margin": "auto"
    }
)
    return html.Div([buttons], style={"padding": "10px"})