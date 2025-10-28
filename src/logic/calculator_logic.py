
from sympy import sympify, sqrt
import re  

def evaluate_expression(expression: str):
    try:
        expression = expression.replace('÷', '/')
        
        expression = expression.replace('x', '*')

        expression = expression.replace('%', '/100')

        expression = expression.replace('M+', '+').replace('M-','-')



        expression = re.sub(r'√(\d+)', r'sqrt(\1)', expression)

        result = sympify(expression, evaluate=True, locals={"sqrt": sqrt})

        return float(result.evalf())
    except Exception as e:
        print("計算中にエラー:", e)
        return "Error"
