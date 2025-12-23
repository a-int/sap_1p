FROM python:3.12-slim
WORKDIR /
COPY main.py /main.py
ENTRYPOINT ["python", "/main.py"]
