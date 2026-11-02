# Containerized API Security Test Lab

Flask REST API behind an NGINX reverse proxy. Testings of HTTP responses, key authentication, private network, & persistent logs.

## Getting Started
1. Have Docker and Docker Compose ready
2. Add your API Key in a .env file
3. `docker compose up -d --build`
4. Use curl, Postman, or other tools to test the API

## Exposed Port
The NGINX proxy is exposed on port 8080. The API container (port 5000) is reachable inside the `test_network`.

## API Key
Copy the .env.example file to a local .env file and add an API (dummy) key. This ensures key is safely used and secured. If using curl in terminal, run  `export $(cat .env)` before testing. 

## Endpoints
- `GET /health` (no key)
- `GET /assets` (key required)
- `GET /assets/<id>` (key required)

## Generate Log Summary
```bash
docker compose cp api:/logs/requests.log .
python3 log.py
