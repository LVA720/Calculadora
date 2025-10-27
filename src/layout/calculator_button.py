from dash import html
import dash_bootstrap_components as dbc

def create_buttom():
    buttons = html.Div(
        [
            dbc.Button("ON/C", color="dark",id={"type": "button", "index": "C"}, className="me-1",style={"color": "#058105"}),
            dbc.Button("CE", color="dark",id={"type": "button", "index": "CE"}, className="me-1",style={"color": "#058105"}),
            dbc.Button("MRC", color="dark",id={"type": "button", "index": "MRC"}, className="me-1",style={"color": "#058105"}),
            dbc.Button("M-", color="dark",id={"type": "button", "index": "M-"}, className="me-1",style={"color": "#058105"}),
            dbc.Button("M+", color="dark",id={"type": "button", "index": "M+"}, className="me-1",style={"color": "#058105"}),
            dbc.Button("7", color="light",id={"type": "button", "index": 7}, className="me-1",style={"color": "#058105"}),
            dbc.Button("8", color="light",id={"type": "button", "index": 8}, className="me-1",style={"color": "#058105"}),
            dbc.Button("9", color="light",id={"type": "button", "index": 9}, className="me-1",style={"color": "#058105"}),
            dbc.Button("%", color="dark",id={"type": "button", "index": "%"}, className="me-1",style={"color": "#058105"}),
            dbc.Button("√", color="dark",id={"type": "button", "index": "√"}, className="me-1",style={"color": "#058105"}),
            dbc.Button("4", color="light",id={"type": "button", "index": 4}, className="me-1",style={"color": "#058105"}),
            dbc.Button("5", color="light",id={"type": "button", "index": 5}, className="me-1",style={"color": "#058105"}),
            dbc.Button("6", color="light",id={"type": "button", "index": 6}, className="me-1",style={"color": "#058105"}),
            dbc.Button("X", color="dark",id={"type": "button", "index": "x"}, className="me-1",style={"color": "#058105"}),
            dbc.Button("÷", color="dark",id={"type": "button", "index": "÷"}, className="me-1",style={"color": "#058105"}),
            dbc.Button("1", color="light",id={"type": "button", "index": 1}, className="me-1",style={"color": "#058105"}),
            dbc.Button("2", color="light",id={"type": "button", "index": 2}, className="me-1",style={"color": "#058105"}),
            dbc.Button("3", color="light",id={"type": "button", "index": 3}, className="me-1",style={"color": "#058105"}),
            dbc.Button("+", color="dark",id={"type": "button", "index": "+"}, className="me-1",style={"color": "#058105"}),
            dbc.Button("-", color="dark",id={"type": "button", "index": "-"}, className="me-1",style={"color": "#058105"}),
            dbc.Button("0", color="light",id={"type": "button", "index": 0}, className="me-1",style={"color": "#058105"}),
            dbc.Button(".", color="dark",id={"type": "button", "index": "."}, className="me-1",style={"color": "#058105"}),
            dbc.Button("+/-", color="dark",id={"type": "button", "index": "+/-"}, className="me-1",style={"color": "#058105"}),
            dbc.Button("=", color="dark",id={"type": "button", "index": "="}, className="me-1",style={"color": "#058105"})
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