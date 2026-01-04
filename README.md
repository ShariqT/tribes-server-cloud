# Tribes Python server

## Intro
This is a reference implementation of the Tribes protocol. This server also has a web dashboard where server admins can add, block or message people who are members of the server. You can read more about the Tribes protocol and how it works at [www.tribes.ltd](https://www.tribes.ltd)

## Prerequistes
The database used for this reference implementation is the Redisstack. This is the version of Redis that has the JSON extensions installed and running. You can use the Docker image RedisStack[(https://hub.docker.com/r/redis/redis-stack-server)] as starting point.

For deploying a server, you can get a managed instance of Redisstack at [Redis.io](https://www.redis.io).

## Docker Image
You can find the [Docker image](https://hub.docker.com/r/shariqtorres/tribes-python-cloud) in DockerHub. This Docker image has several environment variables that must be set before 
running a container. These can be found in the `.env.example` file for this repo.

If you are running a container for the first time, you will need the admin setup password. 
You can get this password by running `uv run ./server.py --show-admin-pw`. You will then see
the password in the docker logs for the container. 

## Deploying
You can read about how to [deploy this image on Railway at the Tribes docs website](https://docs.tribes.ltd/guides/launch-on-railway/).

## Tribes Network Client
You will need to get the Tribes client to be able to visit your newly launched server. Go to [www.tribes.ltd](https://www.tribes.ltd) to get the client. 


