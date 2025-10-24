from sympy import sympify

def evaluate_expression(expression:str):
    try:
        expression = expression.replace('÷','/').replace('X','*')

        expression = expression.replace('√','sqrt')

        expression = expression.replace('%','/100')

        result = sympify(expression,evaluate=True)

        return float(result.evalf())
    except Exception as e:
        print("計算中にエラー:", e)
        return "Error"




