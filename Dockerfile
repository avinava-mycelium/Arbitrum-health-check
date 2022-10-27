FROM python:3.7
RUN pip3 install fastapi uvicorn typing pydantic http3
COPY ./app /app
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8547" ]