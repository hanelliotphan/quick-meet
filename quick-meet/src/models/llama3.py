# ---------------------------------------------------------------------------- #
# Author: Han-Elliot Phan                                                      #
# Email: hanelliotphan@gmail.com                                               #
#                                                                              #
# Last update: February 11, 2025                                               #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# llama3.py                                                                    #
#                                                                              #
# This file is for setting up the Llama-3.1 model in order to generate summary,# 
# keypoints, takeaways and list of action items from audio transcripts.        #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#                               IMPORT LIBRARIES                               #
# ---------------------------------------------------------------------------- #

import logging
import sys
import torch

from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer, BitsAndBytesConfig


# ---------------------------------------------------------------------------- #
#                       LLAMA 3.1 MODEL SETUP FUNCTIONS                        #
# ---------------------------------------------------------------------------- #

def configure_quantization():
    """
    configure_quantization -- Set up quantization for the Llama 3.1 model
    """
    try:
        quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16
        )
        return quant_config
    except Exception as e:
        logging.critical(msg=f"[llama3.py] configure_quantization: Cannot configure quantization. Error message: {e}")
        sys.exit(-1)


def generate_outputs(audio_filepath, model_type, prompt, quant_config):
    try:
        logging.info(msg=f"[llama3.py] generate_outputs: Generating summary, keynotes and list of action items from audio '{audio_filepath}'...")
        llama3_tokenizer = AutoTokenizer.from_pretrained(model_type)
        llama3_tokenizer.pad_token = llama3_tokenizer.eos_token
        model = AutoModelForCausalLM.from_pretrained(
            model_type,
            device_map="auto",
            trust_remote_code=True,
            quantization_config=quant_config
        )
        inputs = llama3_tokenizer.apply_chat_template(prompt, return_tensors="pt", tokenize=False).to(model.device)
        streamer = TextStreamer(llama3_tokenizer)
        outputs = model.generate(inputs, streamer=streamer, max_new_tokens=2000)
        logging.info(msg=f"[llama3.py] generate_outputs: Successfully generated summary, keynotes and list of action items from audio '{audio_filepath}'...")
        return llama3_tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception as e:
        logging.error(msg=f"[llama3.py] generate_outputs: Cannot generate summary, keynotes and list of action items from audio '{audio_filepath}'. Error message: {e}")
        sys.exit(1)