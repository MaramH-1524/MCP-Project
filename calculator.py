from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="calculator"
)
#on doit faire des documentations / on l'a deja fait ici 
@mcp.tool()
def add(a: float, b: float):
    """Additionne deux nombres."""
    return a + b

@mcp.tool()
def subtract(a: float, b: float):
    """Soustrait b de a."""
    return a - b

@mcp.tool()
def multiply(a: float, b: float):
    """Multiplie deux nombres."""
    return a * b

@mcp.tool()
def divide(a: float, b: float):
    """Divise a par b."""
    if b == 0:
        raise ValueError("Division par zéro impossible.")
    return a / b


if __name__ == "__main__":
    mcp.run(transport="stdio")
