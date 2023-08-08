# Importing necessary modules required
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import pygame
import os
from gpiozero import Button
from time import sleep
import sys

flag = 0

# A tuple containing all the language and codes of the language will be detected
dic = ('english', 'en', 'hindi', 'hi', 'spanish', 'es')

# Creating Recognizer() class object
def do_stuff():
    recog1 = sr.Recognizer()

    # Creating microphone instance
    mc = sr.Microphone()

    # Capture Voice
    # playsound("translate_tts.mp3")

    with mc as source:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        try:
            # recog1.adjust_for_ambient_noise(source, duration=0.2)
            # audio = recog1.listen(source)
            # yText = recog1.recognize_google(audio)
            MyText = 'hello'
        except Exception as e:
            print("say that again please.....")

        MyText = MyText.lower()

        if 'hello' in MyText:
            # Capture Voice
            # takes command through microphone
            disp = Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3C)
            small_font = ImageFont.truetype('FreeSans.ttf', 20)
            large_font = ImageFont.truetype('FreeSans.ttf', 20)
            disp.begin()
            disp.clear()
            disp.display()

            # Make an image to draw on in 1-bit color.
            width = disp.width
            height = disp.height
            image = Image.new('1', (width, height))
            draw = ImageDraw.Draw(image)

            def display_message(top_line, line_2):
                draw.rectangle((0, 0, width, height), outline=0, fill=0)
                draw.text((0, 0), top_line, font=large_font, fill=255)
                draw.text((0, 25), line_2, font=small_font, fill=255)
                disp.image(image)
                disp.display()

            def takecommand():
                r = sr.Recognizer()
                with sr.Microphone(device_index=1) as source:
                    print("Listening.....")
                    display_message("Listening", "....")
                    # time.sleep(0.1)
                    r.pause_threshold = 1
                    audio = r.listen(source)
                    disp.clear()
                    try:
                        print("Recognizing.....")
                        display_message("Recognizing", "Language")
                        query = r.recognize_google(audio, language='en-in')
                        print(f"The User said {query}\n")
                    except Exception as e:
                        print("say that again please.....")
                        display_message("Error", "Say Again!")
                        return "None"
                    return query

            # Input from user
            # Make input to lowercase
            query = takecommand()
            # playsound("/Users/amanbhatt/Desktop/translate_tts _which.mp3")

            def destination_language():
                print("Enter the language in which you want to convert : Ex. Hindi , English , etc.")
                print()
                # Input destination language in which the user wants to translate
                to_lang = takecommand()

                while to_lang == "None":
                    to_lang = takecommand()

                to_lang = to_lang.lower()
                return to_lang

            to_lang = destination_language()

            # Mapping it with the code
            while to_lang not in dic:
                print("Language in which you are trying to convert is currently not available, please input some other language")
                print()
                to_lang = destination_language()
                to_lang = dic[dic.index(to_lang) + 1]

            # invoking Translator
            translator = Translator()

            # Translating from src to dest
            text_to_translate = translator.translate(query, dest=to_lang)
            text = text_to_translate.text
            text = text.strip()

            # Using Google-Text-to-Speech ie, gTTS() method
            # to speak the translated text into the destination language which is stored in to_lang.
            # Also, we have given the 3rd argument as False because by default it speaks very slowly
            speak = gTTS(text=text, lang=to_lang, slow=True)

            # Using the save() method to save the translated speech in capture_voice.mp3
            speak.save("captured_voice.mp3")

            display_message("Speaking", ".....")

            # Using the OS module to run the translated voice.
            file = 'captured_voice.mp3'
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            os.remove('captured_voice.mp3')

            # Printing Output
            print(text)

 
