from dash import html
import dash_bootstrap_components as dbc

def create_buttom():
    layout = [
        ["ON/C","CE","MRC","M-","M+"],
        ["7","8","9","%","√"],
        ["4","5","6","x","÷"],
        ["1","2","3","+","-"],
        ["0",".","+/-","="]
    ]

    buttons=[]
    for row in layout:
        for label in row:
            color = "light" if label.isdigit() else "dark"
            button = dbc.Button(
                label,
                color=color,
                id={"type":"button","index":label},
                className="me-1",
                style={"color":"#058105"}
            )
            buttons.append(button)

    return html.Div(
        buttons,
        style={
            "display": "grid",
            "gridTemplateColumns":"repeat(5,1fr)",
            "gap": "10px",
            "width":"100%",
            "margin":"auto",
        },
    )
