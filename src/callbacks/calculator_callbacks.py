
from dash import Input, Output, ALL, callback, ctx, State
from logic.calculator_logic import evaluate_expression
import re

operators = ["+", "-", "x", "÷", "%"]

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

    #limite de 12 caracteres
    if len(current_display) >= 14 and button_value not in ["ON/C", "CE", "="]:
        return current_display

    #limpar ou 0
    if button_value == "ON/C":
        return "0"
    if button_value == "CE":
        return current_display[:-1] if len(current_display) > 1 else "0"

    #operadores
    if button_value in operators:
        if last_op == "√": #impede operador depois de √
            return current_display
        if last_op in operators:
            if button_value == "-" and last_op != "-": #permite o uso de -
                return current_display + "-"
            if len(current_display) >= 2 and current_display[-2] in operators: #substitui pelo novo
                return current_display[:-2] + button_value
            return current_display[:-1] + button_value
        
        return current_display + button_value
    
    #numeros iniciais / display vazio
    if current_display == "0":
        if button_value == "-":
            return "-"
        elif button_value in operators:
            return "0"
        elif button_value == ".":
            return "0."
        elif button_value == "√":
            return "√"
        else:
            return button_value
        
    #raiz quadrada
    if button_value == "√":
        if last_op == "√":
            return current_display #evita duplo √
        if last_op.isdigit(): #insere multiplicacao
            return current_display + "x√"
        if last_op in operators:
            return current_display + "√"
        return current_display + "√"

    #ponto decimal
    if button_value == ".":
        last_number = re.split(r"[+\-x÷%]", current_display)[-1] #numero atual depois do ultimo operador
        if "." in last_number: #evitar duplo .
            return current_display
        if last_op in operators:
            return current_display + "0."
        return current_display + "."

    #igual
    if button_value == "=":
        try:
            result = evaluate_expression(current_display)
            result = round(float(result), 10)
            result_str = str(result).rstrip("0").rstrip(".") if "." in str(result) else str(result)
            return result_str
        except Exception:
            return "Erro"

    return current_display + str(button_value)
