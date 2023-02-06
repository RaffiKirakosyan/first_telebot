import telebot
from telebot import types

"""
documentations
https://github.com/eternnoir/pyTelegramBotAPI/tree/master/examples/webhook_examples
https://pytba.readthedocs.io/en/latest/types.html#telebot.types.InputFile


"""

my_bot_token = "6048114555:AAEnM7-rD6P58apEO5D-IRix5-rATk9goDQ"
bot = telebot.TeleBot(token = my_bot_token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "<b>Welcome</b>", parse_mode="html")
    
    
    


@bot.message_handler(commands=["help"])
def help(message):
    with open("./files/help.info", "r") as help_file:
        help_text = ""
        for line in help_file:
            help_text += line
        

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
        
        item1 = types.KeyboardButton("Good")
        item2 = types.KeyboardButton("Bad")
        item3 = types.KeyboardButton("IDK")

        markup.add(item1, item2, item3)

        mup = types.MenuButtonCommands(["start","help","end"])
        

        bot.send_message(message.chat.id, help_text, parse_mode = "html", reply_markup = markup)

@bot.message_handler(commands=["end"])
def end(message):
    bot.send_message(message.chat.id, "Bye!!!")
    stic = open("./resources/bye.webp","rb")
    bot.send_sticker(message.chat.id, sticker = stic)

@bot.message_handler(content_types=['text'])
def other_texts(message):
    if message.chat.type == 'private':
        if message.text == "Good":
            do_good(message)
        elif message.text == "Bad":
            do_bad(message)
        elif message.text == "IDK":
            think(message)
        else:
            bot.send_message(message.chat.id, "I dont know what to say")
        


@bot.message_handler()
def do_good(message):
    bot.send_message(message.chat.id, "its good", reply_markup = types.ReplyKeyboardRemove())

@bot.message_handler()
def do_bad(message):
    bot.send_message(message.chat.id, "its not good", reply_markup = types.ReplyKeyboardRemove())

@bot.message_handler()
def think(message):
    bot.send_message(message.chat.id, "go and think about that", reply_markup = types.ReplyKeyboardRemove())










if __name__ == "__main__":
    print("server is runned")
    bot.polling(non_stop = True)
    print("server finish his work")
