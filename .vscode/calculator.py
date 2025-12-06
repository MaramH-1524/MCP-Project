from mcp.server import Server
from mcp.types import Tool, ToolResult

server = server("calculator")


# -------------------- ADD --------------------
@server.register_tool(
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
def add(a: float, b: float) -> ToolResult:
    return ToolResult(output=a + b)


# -------------------- SUBTRACT --------------------
@server.register_tool(
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
def subtract(a: float, b: float) -> ToolResult:
    return ToolResult(output=a - b)


# -------------------- MULTIPLY --------------------
@server.register_tool(
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
def multiply(a: float, b: float) -> ToolResult:
    return ToolResult(output=a * b)


# -------------------- DIVIDE --------------------
@server.register_tool(
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
def divide(a: float, b: float) -> ToolResult:
    if b == 0:
        return ToolResult(error="Division par zéro impossible")
    return ToolResult(output=a / b)


# -------------------- RUN SERVER --------------------
if __name__ == "__main__":
    server.run_stdio()
