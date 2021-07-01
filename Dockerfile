FROM python:3

WORKDIR /app
VOLUME /app/data 

COPY . . 
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "src/helloworld.py" ]
