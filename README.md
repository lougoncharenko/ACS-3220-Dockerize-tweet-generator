# docker-flask

<!-- omit in toc -->
## Table of Contents

1. [Build the Image](#build-the-image)
1. [Run the Container](#build-the-container)
1. [Access via Browser](#access-via-browsers)

## Command Reference

### 1. Build the Image

```bash
docker build -t docker-tweet-generator .
```

### 2. Run the Container

```bash
docker run -p 5001:3000 --rm --name tweet-generator-container docker-tweet-generator
```

### 3. Access via Browser

http://localhost:5001