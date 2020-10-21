# In context learning

## Starting point

These instructions assume you are already in an interactive bash session in the docker container.
This is the end point of the instructions found in [DOCKER.md](./DOCKER.md).

## Let's make a haiku bot

### A word on training data

In haikus, the structure and style are an important component to the end result. Therefore the training data has to be structured in a way where there is a delimitation between each haiku.

We do this by putting `<|endoftext|>` in between each haiku in our training text file. This tells the model that each chunk of text in between this delimiter is a separate document.

The example file included in `/data` has already been formatted to include the delimiters.

### Next we encode the training data into a format which the model can use

```
python3 encode.py data/haiku.txt data/haiku.npz
```

### Finally we can start training

```
python3 train.py --dataset data/haiku.npz --model_name haiku
```

To differentiate between model runs we train we add `--model_name name` to the command.
There are many other parameters which can be changed and tuned while training the model. You can find out more within

```
python3 train.py --help
```

For example, if you would like to see more samples, you can modify it accordingly (default is once every 100 steps). For example, to output 3 samples every 50 steps, type the following command instead:

```
python train.py --dataset data/haiku.npz --model_name haiku --sample_every 50 --sample_num 3
```

You can stop the training at any time by using `CTRL+C`
The model will automatically save every 1000 steps, and at the last step before training stops.

### Using our model to generate Text

Create a folder for the model

In the src/models folder, you should have just one folder called 117M. Create another folder to store your model alongside with the original model. I made a new folder called lyric. Now, I have two folders in src/models, one is called 117M and the other is called lyric.

Go to src/checkpoint/run1 folder, and copy the following files:

checkpoint
model-xxx.data-00000-of-00001
model-xxx.index
model-xxx.meta

xxx refers to the step number. Since I have trained for 501 steps, I have model-501.index.

Paste them into the newly created folder (in my case, the folder is called lyric). Next, go to the 124M folder and copy the following files:

encoder.json
hparams.json
vocab.bpe

Paste them into the lyric folder. Double check that you should have 7 files in it.

With this, we are ready to generate samples. There are two ways to generate samples.
