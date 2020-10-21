# In context learning

## Starting point

These instructions assume you are already in an interactive bash session in the docker container.
This is the end point of the instructions found in [DOCKER.md](./DOCKER.md).

## Let's make a haiku bot

## First let's download some training data

In haikus, the structure and style are an important component to the end result. Therefore the training data has to be structured in a way where there is a delimitation between each haiku.

We do this by putting `<|endoftext|>` in between each haiku in our training text file. This tells the model that each chink  of text in between this delimiter is a separate document.

The example file we are downloading has already been formatted to include the delimiters.

```
wget -o data/haiku.txt https://raw.githubusercontent.com/brianweet/gpt-2-haiku/master/train/run1/dataset/herval-creative-machines.txt
```

## Next we encode the training data into a format which the model can used

```
python3 encode.py data/haiku.txt data/haiku.npz
```

## Finally we can start training

```
python3 train.py --dataset data/haiku.npz --model_name haiku
```

To differentiate between model runs we train we add `--model_name name` to the command.
There are many other parameters which can be changed and tuned while training the model. You can find out more within

```
python3 train.py --help
```

You can stop the training at any time by using `CTRL+C`
The model will automatically save every 1000 steps, and at the last step before training stops.
