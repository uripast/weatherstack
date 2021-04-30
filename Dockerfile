FROM python:3.8

COPY . /weatherstack
WORKDIR /weatherstack
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["venv/weather.py"]
