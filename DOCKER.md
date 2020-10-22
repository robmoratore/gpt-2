# Installation

All the instructions in this repository are meant to be run in a docker container based on the provided dockerfile. However, you can also install all the required libraries natively instead.

If you do not wish to user Docker, then the original GPT-2 repo has instructions on how to do a native installation. This is not recommended as it is reliant on outdated versions of python packages. If however you still wish to do so, please refer to the original documentation [here](https://github.com/openai/gpt-2/blob/master/DEVELOPERS.md).


## Docker

If you do not currently have Docker installed in you system, you can find instructions to do so [here](https://docs.docker.com/get-docker/)

## Docker Image

Make sure you are currently in the GPT-2 repository directory.

Build the Dockerfile and tag the created image as `gpt2`:

```
docker build -t gpt2 .
```

## Docker Container

We will run interactive ephemeral docker containers which "self-destruct" upon stoping it. In order for our progress to not be lost when we exit the container, we will mount the `gpt-2` local directory in the container so that our changes are saved to the local computer and not lost.

*__Note:__ The commands below will mount your current working directory into the container, therefore it is important you run it from the cloned `gpt-2` repository directory.*

To run the container and enter an interactive bash session, run the following command:

```
docker run -it --rm -v "$PWD":/repo gpt2 bash
```

Now we are inside the container. The last step is to go into the `/repo` directory to access the shared volume in the local machine:

```
cd repo
```

This point is the starting point for [sample generation](./SAMPLEGENERATION.md) and [in context learning](./INCONTEXTLEARNING.md)
