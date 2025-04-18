#!/bin/bash
set -euo pipefail
echo "Run this script from the repository root."
docker login
docker buildx build --no-cache --pull --push --platform=linux/amd64,linux/arm64 -f ./Dockerfile -t gboeing/pynamical .
IMPORTED_VERSION=$(docker run --rm gboeing/pynamical:latest /bin/bash -c "ipython -c \"import pynamical; print(pynamical.__version__)\"")
echo "Imported $IMPORTED_VERSION"
