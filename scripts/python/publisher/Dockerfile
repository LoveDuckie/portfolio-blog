FROM python:3.10.8-slim AS publisher-base

ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir -p /publisher
COPY . /publisher
RUN chmod -R ug+rwx /publisher

FROM publisher-base as publisher-system

RUN apt -yqq update && apt -yqq upgrade && apt -yqq install ssh build-essential gcc sudo && apt -yqq autoremove

FROM publisher-system as publisher-poetry

RUN python -m pip install pip --upgrade
RUN /publisher/scripts/setup-tooling-poetry.sh
RUN /bin/bash -c ". ~/.profile && cd /publisher && poetry install && pip install -e ."
WORKDIR /publisher

# ENTRYPOINT [ "/bin/bash", "-c", "publisher" ]
ENTRYPOINT [ "publisher" ]
