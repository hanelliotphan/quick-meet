# ---------------------------------------------------------------------------- #
# Author: Han-Elliot Phan                                                      #
# Email: hanelliotphan@gmail.com                                               #
#                                                                              #
# Last update: February 10, 2025                                               #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# main.py                                                                      #
#                                                                              #
# This file is for the main execution of the QuickMeet project.                #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#                               IMPORT LIBRARIES                               #
# ---------------------------------------------------------------------------- #

import argparse
import logging
import os
import requests
import sys
import torch

from IPython.display import display, Markdown, update_display
from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer, BitsAndBytesConfig

from utils.login import hf_login, openai_login
from utils.file_processor import process_audio_file


# ---------------------------------------------------------------------------- #
#                            MAIN STREAMLINE FUCNTION                          #
# ---------------------------------------------------------------------------- #

def main_streamline(
    hf_token, 
    openai_api_key,
    audio_filepath,
    audio_model
):
    """
    main_streamline -- Streamline the end-to-end process of the Quick-Meet 
    project
    """
    # Login to Hugging Face & OpenAI
    hf_login(token=hf_token)
    openai_client = openai_login(api_key=openai_api_key)
    
    # Generate transcript from audio file
    transcript = process_audio_file(
        audio_filepath=audio_filepath,
        audio_model=audio_model
    )


def main():
    """
    main -- Main execution for the QuickMeet project
    """
    # Get arguments from script command execution
    parser = argparse.ArgumentParser()
    parser.add_argument("--audio_filepath", "-f", help="[Required] Path to the audio file.")
    args = parser.parse_args()
   
    # Initialize required variables
    hf_token_var = "HF_TOKEN"
    openai_api_key_var = "OPENAI_API_KEY"
    hf_token = os.environ.get(hf_token_var)
    openai_api_key = os.environ.get(openai_api_key_var)
    audio_filepath = args.audio_filepath
    audio_model = "whisper-1"
   
    # QuickMeet Streamline
    main_streamline(
        hf_token=hf_token, 
        openai_api_key=openai_api_key,
        audio_filepath=audio_filepath,
        audio_model=audio_model
    )


# ---------------------------------------------------------------------------- #
#                                 MAIN EXECUTION                               #
# ---------------------------------------------------------------------------- #

if __name__ == "__main__":
    main()