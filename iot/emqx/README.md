# EMQX MQTT broker

## Environment:
* EMQX 5.7.2

## Port mappings
| Ports | Usages          |
| ----- | --------------- |
| 1883  | MQTT (tcp)      |
| 8883  | MQTT (ssl)      |
| 8083  | WebSocket (ws)  |
| 8084  | WebSocket (wss) |
| 18083 | EMQX Dashboard  |

## Usage
```bash
docker compose up -d
```
