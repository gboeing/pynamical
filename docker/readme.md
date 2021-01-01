# Pynamical Docker Image

## Usage

The Pynamical Docker image and container usage instructions are available on [Docker Hub](https://hub.docker.com/r/gboeing/pynamical).

## Development

### Build image from Dockerfile

Run `docker-build.sh` in this directory. This script stops/deletes all containers/images on the system, builds the   image, then exports its conda environment to a yml file in the mounted working directory.

### Push image to hub for public use

```
docker login
docker tag gboeing/pynamical gboeing/pynamical:v0.0.0
docker push -a gboeing/pynamical
```
