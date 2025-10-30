
from dash import Input, Output, ALL, callback, ctx, State
from logic.calculator_logic import evaluate_expression
import re#tardado

operators = ["+", "-", "x", "÷", "%"]

def replace(display, value):
    if display != "0":
        return None
    if value in ("-", "√"):
        return value
    if value == ".":
        return "0."
    if value in operators or value == "=":
        return "0"
    return value

def handle_operator(display, value):
    last_op = display[-1]
    if display == "-":
        return "0"
    if last_op == "√": #impede operador depois de √
        return display
    if last_op in operators:
        if value == "-" and last_op != "-": #permite o uso de -
            return display + "-"
        if len(display) >= 2 and display[-2] in operators: #substitui pelo novo
            return display[:-2] + value
        return display [:-1] + value
    return display + value

def decimal(display):
    last_op = display[-1]
    last_number = re.split(r"[+\-x÷%]",display)[-1] #numero atual depois do ultimo operador
    if "." in last_number:
        return display
    if last_op in operators:
        return display + "0."
    return display + "."

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
    current_display = current_display or "0"
    last_op = current_display[-1]

    #limite de 14 caracteres
    if len(current_display) >= 14 and button_value not in ["ON/C", "CE", "="]:
        return current_display

    #limpar ou 0
    if button_value == "ON/C":
        return "0"
    if button_value == "CE":
        return current_display[:-1] if len(current_display) > 1 else "0"

    #numeros iniciais / display vazio
    if current_display == "0":
        return replace(current_display, button_value)

    #operadores
    if button_value in operators:
        return handle_operator(current_display, button_value)

    #ponto decimal
    if button_value == ".":
        return decimal(current_display)

    #raiz quadrada
    if button_value == "√":
        if last_op == "√":
            return current_display #evita duplo √
        if last_op.isdigit(): #insere multiplicacao
            fix = "x" if last_op.isdigit() else ""
        return current_display + fix + "√"

    #ingual
    if button_value == "=":
        try:
            result = evaluate_expression(current_display)
            result = round(float(result), 10)
            result_str = str(result).rstrip("0").rstrip(".") if "." in str(result) else str(result)
            return result_str
        except Exception:
            return "Erro"

    return current_display + str(button_value)
