from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp_project")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def validate_test_sc() -> str:
    return "성공"

if __name__ == "__main__":
    import sys
    print("Starting MCP server...", file=sys.stderr)
    mcp.run()
    print("Server stopped", file=sys.stderr)