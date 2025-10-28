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
    
    button_value = str(ctx.triggered_id["index"])
    operators = ["+", "-", "x", "÷", "%"]

    if not current_display or current_display == "0":
        if button_value in operators or button_value == ".":
            return current_display
        else:
            return button_value
        
    if button_value == "C":
        return "0"
    
    elif button_value == "CE":
        return current_display[:-1] if len(current_display) > 1 else "0"
    
    elif button_value == "=":
        try:
            return str(evaluate_expression(current_display))
        except Exception:
            return "Erro"
        
    if current_display[-1] in operators and button_value in operators:
        return current_display
    
    if button_value == ".":
        last_number = current_display.split("+")[-1].split("x")[-1].split("÷")[-1]
        if "." in last_number:
            return current_display
    
    new_display = current_display + button_value 
    return new_display
