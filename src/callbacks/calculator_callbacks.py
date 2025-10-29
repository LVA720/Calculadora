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

    #limite de 12 caracteres
    if len(current_display) >= 14 and button_value not in ["C", "CE", "="]:
        return current_display

    #operadores
    last_op = current_display[-1]
    if button_value in operators:
        if last_op in operators and button_value == "-":
            if button_value == "-" and last_op != "-":
                return current_display + button_value
            elif last_op in operators:
                return current_display[:-1] + button_value
        elif last_op == "√":
            return current_display
        else:
            return current_display + button_value

    #limpar ou 0
    if not current_display or current_display == "0":
        if button_value in operators:
            return current_display
        elif button_value == ".":
            return "0."
        elif button_value in ["C", "CE"]:
            return "0"
        else:
            return button_value

    #raiz quadrada
    if button_value == "√":
        if current_display == "0":
            return "√"
        last_op = current_display[-1]
        if last_op in operators:
            return current_display + "√"
        elif last_op == "√":
            return current_display
        elif last_op.isdigit():
            return current_display + "x√"
        else:
            return current_display + "√"

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
