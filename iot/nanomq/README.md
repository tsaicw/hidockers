# NanoMQ MQTT broker

## Environment:
* NanoMQ 0.22.8

## Port mappings
| Ports | Usages          |
| ----- | --------------- |
| 1883  | MQTT (tcp)      |
| 8883  | MQTT (ssl)      |
| 8083  | WebSocket (ws)  |
| 8084  | WebSocket (wss) |
| 8081  | HTTP server     |

## Usage
```bash
docker compose up -d
```
