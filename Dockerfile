FROM python:alpine
RUN pip install uv
RUN mkdir /app
WORKDIR /app
COPY . .
RUN uv sync
ENV PORT=8000
ENV REDIS_HOST=localhost
ENV REDIS_PORT=6380
ENV REDIS_DB=0
ENV REDIS_USERNAME=changeme
ENV REDIS_PASSWORD=changeme
ENV PUBLIC_ACCESS=1
ENV OTP_KEY=changeme
ENV APP_KEY=changeme
RUN uv run ./server.py --show-admin-pw
CMD ["uv", "run", "server.py", "--run-server"]