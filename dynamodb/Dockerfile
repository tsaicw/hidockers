FROM galoistsai/jdk:latest
MAINTAINER Daniel Tsai <galoistsai@gmail.com>

ENV DYNAMODB_HOME /opt/dynamodb
ENV DYNAMODB_PORT 8000

# Install the latest version of DynamoDB
RUN mkdir -p $DYNAMODB_HOME
WORKDIR $DYNAMODB_HOME
RUN curl -SL --silent http://dynamodb-local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest.tar.gz | tar zxfv -
COPY materials/start_dynamodb.sh $DYNAMODB_HOME

EXPOSE $DYNAMODB_PORT
ENTRYPOINT ["./start_dynamodb.sh"]

