
from dash import html
import dash_bootstrap_components as dbc
from layout.calculator_button import create_buttom

class Layout():
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
                                                "height": "100px",
                                                "borderRadius": "10px",
                                                "padding": "10px",
                                                "marginBottom": "20px",
                                                "flex": "0 0 auto"}),
                                                dbc.Card(
                                                    dbc.CardBody(
                                                        html.Img(
                                                            src="/assets/ben10_logo.png",
                                                            style={
                                                                "display": "block",
                                                                "margin": "0 auto",
                                                                "width": "120px",
                                                                "height": "auto"
                                                            }
                                                        )
                                                    ),
                                                    color="success",
                                                    inverse=True,
                                                    class_name="mb-2",
                                                    style={"border": "none"}
                                                ),
                                                create_buttom()
                                            ],
                                color="success", 
                                inverse=True,
                                class_name="mb-4",
                                style={"width": "432px", 
                                        "height": "600px",
                                        "margin": "auto", 
                                        "margin-top": "60px"})),
                        ]
                    )
                ]
            ))
        return card

#    return html.Div(
#        children=[
#            html.Center(html.H1("Calculadora muito foda")),
#            html.Div(children="Texto", style={"backgroundColor": "#127207", "padding": "10px", "textAlign": "center"}),
#            html.Div(children=[html.Center(html.H1("Display"))])
#        ],
#        #style={"border": "10px solid black", "padding": "50px"}
#    )
