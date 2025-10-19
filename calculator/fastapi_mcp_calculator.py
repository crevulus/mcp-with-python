from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI(title="Calculator API", version="1.0.0")

# Base API
@app.post("/multiply")
def multiply(a: float, b: float) -> dict:
    """
    Multiplies two numbers and returns the result.

    args: a (float): The first number.
          b (float): The second number.

    returns: float: The product of the two numbers.
    """
    return {"result": a * b}

@app.post("/add")
def add(a: float, b: float) -> dict:
    """
    Adds two numbers and returns the result.
    """
    return {"result": a + b}

@app.post("/subtract")
def subtract(a: float, b: float) -> dict:
    """
    Subtracts the second number from the first number and returns the result.
    """
    return {"result": a - b}

@app.post("/divide")
def divide(a: float, b: float) -> dict:
    """
    Divides the first number by the second number and returns the result.
    Raises an error if division by zero is attempted.
    """
    if b == 0:
        return {"error": "Cannot divide by zero."}
    return {"result": a / b}

# Convert to MCP
mcp = FastApiMCP(app, name="Calculator MCP API")
mcp.mount_http()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8002)