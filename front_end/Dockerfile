FROM python:3.7-slim

RUN adduser --disabled-password --gecos "" user1

WORKDIR /opt/front_end/

COPY requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . ./

RUN chmod +x ./run.sh
RUN chown -R user1:user1 ./

USER user1

EXPOSE 5000
ENTRYPOINT ["./run.sh"]