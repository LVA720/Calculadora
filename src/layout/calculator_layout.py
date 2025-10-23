
from dash import Dash, html, dash
import dash_bootstrap_components as dbc

def create_layout():
    card = dbc.Container(
        dbc.Card(
            [
                dbc.Row(
                    [
                        dbc.Col(dbc.Card([ 
                            dbc.CardHeader("Ben 10"),
                            dbc.CardBody("0", 
                                        style={
                                            "backgroundColor": "black",
                                            "fontSize": "48px",
                                            "textAlign": "right",
                                            "height": "20px",
                                            "borderRadius": "10px",
                                            "padding": "8px",
                                            "marginBottom": "470px"})],
                            color="success", 
                            inverse=True,
                            class_name="mb-4",
                            style={"width": "432px", "height": "600px", "margin": "auto", "margin-top": "60px"})),
                    ]
                )
            ]
        ))
    return card

def create_layout():
    buttons = html.Div(
        [
            dbc.Button("ON/C", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("CE", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("MRC", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("M-", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("M+", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("7", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("8", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("9", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("%", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("√", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("4", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("5", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("6", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("X", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("÷", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("1", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("2", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("3", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("+", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("-", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("0", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button(".", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("+/=", color="light", className="me-1",style={"color": "#058105"}),
            dbc.Button("=", color="light", className="me-1",style={"color": "#058105"})
        ],
        style={
        "display": "grid",
        "gridTemplateColumns": "repeat(5, 1fr)",  # 3列
        "gap": "10px",
        "width": "120px",
        "margin": "auto"
    }
)
    return html.Div([buttons], style={"padding": "20px"})

#    return html.Div(
#        children=[
#            html.Center(html.H1("Calculadora muito foda")),
#            html.Div(children="Texto", style={"backgroundColor": "#127207", "padding": "10px", "textAlign": "center"}),
#            html.Div(children=[html.Center(html.H1("Display"))])
#        ],
#        #style={"border": "10px solid black", "padding": "50px"}
#    )
