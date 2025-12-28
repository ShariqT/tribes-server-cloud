FROM python:3.11.6
RUN pip install uv
RUN mkdir /app
WORKDIR /app
COPY . .
RUN uv sync
ENV PORT=8000
VOLUME ["/var/keys/"]
CMD ["uv", "run", "server.py", "--run-server"]