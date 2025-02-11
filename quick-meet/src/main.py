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

import logging
import os
import requests
import sys
import torch

from IPython.display import display, Markdown, update_display
from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer, BitsAndBytesConfig

from utils.login import hf_login, openai_login


# ---------------------------------------------------------------------------- #
#                            MAIN STREAMLINE FUCNTION                          #
# ---------------------------------------------------------------------------- #

def main_streamline(
    hf_token, 
    openai_api_key
):
    """
    main_streamline -- Streamline the end-to-end process of the Quick-Meet 
    project
    """
    # Login to Hugging Face & OpenAI
    hf_login(token=hf_token)
    openai_client = openai_login(api_key=openai_api_key)


def main():
    """
    main -- Main execution for the QuickMeet project
    """
    hf_token_var = "HF_TOKEN"
    openai_api_key_var = "OPENAI_API_KEY"
    hf_token = os.environ.get(hf_token_var)
    openai_api_key = os.environ.get(openai_api_key_var)
    # QuickMeet Streamline
    main_streamline(
        hf_token=hf_token, 
        openai_api_key=openai_api_key
    )


# ---------------------------------------------------------------------------- #
#                                 MAIN EXECUTION                               #
# ---------------------------------------------------------------------------- #

if __name__ == "__main__":
    main()