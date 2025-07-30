import os
import sys

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

if __name__ == "__main__":
    print("Starting MCP server...", file=sys.stderr)

    # HTTP 모드로 변경: Smithery 배포 호환
    port = int(os.environ.get("PORT", 8000))  # Smithery가 PORT 할당
    mcp.run(transport="streamable-http", host="0.0.0.0", port=port, path="/mcp")

    print("Server stopped", file=sys.stderr)

    # if __name__ == "__main__":
    #     print("Starting MCP server...")
    #     uvicorn.run(mcp.sse_app(), host="0.0.0.0", port=8000, log_level="info")