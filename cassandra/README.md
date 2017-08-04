## Cassandra Docker

Environment:

- Debian Jessie-backports
- Cassandra 2.2

Usage:
```
$ docker run -d --rm -p 9042:9042 -v $PWD/cassandra:/var/lib/cassandra --name cassandra cassandra
```

