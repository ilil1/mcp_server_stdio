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

    try:
        port = int(os.environ.get('PORT', 8000))
        print(f"Using port: {port}", file=sys.stderr)  # 포트 로그 추가

        # FastMCP 앱 가져오기 전에 로그
        print("Initializing streamable_http_app...", file=sys.stderr)
        app = mcp.streamable_http_app()  # 앱 초기화 로그
        print("streamable_http_app initialized successfully", file=sys.stderr)

        # uvicorn 실행
        uvicorn.run(app, host="0.0.0.0", port=port, log_level="info", timeout_keep_alive=60)

    except Exception as e:
        print(f"Server error: {str(e)}", file=sys.stderr)  # 예외 캡처
        raise

    print("Server stopped", file=sys.stderr)

    # if __name__ == "__main__":
    #     print("Starting MCP server...", file=sys.stderr)
    #
    #     # Streamable HTTP 모드로 변경
    #     port = int(os.environ.get("PORT", 8000))  # Smithery PORT 사용
    #     mcp.run(transport="streamable-http", host="0.0.0.0", port=port)  # host/port 추가 (path는 내부 기본 /mcp)
    #
    #     print("Server stopped", file=sys.stderr)