# Jarvis AI Assistant

Jarvis is a voice-controlled AI assistant implemented in Python. It leverages various libraries and APIs to understand voice commands, process natural language, and perform tasks such as web searches, opening websites, playing music, and interacting with the OpenAI GPT-3 model.

## Features

- **Voice Recognition:** Utilizes the SpeechRecognition library to capture voice input from the user.
- **Natural Language Processing:** Interacts with the OpenAI GPT-3 model for generating responses to user queries.
- **Text-to-Speech Conversion:** Employs the pyttsx3 library to convert text responses to speech.
- **Web Search and YouTube Playback:** Can open specified websites and search and play videos on YouTube based on user queries.
- **System Information:** Provides current time, date, and day.
- **Camera Access:** Opens the system's camera.
- **Configuration:** Allows customization through a configuration file (config.py).

## Requirements

- Python 3.x
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [OpenAI GPT-3 API Key](https://beta.openai.com/signup/)
- [YouTube Data API Key](https://developers.google.com/youtube/registering_an_application)

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mannan258/Jarvis-AI-Assistant.git
   cd jarvis-ai

2. **Configure API keys:**
   
   Replace the placeholder API keys in **`config.py`** with your actual keys.

3. **Run the application:**

   ```bash
   python main.py

## Usage

- **Voice Commands:**
  - Speak clearly and wait for Jarvis to respond.
  - Use commands like "Jarvis, open YouTube," "Jarvis, play music," or "Jarvis, what's the time?"

- **Custom Commands:**
  - Edit the `sites` list in `main.py` to include your preferred websites.

- **Exit Jarvis:**
  - Say "Jarvis Exit" to terminate the application.

- **Reset Chat History:**
  - Say "reset chat" to clear the chat history.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



