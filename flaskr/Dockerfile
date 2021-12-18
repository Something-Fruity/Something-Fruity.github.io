FROM python:3.8
EXPOSE 5000:5000
COPY . /flaskr
COPY requirements /flaskr
WORKDIR /flaskr
RUN pip install -r requirements
CMD [ "flask", "run", "--host=0.0.0.0" ]