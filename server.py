import uvicorn
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp_project")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# if __name__ == "__main__":
#     print("Starting MCP server...")
#     uvicorn.run(mcp.sse_app(), host="0.0.0.0", port=8000, log_level="info")

if __name__ == "__main__":
    import sys
    print("Starting MCP server...", file=sys.stderr)
    mcp.run()
    print("Server stopped", file=sys.stderr)