# ---------------------------------------------------------------------------- #
# Author: Han-Elliot Phan                                                      #
# Email: hanelliotphan@gmail.com                                               #
#                                                                              #
# Last update: February 11, 2025                                               #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# login.py                                                                     #
#                                                                              #
# This file is for setting up Hugging Face & OpenAI login using HF_TOKEN and   #
# OPENAI_API_KEY environment variables.                                        #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#                               IMPORT LIBRARIES                               #
# ---------------------------------------------------------------------------- #

import huggingface_hub
from openai import OpenAI


# ---------------------------------------------------------------------------- #
#                                LOGIN FUNCTIONS                               #
# ---------------------------------------------------------------------------- #

def hf_login(token):
    """
    hf_login -- Log in to Hugging Face interface using Hugging Face access token

    Documentation: https://huggingface.co/docs/huggingface_hub/en/package_reference/authentication#huggingface_hub.login
    """
    huggingface_hub.login(token=token)


def openai_login(api_key):
    """
    openai_login -- Log in to OpenAI interface using OpenAI API key

    Documentation: https://platform.openai.com/docs/quickstart
    """
    return OpenAI(api_key=api_key)