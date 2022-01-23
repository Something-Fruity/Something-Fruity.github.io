FROM python:3.8
EXPOSE 5000:5000
COPY . /flaskr
WORKDIR /flaskr
RUN pip install -r ./flaskr/requirements.txt
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]
