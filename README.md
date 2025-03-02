# QuickMeet - Create a List of Action Items from Meeting Audios

```bash
Author: Han-Elliot Phan
Email: hanelliotphan@gmail.com

Last Update: March 1, 2025
```

## Brief Discussion
This project is to create summary, keynotes, takeaways and list of action items 
from meeting audios using Python, Meta's Llama-3 and OpenAI's Whisper-1 models.

## Architecture
This project uses the OpenAI's Whisper-1 model for audio-to-text transcription, 
and Meta's LLama-3 model for quantization for the process of generating list of 
action items.

For more information about the model, please read the following documentation
- [OpenAI's Whisper-1](https://platform.openai.com/docs/guides/speech-to-text)
- [Meta's Llama-3](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)

## Instructions of Use

First, this project requires GPU instances to run. If you are using a Macbook, 
please ensure that you are having eGPUs (through Thunderbolt) installed, or use 
an online platform that has GPUs installed, i.e. Google Colab.

Second, the API keys for Hugging Face and OpenAI are required. Please ensure that 
you have created an account for both of these products, and generate an API 
token from your account settings.

After having the two required API tokens, please run the following command:
```bash
$ export OPENAI_API_KEY=<you OpenAI API key>
$ export HF_TOKEN=<your Hugging Face API token>
```

Third, since this project utilizes the Meta's Llama-3.1 model from Hugging Face, 
you need to be added to all the Meta's Llama repositories. Please go to 
[this repository](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) and 
on top of the page, fill in the information and wait for approval (in my case, 
it took 20 minutes, but it could be shorter or longer).

Next, install required packages via `pip` command
```bash
$ pip install -r requirements.txt
```

Then, run the `main.py` script to execute the software
```bash
$ python ./quick-meet/src/main.py -f <your audio filepath>
```

where
- `-f / --audio_filepath` (required): The filepath of the audio to analyze and generate the list of action items.

Note: The audio file must not exceed 25MB per the size limit for OpenAI's Whisper model.

You will find the `transcript.md` file with all the summary, keynotes, takeaways and list of action items located 
in the `./files` directory.

## Dedication
I dedicate this hard-work commitment to myself, my mother, my best friend Ha-Phuong and those that have imprinted 
in my heart. I hope that I have made you all truly proud of me.

## References
- [OpenAI's Whisper-1 Model](https://platform.openai.com/docs/guides/speech-to-text)
- [Meta's Llama-3 Model](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)
