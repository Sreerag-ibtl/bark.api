# bark.api

Implement [Bark](https://github.com/suno-ai/bark) as a REST API.

## Usage

### Running with docker-compose
```bash
docker build -t myimage . -f Dockerfile
```
```
docker run -d --name mycontainer -p 80:80 myimage
```


## Testing

```bash
docker build -f Dockerfile.pytest .
```
```bash
docker run <image>
```
