# MongoDB Docker

## Environment:
  * Debian Jessie-slim
  * MongoDB 3.4

## Usage:
```console
docker container run -d --rm -p 27017:27017 -v $PWD/mongo:/data --name mongodb galoistsai/mongodb
```

