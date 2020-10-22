# In context learning

## Starting point

These instructions assume you are already in an interactive bash session in the docker container.
This is the end point of the instructions found in [DOCKER.md](./DOCKER.md).

## Let's make a haiku bot

### Setting up the training dataset

In haikus, the structure and style are an important component to the end result. Therefore the training data has to be structured in a way where there is a delimitation between each haiku.

We do this by putting `<|endoftext|>` in between each haiku in our training text file. This tells the model that each chunk of text in between this delimiter is a separate document.

The example file included in `/data` has already been formatted to include the delimiters.

#### Data encoding

For the model to be able to use the data, it first needs to be encoded. This only needs to be done once for any dataset you use for training.

We can do that with the following command:

```
python3 encode.py data/haiku.txt data/haiku.npz
```

### Model training

We are now ready to train the model. The questions is, which model will we train?

By default, the `124M` model will be used as the basis, however you can specify a different model with the `--model_name model` parameter.
Bigger models will be a lot more resource intensive to train, so we suggest you first try with the smallest model. In general that model already produces quite good results.


We can start training with:
```
python3 train.py --dataset data/haiku.npz --run_name haiku
```

To differentiate between model runs we train we add `--run_name name` to the command.

There are many other parameters which can be changed and tuned while training the model. You can find out more with:

```
python3 train.py --help
```

For example, if you would like to see more samples, you can modify it accordingly (default is once every 100 steps). For example, to output 3 samples every 50 steps, type the following command instead:

```
python train.py --dataset data/haiku.npz --run_name haiku --sample_every 50 --sample_num 3
```

You can stop the training at any time by using `CTRL+C`

The model will automatically save every 1000 steps, and at the last step before training stops.

### Using our model to generate text

To use our trained model, we have to move it to the `models` directory alongside the default GPT-2 models.

Navigate to `models` directory and create a new directory with the model name of your choosing. In our case we will call is `haiku`

Next we have to copy our trained model to that new directory we created.
For that, go to the `checkpoint/haiku` directory, and copy the following files:

```
checkpoint
model-xxx.data-00000-of-00001
model-xxx.index
model-xxx.meta
```

xxx refers to the step number, and it will depend on the number of step you trained your model. If you trained for 500 steps, you will have model-500.index.

Paste them into the newly created directory `models/haiku`.

Next, we need some base files from the existing models. Go to the `models/124M` directory and copy the following files:

```
encoder.json
hparams.json
vocab.bpe
```

Paste them into `models/haiku`. If it all went well, you should have 7 files in it.

With this, we are ready to generate samples with our new model!

To do this you can follow the instructions in [SAMPLEGENERATION.md](./SAMPLEGENERATION.md) with one small change.
To use our new model for sample generation, you have to add the following parameter

```
--model_name haiku
```
