import telebot, BraintreeAuth, tools, random, checkeproxy

token = "7601155492:AAHlQulfkyRELaFDvpgKEKux__e8YR09ZVc"

bot = telebot.TeleBot(token=token)

#comando /on
@bot.message_handler(commands=["on"])
def on_handler(message):
    mensaje = message.text.split(" ")[1]
    cc, mm, yy, cvv = mensaje.split("|")
    username = message.from_user.username
    country, data, bank = tools.data_bin(str(cc))
    id_msj = bot.send_message(message.chat.id, text=f"""
»𝙲𝚊𝚛𝚍 -> {cc}|{mm}|{yy}|{cvv}
»𝚂𝚝𝚊𝚝𝚞𝚜 -> Processing

𝙸𝙽𝙵𝙾 𝙱𝙸𝙽

»𝙲𝚘𝚞𝚗𝚝𝚛𝚢 ->  {country}
»𝙳𝚊𝚝𝚊 -> {data}
»𝙱𝚊𝚗𝚔 -> {bank} 

𝙾𝚃𝙷𝙴𝚁
𝙲𝚑𝚎𝚌𝚔𝚎𝚍 𝚋𝚢 -> @{username}  
𝙶𝚊𝚝𝚎𝚠𝚊𝚢 -> 𝙾𝚗𝚊𝚖𝚒 - B3 Auth
𝙱𝚘𝚝 𝚋𝚢 -> @Ryder_2417""").id

    responseCard, status  = BraintreeAuth.chk(cc, mm, yy, cvv)
    bot.edit_message_text(text=f"""
»𝙲𝚊𝚛𝚍 -> {cc}|{mm}|{yy}|{cvv}
»𝚂𝚝𝚊𝚝𝚞𝚜 -> {status}
»𝚁𝚎𝚜𝚙𝚘𝚗𝚜𝚎 -> {responseCard}

𝙸𝙽𝙵𝙾 𝙱𝙸𝙽

»𝙲𝚘𝚞𝚗𝚝𝚛𝚢 ->  {country}
»𝙳𝚊𝚝𝚊 -> {data}
»𝙱𝚊𝚗𝚔 -> {bank} 

𝙾𝚃𝙷𝙴𝚁
𝙲𝚑𝚎𝚌𝚔𝚎𝚍 𝚋𝚢 -> @{username}
𝙶𝚊𝚝𝚎𝚠𝚊𝚢 -> 𝙾𝚗𝚊𝚖𝚒 - B3 Auth
𝙱𝚘𝚝 𝚋𝚢 -> @Ryder_2417""", message_id=id_msj, chat_id=message.chat.id)

    
bot.polling(non_stop=True)
    
    