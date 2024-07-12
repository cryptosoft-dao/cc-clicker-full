from telebot import types
import telebot
import requests

URL = 'https://crypto-cash.netlify.app'
TG_TOKEN = '7280149547:AAGPHWS3FzdQn4FqOTziYlCEuBXmVsQjrYY'
BASE_URL = 'https://953a-46-174-112-153.ngrok-free.app'

def webAppKeyboard():
   keyboard = types.InlineKeyboardMarkup(row_width=1)
   webAppTest = types.WebAppInfo(URL)
   one_butt = types.InlineKeyboardButton(text="Играть!", web_app=webAppTest)
   keyboard.add(one_butt)

   return keyboard
def has_referrer(user_id):
    res = requests.post(f'{BASE_URL}/ref/has_ref',json={'tg_id':user_id})
    return res.json()['has_ref']
def get_all_users():
    data = requests.post(f'{BASE_URL}/users/all')
    return data.json()['users']
def add_ref(creator, come, has_tg_premium, user_name):
    requests.post(f'{BASE_URL}/ref/add',json={'creator':creator,'come':come, 'has_tg_premium':has_tg_premium, 'user_name':user_name})

bot = telebot.TeleBot(TG_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message: types.Message):
    bot.send_message( message.chat.id, '''
Заходи!
''', reply_markup=webAppKeyboard()) 
    
    
    user_id = message.from_user.id
    if not has_referrer(user_id):
        if " " in message.text:
            referrer_candidate = message.text.split()[1]
            try:
                referrer_candidate = int(referrer_candidate)
                if user_id != referrer_candidate and referrer_candidate in get_all_users():
                    referer = referrer_candidate
                    has_tg_premium = message.from_user.is_premium
                    user_name = message.from_user.first_name
                    add_ref(referer, user_id, has_tg_premium, user_name)

            except ValueError as e:
                print('e: ',e)
                pass

bot.infinity_polling()
