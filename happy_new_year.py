from gtts import gTTS
import os


def create_audio_message():
    message = "Happy 2025 EVERYONE! Wishing you a fantastic and prosperous year ahead."
    language = 'en'

    tts = gTTS(text=message, lang=language, slow=False)
    tts.save("happy_new_year.mp3")

    os.system("start happy_new_year.mp3")


if __name__ == "__main__":
    create_audio_message()
