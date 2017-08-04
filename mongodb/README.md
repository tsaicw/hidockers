## MongoDB Docker

Environment:

- Debian Jessie-slim
- MongoDB 3.5

Usage:
```
$ docker run -d -rm -p 27017:27017 -v $PWD/data:/data --name mongo mongo
```

