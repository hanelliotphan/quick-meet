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
import os

from utils.login import hf_login, openai_login
from utils.file_processor import process_audio_file, generate_output_file
from models.llama3 import configure_quantization, generate_outputs


# ---------------------------------------------------------------------------- #
#                            MAIN STREAMLINE FUCNTION                          #
# ---------------------------------------------------------------------------- #

def main_streamline(
    hf_token, 
    openai_api_key,
    audio_filepath,
    audio_model,
    generative_model_type,
    output_filepath
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

    # Set up prompt
    system_msg = "I am an assistant that takes in an audio transcript and then provides summary, key discussion points, takeaways and list of action items"
    user_prompt = "Here is a meeting audio transcript. Please provide the location, date and summary of the meeting with attendees, and list of action items accoridingly: ", transcript
    messages = [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": user_prompt}
    ]

    # Configure quantization and generate outputs
    quant_config = configure_quantization()
    outputs = generate_outputs(
        audio_filepath=audio_filepath,
        model_type=generative_model_type,
        prompt=messages,
        quant_config=quant_config
    )
    
    # Write outputs to Markdown file
    generate_output_file(filepath=output_filepath, output=outputs)


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
    llama3_model = "meta-llama/Meta-Llama-3.1-8B-Instruct"
    output_filepath = "./research/media/transcript.md"
   
    # QuickMeet Streamline
    main_streamline(
        hf_token=hf_token, 
        openai_api_key=openai_api_key,
        audio_filepath=audio_filepath,
        audio_model=audio_model,
        generative_model_type=llama3_model,
        output_filepath=output_filepath
    )


# ---------------------------------------------------------------------------- #
#                                 MAIN EXECUTION                               #
# ---------------------------------------------------------------------------- #

if __name__ == "__main__":
    main()