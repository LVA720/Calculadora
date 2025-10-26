from sympy import sympify, sqrt
import re  # ← 正規表現モジュールを使う

def evaluate_expression(expression: str):
    try:
        expression = expression.replace('÷', '/').replace('X', '*')
        
        expression = expression.replace('%', '/100')

        expression = re.sub(r'√(\d+)', r'sqrt(\1)', expression)

        result = sympify(expression, evaluate=True, locals={"sqrt": sqrt})

        return float(result.evalf())
    except Exception as e:
        print("計算中にエラー:", e)
        return "Error"


