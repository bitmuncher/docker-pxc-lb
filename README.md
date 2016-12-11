# docker-pxc-lb
Files to create Docker image for a Percona Cluster Load Balancer

You can get the image from Docker Hub with:

```
docker pull bitmuncher/pxc-lb
```

To run this image define environment variable SERVERS on container startup with a comma-separated list of IPs for all servers. Example:

```
docker run -d \
  --name pxc-lb \
  -e 'SERVERS=10.10.0.1,10.10.0.2,10.10.0.3' \
  bitmuncher/pxc-lb
```