FROM python:3.4-alpine

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt

CMD ["python3", "run.py", "db init", "db migrate"]
#CMD ["python3", "run.py", "db", "init" ]
#CMD ["python3", "run.py", "db", "migrate" ]
#CMD ["python3", "run.py", "db", "migrate"]
#CMD ["python 3 db init" ]
#CMD ["python3", "run.py", "db", "init"]
#CMD ["python3", "run.py", "db", "migrate"]