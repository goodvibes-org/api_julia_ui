
FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .  
RUN pip3 install -r requirements.txt
COPY .  .
EXPOSE 9977
# ENTRYPOINT ["flask", "run", "--port=6565"]
# CMD [ "python", "app.py" ]
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=9977", "--server.address=0.0.0.0"]