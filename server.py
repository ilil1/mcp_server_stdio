import os

import uvicorn
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp_project")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def validate_test_sc() -> str:
    return "성공"

# if __name__ == "__main__":
#     try:
#         port = int(os.environ.get('PORT', 8000))
#         app = mcp.streamable_http_app()
#         uvicorn.run(app, host="0.0.0.0", port=port, log_level="info", timeout_keep_alive=60)
#     except Exception as e:
#         raise

if __name__ == "__main__":
    import sys
    print("Starting MCP server...", file=sys.stderr)
    mcp.run("stdio")
    print("Server stopped", file=sys.stderr)