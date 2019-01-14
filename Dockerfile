FROM python:3.6-alpine
COPY ./Hello* /
CMD ["python", "/HelloWorldTest.py"]
