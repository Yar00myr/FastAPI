from .. import app


@app.get("/")
def main():
    return {"hello": "world"}


@app.get("/calculate/{operation}/{num1}/{num2}")
def calculate(operation: str, num1: int, num2: int):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    else:
        return {"error": "Invalid operation"}
    return {"result": result}
