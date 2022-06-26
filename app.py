from gtts import gTTS
import telebot
import os
import configparser

setting = configparser.ConfigParser()
setting.read('setting.ini')

bot = telebot.TeleBot(setting['GENERAL']['TOKEN'])


def convert_txt_to_speech(text='', lang='ru', slow=False, id=''):
    if text != '':
        convert = gTTS(text=text, lang=lang, slow=slow)
        convert.save(f'{id}.mp3')
        with open(f'{id}.mp3', 'rb') as file:
            audio = file.read()
        os.remove(f'{id}.mp3')
        return audio


@bot.message_handler(commands=["check"])
def start(m):
    bot.send_message(m.chat.id, 'Я готов к работе')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_audio(message.chat.id, convert_txt_to_speech(text=message.text, id=message.chat.id), title='Вы ввели:')


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
