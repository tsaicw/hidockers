#!/bin/bash
set -e

if [ "$1" = 'dynamo' ]; then
  echo "=== TODO ==="
fi

# Start DynamoDB.
exec java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -inMemory -sharedDb -port $DYNAMODB_PORT

exit $?

