FROM continuumio/anaconda:4.4.0
COPY ./FlaskModels /usr/local/python/
EXPOSE 5000
WORKDIR /usr/local/python
RUN pip install -r requirements.txt
CMD python plask_predict_api.py