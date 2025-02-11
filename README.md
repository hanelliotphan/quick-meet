# QuickMeet - Create List of Action Items from Meeting Transcriptions

Last Update: February 11, 2025

```bash
Author: Han-Elliot Phan
Email: hanelliotphan@gmail.com

Last Update: February 11, 2025
```

## Brief Discussion
This project is to create list of action items based on the meeting transcriptions using Python and Llama-3 model. This notebook is used solely for research purpose. The source code of the project can be found [here](https://github.com/hanelliotphan/quick-meet).

## Architecture
This project uses the OpenAI's Whisper-1 model for audio-to-text transcription, and Meta's LLama-3 model for quantization for the process of generating list of action items.

For more information about the model, please read the following documentation
- [OpenAI's Whisper-1](https://platform.openai.com/docs/guides/speech-to-text)
- [Meta's Llama-3](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)

## Instructions of Use
Install required packages via `pip` command
```bash
$ pip install -r requirements.txt
```

Then, run the `main.py` script to execute the software
```bash
$ python ./quick-meet/src/main.py --f <audio_filepath>
```

where
- `--f / --audio-filepath` (required): The filepath of the audio to analyze and generate the list of action items.

## Dedication
I dedicate this hard-work commitment to myself, my mother, my best friend Ha-Phuong and those that have imprinted in my heart. I hope that I have made you all truly proud of me.