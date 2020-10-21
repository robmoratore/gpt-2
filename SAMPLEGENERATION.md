# Sample generation

## Starting point

These instructions assume you are already in an interactive bash session in the docker container.
This is the end point of the instructions found in [DOCKER.md](./DOCKER.md).

##  Download the model data

First we need to download the models before being able to use them.
By default all the codes below will use the `124M` model, unless otherwise specified. The larger models might not run locally in your machine.

```
python3 download_model.py 124M
python3 download_model.py 355M
python3 download_model.py 774M
python3 download_model.py 1558M
```

## Conditional sample generation

To give the model custom prompts, you can use:
```
python3 src/interactive_conditional_samples.py
```

There are various flags for controlling the samples, which can be found with the help command:
```
python3 src/interactive_conditional_samples.py -- --help
```

## Unconditional sample generation

To generate unconditional samples from the small model:
```
python3 src/generate_unconditional_samples.py
```

There are various flags for controlling the samples, which can be found with the help command:
```
python3 src/generate_unconditional_samples.py -- --help
```



You can go back to the intro ReadMe [here](./README.md)
