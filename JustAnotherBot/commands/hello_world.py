# coding: utf-8


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hello World!')


def hello(bot, update):
    bot.sendMessage(update.message.chat_id,
                    text='Hello {0}'.format(update.message.from_user.first_name))


