FROM alpine:latest as runtime

#Personal access token are an alternative to using passwords 
#for authentication to GitHub when using the GitHub API or the command line. 
#Personal access tokens are intended to access GitHub resources on behalf of yourself.
RUN echo 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 > /app/key

ENTRYPOINT ["tail", "-f", "/dev/null"]
