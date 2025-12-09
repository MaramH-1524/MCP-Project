from fastmcp import FastMCP
from mcp.types import Tool

mcp = FastMCP("calculator")

# -------------------- ADD --------------------
@mcp.register_tool(
    Tool(
        name="add",
        description="Additionne deux nombres",
        input_schema={
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"}
            },
            "required": ["a", "b"]
        }
    )
)
def add(a: float, b: float):
    return {"output": a + b}

# -------------------- SUBTRACT --------------------
@mcp.register_tool(
    Tool(
        name="subtract",
        description="Soustrait b de a",
        input_schema={
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"}
            },
            "required": ["a", "b"]
        }
    )
)
def subtract(a: float, b: float):
    return {"output": a - b}

# -------------------- MULTIPLY --------------------
@mcp.register_tool(
    Tool(
        name="multiply",
        description="Multiplie deux nombres",
        input_schema={
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"}
            },
            "required": ["a", "b"]
        }
    )
)
def multiply(a: float, b: float):
    return {"output": a * b}

# -------------------- DIVIDE --------------------
@mcp.register_tool(
    Tool(
        name="divide",
        description="Divise a par b",
        input_schema={
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"}
            },
            "required": ["a", "b"]
        }
    )
)
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Division par zéro impossible"}
    return {"output": a / b}

# -------------------- RUN SERVER --------------------
if __name__ == "__main__":
    mcp.run(transport="http")
