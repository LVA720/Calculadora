from dash import Input, Output, ALL, callback, ctx, State
from logic.calculator_logic import evaluate_expression
@callback(
    Output("display", "children"),
    Input({"type": "button", "index": ALL}, "n_clicks"),
    State("display", "children"),
    prevent_initial_call=True
)

def on_click(n_clicks, current_display):
    if not ctx.triggered_id:
        return current_display or "0"
    button = ctx.triggered_id
    if button == "C":
        return "0"
    elif button == "CE":
        return current_display[:-1] if len(current_display) > 1 else "0"
    elif button == "=":
        try:
            return str(evaluate_expression(current_display))
        except Exception:
            return "Erro"
    else:
        if current_display == "0":
            current_display = ""
            return current_display + str(button)
    