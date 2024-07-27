FROM python:3.10-alpine

RUN pip install --upgrade pip

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH="/app/src"

EXPOSE 8080

CMD ["sh", "-c", "python db_script.py && python entry.py"]
