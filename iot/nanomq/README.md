# NanoMQ MQTT broker

## Environment:
* NanoMQ 0.22.9

## Port mappings
| Ports | Usages          |
| ----- | --------------- |
| 1883  | MQTT (TCP)      |
| 8883  | MQTT (TLS)      |
| 8083  | WebSocket (WS)  |
| 8084  | WebSocket (WSS) |
| 8081  | HTTP server     |

## Usage
```bash
docker compose up -d
```
