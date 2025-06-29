from gtts import gTTS
import os

# Read the text file containing the Icelandic words and phrases
with open('../data/icelandic_words.txt', 'r') as f:
    words = f.readlines()

# Iterate over each word and generate an audio file using the gtts library
for word in words:
    # Remove the newline character at the end of the word
    word = word.strip()

    # Generate an audio file for the word using the gtts library
    audio_file = f'{word}.mp3'
    tts = gTTS(word, lang='is')
    tts.save(f"./is_audio/{audio_file}")

    # Print the name of the audio file for debugging purposes
    print(f'Generated audio file: {audio_file}')
