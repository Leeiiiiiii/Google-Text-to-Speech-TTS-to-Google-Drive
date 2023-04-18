from google.cloud import texttospeech
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
import io

def synthesize_text(text, language_code):
    credentials = service_account.Credentials.from_service_account_file(' insert credentials_file_path')
    client = texttospeech.TextToSpeechClient(credentials=credentials)

    input_text = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(input=input_text, voice=voice, audio_config=audio_config)

    return response.audio_content

if __name__ == '__main__':
    credentials_file_path = 'insert path here'
    folder_id = 'insert folder id'
    text = input("Enter a word: ")
    language = input("Enter a language (fi for Finnish, en for English): ")

    if language == 'fi':
        language_code = 'fi-FI'
    elif language == 'en':
        language_code = 'en-US'
    else:
        print('Invalid language code entered.')
        exit()

    file_name = f'{text}_{language}.mp3'

    credentials = service_account.Credentials.from_service_account_file(credentials_file_path)

    file_content = synthesize_text(text, language_code)
    file = io.BytesIO(file_content)

    # Upload the file to Google Drive
    drive_service = build('drive', 'v3', credentials=credentials)
    file_metadata = {'name': file_name, 'parents': [folder_id]}
    media = MediaIoBaseUpload(file, mimetype='audio/mpeg', chunksize=1024*1024, resumable=True)
    uploaded_file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f'File ID: {uploaded_file.get("id")}')
