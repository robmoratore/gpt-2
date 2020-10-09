# Installation

Git clone this repository, and `cd` into directory for remaining commands
```
git clone https://github.com/robmoratore/gpt-2.git && cd gpt-2
```

Then, follow instructions for the Docker installation.

## Docker Image

Build the Dockerfile and tag the created image as `gpt2`:
```
docker build -t gpt2 .
```

## Docker Container

You can either run interactive ephemeral containers which "self-destruct" upon stoping or a container which does not self delete itself after it stops, which you can keep reusing.
Either option works well, as we will be mounting the `gpt-2` local directory in the container so all no files will be stored in the container.
You also have the choice of running everything from the terminal or from a Jupyter notebook.

*__Note:__ The commands below will mount your current working directory into the container, therefore it is important you run it from the cloned `gpt-2` repository directory.*

### Ephemeral Container

#### Jupyter
```
docker run -it -v "$PWD":/tf/notebooks gpt2
```

#### Interactive bash session
```
docker run -it -v "$PWD":/tf/notebooks gpt2 bash
```
### Permanent Container

For a permanent container it makes sense to manage it by giving it a specific name and also specifying the port you use to connect to Jupyter in the browser. This way you avoid port conflicts between docker containers and you can easily remember what they do by their name.

Here we are creating a container called `gpt2` (I know, very imaginative), with the external port 20000 (this can be an arbitrary number as long as it is an available port)

```
docker run --name gpt2 -p 20000:8888 -v "$PWD":/tf/notebooks gpt2
```

When you first run the container, you will be put into a bash session within the container which will contain the information on how to  connect to Jupyter in your browser.
To do so navigate to:

```
http://localhost:(the port specified above)/?token=(your token)
```

# Running

## Jupyter

Navigate to the `/notebooks` folder and start  with:  
`GPT-2_Intro.ipynb`

## Bash

###  Download the model data

```
python3 download_model.py 124M
python3 download_model.py 355M
python3 download_model.py 774M
python3 download_model.py 1558M
```

### Unconditional sample generation

To generate unconditional samples from the small model:
```
python3 src/generate_unconditional_samples.py | tee /tmp/samples
```
There are various flags for controlling the samples:
```
python3 src/generate_unconditional_samples.py --top_k 40 --temperature 0.7 | tee /tmp/samples
```

To check flag descriptions, use:
```
python3 src/generate_unconditional_samples.py -- --help
```

### Conditional sample generation

To give the model custom prompts, you can use:
```
python3 src/interactive_conditional_samples.py --top_k 40
```

To check flag descriptions, use:
```
python3 src/interactive_conditional_samples.py -- --help
```

### Fine tune model for specific task

#### Let's make a haiku bot

#### First let's download some training data

In haikus, the structure and style are an important component to the end result. Therefore the training data has to be structured in a way where there is a delimitation between each haiku.

We do this by putting `<|endoftext|>` in between each haiku in our training text file. This tells the model that each chink  of text in between this delimiter is a separate document.

The example file we are downloading has already been formatted to include the delimiters.

```
wget -o data/haiku.txt https://raw.githubusercontent.com/brianweet/gpt-2-haiku/master/train/run1/dataset/herval-creative-machines.txt
```

#### Next we encode the training data into a format which the model can used

```
python3 encode.py data/haiku.txt data/haiku.npz
```

#### Finally we can start training

```
python3 train.py --dataset data/haiku.npz --model_name haiku
```

To differentiate between models we train we add `--model_name name` to the command.
There are many other parameters which can be changed and tuned while training the model. You can find out more within

```
python3 train.py --help
```

You can stop the training at any time by using `CTRL+C`
The model will automatically save every 1000 steps, and at the last step before training stops.
