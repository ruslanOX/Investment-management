FROM alpine:latest as runtime
ENTRYPOINT ["tail", "-f", "/dev/null"]