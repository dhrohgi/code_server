import telegram
import asyncio

token = '6178966064:AAHC3qOwkdIBpgn9EVqBPH05x3EW9H8AcTQ'
bot = telegram.Bot(token=token)

chat_id = 324528049
asyncio.run(bot.send_message(chat_id=chat_id, text = 'hello'))