FROM python:3.12-slim

WORKDIR /code

# Install procps (for pkill), and update pip
RUN apt-get update && pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_ENV=development
ENV FLASK_APP=app

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--reload"]
