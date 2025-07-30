# Python 3.13.5 기반 이미지 사용
FROM python:3.13.5-slim

# 작업 디렉토리 설정
WORKDIR /app

# 프로젝트 파일 복사
COPY server.py .
COPY pyproject.toml .
COPY uv.lock .

# uv 설치
RUN pip install uv

# 의존성 설치
RUN uv sync --all-extras

# 서버 실행
CMD ["uv", "run", "python3", "server.py"]