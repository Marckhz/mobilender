FROM python:3.9-buster

RUN mkdir /myapp

WORKDIR /myapp

COPY run.sh /myapp
COPY ./ /myapp/
COPY ./api/fixtures/address.json /myapp/fixtures/
COPY ./api/fixtures/articles.json /myapp/fixtures/
COPY ./api/fixtures/ranks.json /myapp/fixtures/
COPY ./api/fixtures/sites.json /myapp/fixtures/
COPY ./api/fixtures/users.json /myapp/fixtures/

RUN chown -R 1001:0 /myapp && \
    chmod +x /myapp/run.sh
RUN apt-get update -y
RUN apt-get install -y 
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip check
RUN ls /myapp/api/fixtures/

USER 1001
EXPOSE 8666

CMD ["./run.sh"]