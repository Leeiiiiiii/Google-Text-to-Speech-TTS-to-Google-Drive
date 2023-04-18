# Google-Text-to-Speech-TTS-to-Google-Drive
This script uses the Google Cloud Text-to-Speech API to generate an audio file from a given text and language, and uploads the file to a specific folder in Google Drive. This could be useful for generating audio files for language learning or other applications.

## Prerequisites
To use this script, you'll need the following:

* A Google Cloud Platform account with access to the Text-to-Speech API
* A Google Cloud Platform service account key file with access to the Text-to-Speech API
* A Google Drive folder ID where you want to upload the audio file

## Installation
1. Clone this repository: git clone https://github.com/Leeiiiiiii/Google-Text-to-Speech-TTS-to-Google-Drive/
2. Install the required Python packages: pip install -r requirements.txt
3. Move your Google Cloud Platform service account key file to the repository folder and rename it to service.json

## Usage
To use this script, follow these steps:

1. Open a terminal in the repository folder.
2. Run the script: python tts-to-drive.py
3. Enter the word you want to generate audio for when prompted.
4. Enter the language code for the language you want to generate audio in (e.g., en for English or fi for Finnish) when prompted.
5. The script will generate an audio file and upload it to the Google Drive folder specified in the folder_id variable.
