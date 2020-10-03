FROM python:3.7-slim

RUN adduser --disabled-password --gecos "" user1

WORKDIR /opt/api/

ARG FURY_USERNAME
ARG FURY_TOKEN
ARG API_MODEL_LSTM_VERSION

COPY requirements_docker.txt ./requirements_docker.txt
RUN pip install --upgrade pip
RUN pip install -r requirements_docker.txt

# This needs to be outside of requirements.txt to pass in secrets
RUN pip install model_lstm==${API_MODEL_LSTM_VERSION} \
    --index-url https://${FURY_TOKEN}@pypi.fury.io/${FURY_USERNAME}/ \
    --extra-index-url https://pypi.org/simple/

COPY ./ ./

RUN chmod +x ./run.sh
RUN chown -R user1:user1 ./

USER user1

EXPOSE 5000
ENTRYPOINT ["./run.sh"]