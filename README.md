# Intro

This repository was created as a combination of the great original work by [OpenAI](https://github.com/openai/gpt-2) and the follow up work by [N. Shepperd](https://github.com/nshepperd/gpt-2).
**N. Sheppard** added the code needed to do *In context learning* to adapt the general GPT-2 models for specific use cases. However his code was based off an older version of GPT-2 and therefore had to be very slightly updated. Moreover, the **OpenAI** GPT-2 repo has been archived as of December 2019, but since then their `Dockerfile` has stopped working. This has also been addressed in this repository.

For more information on GPT-2, please consult the original repositories and the paper ["Language Models are Unsupervised Multitask Learners"](https://d4mucfpksywv.cloudfront.net/better-language-models/language-models.pdf).

Finally, the original contributors can be found here [CONTRIBUTORS.md](./CONTRIBUTORS.md).

# Usage

All the following instructions assume you have cloned this repository and have opened its directory in the command prompt.
This can be done with the following command provided you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed in your system.

```
git clone https://github.com/robmoratore/gpt-2.git && cd gpt-2
```

## Docker

A `Dockerfile` is provided to build a cpu container. More information and usage instructions can be found here [DOCKER.md](./DOCKER.md).

If you do not wish to user Docker, then the original GPT-2 repo has instructions on how to do a native installation. This is not recommended as it is reliant on outdated versions of python packages. If however you still wish to do so, please refer to the original documentation [here](https://github.com/openai/gpt-2/blob/master/DEVELOPERS.md).

## Sample generation

Samples can be generated either conditionally or unconditionally. Conditional sample generation is an interactive mode where users are prompted for a initial text input which the model uses to generate the remaining text. With unconditional sample generation, the model outputs text without any prompting.

OpenAI has provided GPT-2 models of four different sizes (number of parameters) and any of those can be used for sample generation. The largest size model might not run locally depending on you machine though. Furthermore, you can also use the same code to generate samples with any custom models you create with **In context learning**.

Detailed instructions on sample generation can be found here [SAMPLEGENERATION.md](./SAMPLEGENERATION.md).

## In context learning

You can improve model results for a specific task with in context learning and a training dataset for that specific task.

Detailed instructions on in context learning can be found here [INCONTEXTLEARNING.md](./INCONTEXTLEARNING.md).

## License

[MIT](./LICENSE)
