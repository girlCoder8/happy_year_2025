# Happy New Year 2025 - Text-to-Speech Project

This project generates a **Happy New Year 2025** greeting using text-to-speech technology powered by the [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/) library. It creates and saves the greeting as a `.mp3` audio file.

## Features

- Converts a custom "Happy New Year 2025" message from text to speech.
- Saves the generated audio as an `.mp3` file on your device.
- Simple and straightforward implementation using Python.

## Prerequisites

Before running this project, ensure that you have the following installed:

- **Python 3.6 or above**: You can download Python from [python.org](https://www.python.org/).
- **gTTS library**: Install it using the command below.

## Installation

1. Clone the project or download the source code.

```bash
   git clone https://girlCoder8/username/happy-new-year-2025.git
   ```
2. Navigate to the project folder.

```bash
   cd happy-new-year-2025
   ```
3. Install the necessary dependencies using the following command:

   ```bash
   pip install gTTS
   ```

## Usage

1. Open the Python script and verify the text message you want to convert into speech.
2. Run the Python script. It will generate and save an `.mp3` file with your greeting message as audio.

Example command to run the script:
```bash
python3 happy_new_year.py
```

3. Find the generated `.mp3` file (e.g., `happy_new_year_2025.mp3`) in the project folder. Play the file in any compatible media player.

## Code Overview

Below is a basic step-by-step overview of what the script does:

1. Imports the `gTTS` library for text-to-speech conversion.
2. Sets the "Happy New Year 2025" message as text to be converted.
3. Uses `gTTS` to convert the text message into audio while specifying the desired language (e.g., English).
4. Saves the audio output as an `.mp3` file.

## Usage in the Code

The following example shows how to convert the "Happy New Year 2025" greeting into an `.mp3` file:

```python
from gtts import gTTS

# Message to convert into audio
message = "Happy New Year 2025! Wishing you joy, health, and success in the coming year."

# Convert text to speech
tts = gTTS(text=message, lang='en')

# Save the output as an MP3 file
tts.save("happy_new_year_2025.mp3")
print("Audio file saved as happy_new_year_2025.mp3")
```

## Customizing the Project

- **Change the Language**: Modify the `lang` parameter to the desired language (`'en'` for English, `'es'` for Spanish, etc.). Refer to the [gTTS language support](https://gtts.readthedocs.io/en/latest/module.html#languages) for supported languages.
- **Modify the Greeting Message**: Change the text in the `message` variable to any greeting of your choice.

## If Error: "sh: start: command not found"
- Ensure that your path to the start command is correct
- Example: `/path/to/script.sh`
- Ensure the file has execute permissions: `chmod +x /path/to/start`


## License

This project is licensed under the MIT License. Feel free to use, modify, and share!

---

Enjoy this small project and share your **Happy New Year 2025** greetings with others through speech!