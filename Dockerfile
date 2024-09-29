FROM python:3.10-slim
WORKDIR /app

RUN apt-get update \
  && apt-get -y install gcc postgresql \
  && apt-get clean

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install 'uvicorn[standard]'

COPY . .

EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["python", "manage.py", "runserver_plus", "--print-sql", "0.0.0.0:8000"]
#CMD ["python", "-m", "gunicorn", "Moppetto.asgi:application", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker"]
