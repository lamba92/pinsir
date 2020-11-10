FROM adoptopenjdk:8u262-b10-jdk-hotspot-bionic

COPY . /app

EXPOSE 50051

ARG APP_NAME
ENV PATH="$PATH:/app/bin"
ENV RUN_COMMAND=$APP_NAME

CMD $RUN_COMMAND
