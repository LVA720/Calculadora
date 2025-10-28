from dash import Input, Output, ALL, callback, ctx, State
from logic.calculator_logic import evaluate_expression
import re
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

    if len(current_display) >= 14 and button_value not in ["C", "CE", "="]:
        return current_display
    if button_value in operators:
        if current_display[-1] in operators:
            return current_display[:-1] + button_value
        else:
            return current_display + button_value

    if not current_display or current_display == "0":
        if button_value in operators:
            return current_display
        elif button_value == ".":
            return "0."
        elif button_value in ["C", "CE"]:
            return "0"
        else:
            return button_value

    button_value = ctx.triggered_id["index"]

    if not current_display:
        current_display = "0"

    if button_value == "C":
        return "0"
    elif button_value == "CE":
        return current_display[:-1] if len(current_display) > 1 else "0"
    elif button_value == "=":
        try:
            result = str(evaluate_expression(current_display))
            result = round(float(result),10)
            result_str = str(result).rstrip("0").rstrip(".") if "." in str(result) else str(result)
            return result_str
        except Exception:
            return "Erro"

    if button_value == ".":
        last_number = re.split(r"[+\-x÷%]", current_display)[-1]
        if current_display[-1] in operators:
            return current_display + "0."
        if "." in last_number:
            return current_display
        return current_display + "."
    
    if not current_display or current_display == "0":
        if button_value in operators:
            return current_display
        else:
            return button_value

    return current_display + str(button_value)
