# RouteRelay

Forward received requests to remote services and relay back their responses.

## Usage

Update the provided sample `config.example.json` and rename it to `config.json`.

Then start the Docker container:
```shell
docker run --rm -p 8080:8080 -v /path/to/config.json:/app/config.json laxsrbija/route-relay:latest
```

Alternatively, use the provided Docker Compose configuration:
```shell
docker compose up
```