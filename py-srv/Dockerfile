FROM tiangolo/meinheld-gunicorn

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY bin/ /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app", "--reload"]
