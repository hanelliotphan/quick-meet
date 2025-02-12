# ---------------------------------------------------------------------------- #
# Author: Han-Elliot Phan                                                      #
# Email: hanelliotphan@gmail.com                                               #
#                                                                              #
# Last update: February 11, 2025                                               #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# file_processor.py                                                            #
#                                                                              #
# This file is for processing input/outfile files:                             #
# 1. Import audio files and generate transcript                                #
# 2. Output a file with summary, keypoints, takeways and list of action items  # 
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#                               IMPORT LIBRARIES                               #
# ---------------------------------------------------------------------------- #

import openai
import logging
import sys


# ---------------------------------------------------------------------------- #
#                          FILE PROCESSING FUNCTIONS                           #
# ---------------------------------------------------------------------------- #

def process_audio_file(audio_filepath, audio_model):
    audio = open(audio_filepath, "rb")
    try:
        logging.info(msg=f"[file_processor.py] process_audio_file: Processing the audio file '{audio_filepath}'...")
        transcript = openai.audio.transcriptions.create(
            model=audio_model,
            file=audio,
            response_format="text"
        )
        return transcript
    except Exception as e:
        logging.critical(msg=f"[file_processor.py] process_audio_file: Cannot generate transcript from audio file '{audio_filepath}'. Error message: {e}")
        sys.exit(-1)