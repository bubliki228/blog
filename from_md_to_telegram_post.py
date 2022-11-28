# -*- coding: utf-8 -*-
import telebot
import markdown
bot = telebot.TeleBot("1451808041:AAEbQKwW70Kd-oItc7CdYADNnZ2tOhp3N5k", skip_pending=True)

stroka='_posts/22-11-10-random-coffee.md'


f = open(stroka, 'r', encoding="utf8")
text = f.read()
text = text[text.find('---', 2)+5:]
html = markdown.markdown(text).replace('<p>', '').replace('</p>', '\n')
print(type(html), html)



@bot.message_handler(commands=['send'])

def mailing(message):
    bot.send_message(message.chat.id, html, parse_mode="HTML")



if __name__ == '__main__':
    try:
        bot.infinity_polling()
    except Exception as ex: 
        print('Возникла осечка в работе программы.\nПричина: ')
        print(ex, type(ex), sep='\n')