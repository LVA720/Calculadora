from dash import Dash
import dash_bootstrap_components as dbc
app = Dash(__name__)

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

#    return html.Div(
#        children=[
#            html.Center(html.H1("Calculadora muito foda")),
#            html.Div(children="Texto", style={"backgroundColor": "#127207", "padding": "10px", "textAlign": "center"}),
#            html.Div(children=[html.Center(html.H1("Display"))])
#        ],
#        #style={"border": "10px solid black", "padding": "50px"}
#    )
