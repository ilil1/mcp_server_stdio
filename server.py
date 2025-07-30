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
    print("Starting MCP server...", file=sys.stderr)  # stderr로 변경

    # PORT 환경 변수 사용: Smithery 호환
    port = int(os.environ.get('PORT', 8000))  # 컨테이너에서 PORT 읽음, 로컬 시 8000 fallback

    # uvicorn.run에 타임아웃 설정 추가 (기본 30초, 필요 시 조정)
    uvicorn.run(mcp.streamable_http_app(), host="0.0.0.0", port=port, log_level="info", timeout_keep_alive=60)

    print("Server stopped", file=sys.stderr)  # stderr로 변경

    # if __name__ == "__main__":
    #     print("Starting MCP server...", file=sys.stderr)
    #
    #     # Streamable HTTP 모드로 변경
    #     port = int(os.environ.get("PORT", 8000))  # Smithery PORT 사용
    #     mcp.run(transport="streamable-http", host="0.0.0.0", port=port)  # host/port 추가 (path는 내부 기본 /mcp)
    #
    #     print("Server stopped", file=sys.stderr)