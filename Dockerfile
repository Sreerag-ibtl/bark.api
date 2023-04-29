FROM python:3.9

WORKDIR /code

ADD ./ /code/

RUN apt-get update -y

RUN python -m pip install -r requirements.txt

CMD ["uvicorn", "api.prediction:app", "--host", "0.0.0.0", "--port", "80"]
