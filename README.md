# Live Language Translation Device

##Demonstration Link:

https://youtu.be/todQIdqSozo

## Abstract

The Live Language Translation Device is a revolutionary tool designed to facilitate real-time language translation. It enables users to record their voice and receive instant translations into a different language. This device proves to be invaluable for travelers visiting countries where they are not fluent in the local language, allowing seamless communication with locals, seeking directions, and understanding tour guides. The device incorporates a two-way communication feature, ensuring smooth conversations without the need to wait for individual phrases or sentences to be translated. Additionally, it can function offline, providing essential translation support even in situations with limited internet connectivity.

## Project Objectives

The primary objective of the Live Language Translation Device is to enable effective communication by providing instant and understandable translations of spoken language in real-time. While the translation may not always be entirely error-free or fully logical, it aims to be comprehensible to facilitate communication between individuals from different linguistic backgrounds. The device is particularly suitable for non-public, company-internal communication and information sharing, where quick transmission of text content is essential but not intended for a large audience. It is crucial that all parties involved are aware of the use of machine translation.

## Project Components

- Microphone: Records and captures the user's spoken words for translation.
- Activate/Repeat Switch: Triggers the device's functionality, allowing convenient activation and repetition of translation processes.
- OLED Screen: Displays prompts and messages to guide users through the translation process.
- Speakers: Plays back the translated audio in the desired language.

## Project Setup

1. Assemble the hardware components, including the Raspberry Pi, microphone, activate/repeat switch, OLED screen, and speakers.
2. Install the required software components:
   - gTTS (Google Text-to-Speech): `pip install gtts`
   - SpeechRecognition: `pip install SpeechRecognition`
   - Pyaudio: `pip install pyaudio`
   - Googletrans: `pip install googletrans==3.1.0a0`
   - Adafruit_SSD1306: Refer to the [Adafruit_SSD1306 GitHub repository](https://github.com/adafruit/Adafruit_Python_SSD1306) for installation instructions.
   - Pygame: Refer to the [Pygame website](https://www.pygame.org/wiki/GettingStarted) for installation instructions.
3. Connect the hardware components to the Raspberry Pi as per the provided documentation and ensure proper connections.
4. Copy the provided Python code into the Raspberry Pi environment and save it as a Python script.
5. Execute the Python script to run the Live Language Translation Device.

## Challenges and Future Improvements

Throughout the project, we encountered several challenges, including implementing rolling text display on the OLED screen and addressing compatibility issues with certain audio modules on the Raspberry Pi. As future improvements, we plan to enhance the device's multilingual capabilities by allowing flexible input language options.

## Credits and References

### Credits:

- Saniya Jain: Project Co-Creator and Developer.
- Aman Bhatt: Project Co-Creator and Developer.

### References:

- Adafruit Industries: [https://www.adafruit.com/](https://www.adafruit.com/)
- Python Software Foundation: [https://www.python.org/](https://www.python.org/)
- Google Translate: [https://translate.google.com/](https://translate.google.com/)
- gTTS (Google Text-to-Speech): [https://github.com/pndurette/gTTS](https://github.com/pndurette/gTTS)
- Pyaudio: [https://pypi.org/project/pyaudio/](https://pypi.org/project/pyaudio/)
- SpeechRecognition: [https://github.com/Uberi/speech_recognition](https://github.com/Uberi/speech_recognition)
- The Official Raspberry Pi Website: [https://www.raspberrypi.org/](https://www.raspberrypi.org/)
- The Python Standard Library Documentation: [https://docs.python.org/](https://docs.python.org/)

## Conclusion

The Live Language Translation Device demonstrates the potential of machine translation technologies in enabling effective communication across linguistic barriers, making it a valuable tool for travelers, international business professionals, and individuals seeking to interact in diverse linguistic environments. With further refinements and improvements, this device could become an indispensable asset for fostering global communication and understanding.

Please feel free to contribute to this project and share your ideas for future enhancements.

Happy Translating!
