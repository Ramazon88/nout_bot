from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackQueryHandler, Updater,MessageHandler,CommandHandler,Filters
from function import *
import time
from ast import literal_eval






def start(update, context):
    user = update.message.from_user
    add_user(user.id)
    qadam = get_step(user.id)
    if qadam[0] == None or qadam[0] == literal_eval("{'qadam': 1}"):
        upd_step(user.id, {'qadam': 1})
        update.message.reply_text('Assalomu aleykum Nout.uz sayti botiga xush kelibsiz\nBotdan foydalanish uchun Registratsiyadan o`tishingiz kerak!')
        update.message.reply_text('Iltimos ismingizni kiriting:')
    elif literal_eval(qadam[0]).get("qadam", 0) == 4:
        update.message.reply_text('Quyidagilardan birini tanlang',
                                  reply_markup=ReplyKeyboardMarkup(
                                      [[KeyboardButton('MAHSULOTLAR'), KeyboardButton('BIZ BILAN ALOQA')],
                                       [KeyboardButton('MA`LUMOTLARNI O`ZGARTIRISH')]], resize_keyboard=True))


def for_message(update, context):
    user = update.message.from_user
    msg = update.message.text
    qadam = get_step(user.id)
    admin = admin_inform()
    admins = []
    for i in range(0, len(admin)):
        admins.append(admin[i][0])


    if literal_eval(qadam[0]).get('qadam', 0) == 1:
        upd_step(user.id, {'qadam': 2, 'ism': msg})
        update.message.reply_text('Viloyatingizni tanlang',
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Toshkent"), KeyboardButton("Navoiy")],
                                                                    [KeyboardButton("Andijon"), KeyboardButton("Namangan")],
                                                                    [KeyboardButton("Qashqadaryo"), KeyboardButton("Surxondaryo")],
                                                                    [KeyboardButton("Farg`ona"), KeyboardButton("Sirdaryo")],
                                                                    [KeyboardButton("Samarqand"), KeyboardButton("Qoraqalpog`iston")],
                                                                    [KeyboardButton("Xorazm"), KeyboardButton("Buxoro")],
                                                                    [KeyboardButton("Toshkent viloyati"), KeyboardButton("Jizzax")]], resize_keyboard=True))



    elif literal_eval(qadam[0]).get('qadam', 0) == 2:
        upd_step(user.id, {'qadam':3, 'ism':literal_eval(qadam[0]).get('ism',''), 'locatsiya': msg })
        update.message.reply_text('Telefon raqamingizni kiriting', reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Telefon raqamni yuborish', request_contact=True)]],resize_keyboard=True))

    elif literal_eval(qadam[0]).get('qadam', 0) == 3:
        qadam = upd_step(user.id, {'qadam': 4, 'ism': literal_eval(qadam[0]).get('ism', ''),
                                'locatsiya': literal_eval(qadam[0]).get('locatsiya', ''), 'tel': msg})
        for_inform(user, literal_eval(qadam[0]))
        update.message.reply_text(f"""Ismingiz: {literal_eval(qadam[0]).get('ism', '')}
Username: @{user.username}
Telefon raqamingiz: {literal_eval(qadam[0]).get('tel', '')}
Manzil: {literal_eval(qadam[0]).get('locatsiya', '')}""")
        update.message.reply_text('Yuqoridagilarni tasdiqlaysizmi?',
                                  reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('HA', callback_data='yes'),
                                                                      InlineKeyboardButton('YO`Q', callback_data='no')]]))

    elif literal_eval(qadam[0]).get('qadam', 0) == 4 and msg == 'MAHSULOTLAR':
        update.message.reply_text('Quyidagilardan birini tanlang',
                                  reply_markup=inl_btn())
    elif literal_eval(qadam[0]).get('qadam', 0) == 4 and msg == 'MA`LUMOTLARNI O`ZGARTIRISH':
        del_inform(user.id)
        upd_step(user.id, {'qadam': 1})
        update.message.reply_text(
            'Assalomu aleykum Nout.uz sayti botiga xush kelibsiz\nBotdan foydalanish uchun Registratsiyadan o`tishingiz kerak!')
        update.message.reply_text('Iltimos ismingizni kiriting:')
    elif literal_eval(qadam[0]).get('qadam', 0) == 4 and msg == 'BIZ BILAN ALOQA':
        update.message.reply_text("""Магазин Nout.uz
пн – вс : c 10. 00 до  18.30   без выходных
Звоните:
( 93 ) 399 – 22 -72  Николай
( 90)  371- 73 -17  Артур
(94)  661 -95 -13 Рустам
(90) 973 49 60 Андрей
(90) 994 59 49  Шохрух""")

    elif literal_eval(qadam[0]).get('qadam', 0) == 4 and msg == 'add admin' and user.id == 254118850:
        upd_step(user.id, {'qadam': 30})
        update.message.reply_text("User id kiriting",reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Orqaga')]],resize_keyboard=True))

    elif literal_eval(qadam[0]).get('qadam', 0) == 30 and msg == 'Orqaga':
        upd_step(user.id, {'qadam': 4})
        update.message.reply_text('Quyidagilardan birini tanlang',
                                  reply_markup=ReplyKeyboardMarkup(
                                      [[KeyboardButton('MAHSULOTLAR'), KeyboardButton('BIZ BILAN ALOQA')],
                                       [KeyboardButton('MA`LUMOTLARNI O`ZGARTIRISH')]], resize_keyboard=True))

    elif literal_eval(qadam[0]).get('qadam', 0) == 30:
        inform = for_admin(int(msg))
        add_admin(inform)
        upd_step(user.id, {'qadam': 4})
        update.message.reply_text('Quyidagilardan birini tanlang',
                                  reply_markup=ReplyKeyboardMarkup(
                                      [[KeyboardButton('MAHSULOTLAR'), KeyboardButton('BIZ BILAN ALOQA')],
                                       [KeyboardButton('MA`LUMOTLARNI O`ZGARTIRISH')]], resize_keyboard=True))


    elif literal_eval(qadam[0]).get('qadam', 0) == 4 and msg == 'del admin' and user.id == 254118850:
        upd_step(user.id, {'qadam': 35})
        inform = get_admin_inform()
        text = ''
        for i in range(0, len(inform)):
            text += f"{str(inform[i][0])}. {str(inform[i][1])}  tel: {str(inform[i][2])}\n"
        context.bot.send_message(chat_id = user.id, text = text)
        update.message.reply_text('Quyidagilardan birini tanlang',reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Orqaga')]],resize_keyboard=True))

    elif literal_eval(qadam[0]).get('qadam', 0) == 35 and msg == 'Orqaga':
        upd_step(user.id, {'qadam': 4})
        update.message.reply_text('Quyidagilardan birini tanlang',
                                  reply_markup=ReplyKeyboardMarkup(
                                      [[KeyboardButton('MAHSULOTLAR'), KeyboardButton('BIZ BILAN ALOQA')],
                                       [KeyboardButton('MA`LUMOTLARNI O`ZGARTIRISH')]], resize_keyboard=True))


    elif literal_eval(qadam[0]).get('qadam', 0) == 35:
        del_admin(int(msg))
        upd_step(user.id, {'qadam': 4})
        update.message.reply_text('Quyidagilardan birini tanlang',
                                  reply_markup=ReplyKeyboardMarkup(
                                      [[KeyboardButton('MAHSULOTLAR'), KeyboardButton('BIZ BILAN ALOQA')],
                                       [KeyboardButton('MA`LUMOTLARNI O`ZGARTIRISH')]], resize_keyboard=True))


    elif literal_eval(qadam[0]).get('qadam', 0) == 4 and msg == 'admin'and (user.id in admins):
        upd_step(user.id, {'qadam': 5})
        update.message.reply_text('Parolni kiriting')
    elif literal_eval(qadam[0]).get('qadam', 0) == 5 and msg == '159753':
        upd_step(user.id, {'qadam': 6})
        update.message.reply_text('Nima qilmoqchisiz', reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Mahsulot qo`shish'),
                                                                                          KeyboardButton('Mahsulot o`chirish')],
                                                                                         [KeyboardButton('Bosh sahifa')]],resize_keyboard=True))
    elif literal_eval(qadam[0]).get('qadam', 0) == 5 and msg != '159753' and msg != 'Orqaga':
        update.message.reply_text('Parol xato, qaytadan urinib ko`ring',
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Orqaga')]],resize_keyboard=True))

    elif literal_eval(qadam[0]).get('qadam', 0) == 5 and msg == 'Orqaga':
        upd_step(user.id, {'qadam': 4})
        update.message.reply_text('Quyidagilardan birini tanlang',
                                  reply_markup=ReplyKeyboardMarkup(
                                      [[KeyboardButton('MAHSULOTLAR'), KeyboardButton('BIZ BILAN ALOQA')],
                                       [KeyboardButton('MA`LUMOTLARNI O`ZGARTIRISH')]], resize_keyboard=True))

    elif literal_eval(qadam[0]).get('qadam', 0) == 6 and msg == 'Bosh sahifa':
        upd_step(user.id, {'qadam': 4})
        update.message.reply_text('Quyidagilardan birini tanlang',
                                  reply_markup=ReplyKeyboardMarkup(
                                      [[KeyboardButton('MAHSULOTLAR'), KeyboardButton('BIZ BILAN ALOQA')],
                                       [KeyboardButton('MA`LUMOTLARNI O`ZGARTIRISH')]], resize_keyboard=True))

    elif literal_eval(qadam[0]).get('qadam', 0) == 6 and msg == 'Mahsulot o`chirish':
        upd_step(user.id, {'qadam': 20})
        inform = inform_del()
        text = ''
        for i in range(0, len(inform)):
            text += f"{inform[i][0]}. {inform[i][1]}\n"
        context.bot.send_message(chat_id=user.id, text=text)
        update.message.reply_text('Mahsulot raqaimini yozing', reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Orqaga')]], resize_keyboard=True))

    elif literal_eval(qadam[0]).get('qadam', 0) == 20 and msg == "Orqaga":
        upd_step(user.id, {'qadam': 6})
        update.message.reply_text('Nima qilmoqchisiz',
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Mahsulot qo`shish'),
                                                                     KeyboardButton('Mahsulot o`chirish')],
                                                                    [KeyboardButton('Bosh sahifa')]],
                                                                   resize_keyboard=True))

    elif literal_eval(qadam[0]).get('qadam', 0) == 20:
        upd_step(user.id, {'qadam': 6})
        del_del(int(msg))
        update.message.reply_text('Mahsulot Muavvaqiyatli O`chirildi', reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Mahsulot qo`shish'),
                                                                     KeyboardButton('Mahsulot o`chirish')],
                                                                    [KeyboardButton('Bosh sahifa')]],
                                                                   resize_keyboard=True))

    elif literal_eval(qadam[0]).get('qadam', 0) == 6 and msg == 'Mahsulot qo`shish':
        upd_step(user.id, {'qadam': 7})
        update.message.reply_text('Quyidagilardan birini tanlang',
                                  reply_markup=keyboard_btn('ctg'))
    elif literal_eval(qadam[0]).get('qadam', 0) == 7 and msg == 'Orqaga':
        upd_step(user.id, {'qadam': 6})
        update.message.reply_text('Nima qilmoqchisiz',
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Mahsulot qo`shish'),
                                                                     KeyboardButton('Mahsulot o`chirish')],
                                                                    [KeyboardButton('Bosh sahifa')]],
                                                                   resize_keyboard=True))
    elif literal_eval(qadam[0]).get('qadam', 0) == 7:
        ctg = get_direct_ctg(msg)
        upd_step(user.id, {'qadam': 8})
        add_inform_ctg(ctg[0][0])
        update.message.reply_text('Brend nomi', reply_markup=keyboard_btn('brand'))

    elif literal_eval(qadam[0]).get('qadam', 0) == 8 and msg == 'Orqaga':
        upd_step(user.id, {'qadam': 7})
        del_product_id()
        update.message.reply_text('Quyidagilardan birini tanlang',
                                  reply_markup=keyboard_btn('ctg'))

    elif literal_eval(qadam[0]).get('qadam', 0) == 8:
        upd_brand_id(msg)
        upd_step(user.id, {'qadam': 9})
        update.message.reply_text('Mahsulot nomi yozing', reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Orqaga')]], resize_keyboard=True))

    elif literal_eval(qadam[0]).get('qadam', 0) == 9 and msg == 'Orqaga':
        del_brand_id()
        upd_step(user.id, {'qadam': 8})
        update.message.reply_text('Brend nomi', reply_markup=keyboard_btn('brand'))

    elif literal_eval(qadam[0]).get('qadam', 0) == 9:
        upd_step(user.id, {'qadam': 10})
        upd_inform_name(msg)
        update.message.reply_text('Mahsulot narxini yozing',
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Orqaga')]], resize_keyboard=True))

    elif literal_eval(qadam[0]).get('qadam', 0) == 10 and msg == 'Orqaga':
        upd_step(user.id, {'qadam': 9})
        del_inform_name()
        update.message.reply_text('Mahsulot nomi yozing',
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Orqaga')]], resize_keyboard=True))

    elif literal_eval(qadam[0]).get('qadam', 0) == 10:
        upd_step(user.id, {'qadam': 11})
        upd_inform_price(msg)
        update.message.reply_text('Mahsulot harakteristikasini yozing', reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Orqaga')]], resize_keyboard=True))

    elif literal_eval(qadam[0]).get('qadam', 0) == 11 and msg == 'Orqaga':
        upd_step(user.id, {'qadam': 10})
        del_inform_price()
        update.message.reply_text('Mahsulot narxi yozing',
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Orqaga')]], resize_keyboard=True))

    elif literal_eval(qadam[0]).get('qadam', 0) == 11:
        upd_step(user.id, {'qadam': 12})
        upd_inform_inform(msg)
        update.message.reply_text('Rasmini nomini yozing', reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Orqaga')]], resize_keyboard=True))

    elif literal_eval(qadam[0]).get('qadam', 0) == 12 and msg == 'Orqaga':
        del_inform_inform()
        upd_step(user.id, {'qadam': 11})
        update.message.reply_text('Mahsulot harakteristikasini yozing',
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Orqaga')]], resize_keyboard=True))
    elif literal_eval(qadam[0]).get('qadam', 0) == 12:
        upd_step(user.id, {'qadam': 13})
        upd_inform_image(msg)
        inform = get_inform_finally(last_product())
        context.bot.send_photo(parse_mode="html", chat_id=user.id, caption=inform[0][0], photo=open(inform[0][1], 'rb'))
        update.message.reply_text('Yuqoridagilarni tasdiqlaysimi?',
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Ha'), KeyboardButton('Orqaga')],
                                                                    [KeyboardButton('Bosh menyu')]], resize_keyboard=True))
    elif literal_eval(qadam[0]).get('qadam', 0) == 13 and msg == 'Ha':
        upd_step(user.id, {'qadam': 6})
        update.message.reply_text('Mahsulot Muovaqqiyatli Qo`shildi', reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Mahsulot qo`shish'),
                                                                                          KeyboardButton('Mahsulot o`chirish')],
                                                                                         [KeyboardButton('Bosh sahifa')]],resize_keyboard=True))
    elif literal_eval(qadam[0]).get('qadam', 0) == 13 and msg == 'Bosh menyu':
        del_product_id()
        upd_step(user.id, {'qadam': 6})
        update.message.reply_text('Mahsulot Muovaqqiyatli Qo`shildi',
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Mahsulot qo`shish'),
                                                                     KeyboardButton('Mahsulot o`chirish')],
                                                                    [KeyboardButton('Bosh sahifa')]],
                                                                   resize_keyboard=True))
    elif literal_eval(qadam[0]).get('qadam', 0) == 13 and msg == 'Orqaga':
        del_inform_image()
        upd_step(user.id, {'qadam': 12})
        update.message.reply_text('Rasmini nomini yozing',
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Orqaga')]], resize_keyboard=True))

    else:
        update.message.reply_text('Noto`g`ri buyruq berildi')













def for_inline(update, context):
    msg = update.callback_query.data
    data_spl = msg.split("_")
    if msg == 'no':
        del_inform(update.callback_query.message.chat_id)
        upd_step(update.callback_query.message.chat_id, {'qadam': 1})
        context.bot.delete_message(message_id=update.callback_query.message.message_id,
                                   chat_id=update.callback_query.message.chat_id)
        context.bot.send_message(text='Assalomu aleykum Nout.uz sayti botiga xush kelibsiz\nBotdan foydalanish uchun Registratsiyadan o`tishingiz kerak!',
                                 chat_id=update.callback_query.message.chat_id)
        context.bot.send_message(
            text='Ismingizni kiriting:',
            chat_id=update.callback_query.message.chat_id, )


    elif msg == 'yes':
        upd_step(update.callback_query.message.chat_id, {'qadam': 4})
        context.bot.delete_message(message_id=update.callback_query.message.message_id,
                                   chat_id=update.callback_query.message.chat_id)
        context.bot.send_message(
            text='Quyidagilardan birini tanlang',
            chat_id=update.callback_query.message.chat_id, reply_markup=ReplyKeyboardMarkup([[KeyboardButton('MAHSULOTLAR'), KeyboardButton('BIZ BILAN ALOQA')],
                                                                        [KeyboardButton('MA`LUMOTLARNI O`ZGARTIRISH')]],resize_keyboard=True)  )
    elif msg == 'nazad1':
        update.callback_query.message.edit_text('Quyidagilardan birini tanlang', reply_markup=inl_btn())


    elif len(data_spl) > 1:
        if len(data_spl) > 2:
            if len(data_spl) > 3:
                inform = get_inform_finally(data_spl[2])
                id = update.callback_query.from_user.id
                contact = get_contact(id)
                context.bot.send_message(chat_id=id, text='Rahmat! Tez orada operator siz bilan bog`lanadi')
                context.bot.send_message(parse_mode='html',chat_id=254118850,
                                         text=f"<b>Yangi haridor</b>\n\nIsmi: {contact[0][2]}\nTelefon raqami: {contact[0][3]}\nUsername: {contact[0][1]}\nJoylashuv: {contact[0][4]}\nMahsulot nomi: {inform[0][0]}\nNarxi: {inform[0][1]}")

            else:
                inform = get_inform(data_spl[2])
                id = update.callback_query.from_user.id
                context.bot.send_photo(parse_mode="html",chat_id=id, caption=inform[0][0], photo=open(inform[0][1], 'rb'),
                                       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('SOTIB OLISH',
                                       callback_data=f"{data_spl[0]}_{data_spl[1]}_{data_spl[2]}_{inform[0][2]}")]]))


        else:
            brand_name = get_brand_name(int(data_spl[1]), int(data_spl[0]))
            btn = []
            text = ""
            for i in range(0, len(brand_name)-1, 2):
                text += f"{i+1}. {brand_name[i][1]}\n"
                text += f"{i+2}. {brand_name[i+1][1]}\n"
                a = [InlineKeyboardButton(f'{i+1}', callback_data=f"{data_spl[0]}_{data_spl[1]}_{brand_name[i][0]}"),
                     InlineKeyboardButton(f'{i+2}', callback_data=f"{data_spl[0]}_{data_spl[1]}_{brand_name[i+1][0]}")]
                btn.append(a)
            if len(brand_name) % 2 == 1:
                btn.append([InlineKeyboardButton(f"{len(brand_name)}", callback_data=f"{data_spl[0]}_{data_spl[1]}_{brand_name[-1][0]}")])
                text += f"{len(brand_name)}. {brand_name[-1][1]}\n"

            brand_inl = InlineKeyboardMarkup(btn)
            update.callback_query.message.edit_text(f'{text}', reply_markup=brand_inl)


    elif len(data_spl) == 1:
        brand = for_brand(int(msg))
        btn = []
        for i in range(0, len(brand)-1, 2):
            a = [InlineKeyboardButton(brand[i][1], callback_data=f"{msg}_{brand[i][0]}"),
                 InlineKeyboardButton(brand[i+1][1], callback_data=f"{msg}_{brand[i+1][0]}")]
            btn.append(a)
        if len(brand) % 2 == 1:
            btn.append([InlineKeyboardButton(brand[-1][1], callback_data=f"{msg}_{brand[-1][0]}")])
        btn.append([InlineKeyboardButton('ORQAGA', callback_data='nazad1')])

        brand_inl = InlineKeyboardMarkup(btn)
        update.callback_query.message.edit_text('Quyidagilardan birini tanlang', reply_markup=brand_inl)




def for_contact(update, context):
    user = update.message.from_user
    qadam = get_step(user.id)
    msg = update.message.contact.phone_number
    if literal_eval(qadam[0]).get('qadam', 0) == 3:
        qadam = upd_step(user.id, {'qadam': 4, 'ism': literal_eval(qadam[0]).get('ism', ''),
                                'locatsiya': literal_eval(qadam[0]).get('locatsiya', ''), 'tel': msg})
        for_inform(user, literal_eval(qadam[0]))
        update.message.reply_text(f"""Ismingiz: {literal_eval(qadam[0]).get('ism', '')}
Username: @{user.username}
Telefon raqamingiz: {literal_eval(qadam[0]).get('tel', '')}
Manzil: {literal_eval(qadam[0]).get('locatsiya', '')}""")
        update.message.reply_text('Yuqoridagilarni tasdiqlaysizmi?',
                                  reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('HA', callback_data='yes'),
                                                                      InlineKeyboardButton('YO`Q',
                                                                                           callback_data='no')]]))




def inl_btn():
    ctg = for_ctg()
    btn = []
    for i in range(1, len(ctg), 2):
        a = [InlineKeyboardButton(ctg[i-1][1], callback_data=ctg[i-1][0]),
            InlineKeyboardButton(ctg[i][1],callback_data=ctg[i][0])]
        btn.append(a)
    if len(ctg) %2 == 1:
        btn.append([InlineKeyboardButton(ctg[-1][1], callback_data=ctg[-1][0])])
    return InlineKeyboardMarkup(btn)


def keyboard_btn(type=None):
    if type == 'ctg':
        ctg = for_ctg()
        btn = []
        for i in range(0, len(ctg)-1, 2):
            a = [KeyboardButton(ctg[i][1]), KeyboardButton(ctg[i+1][1])]
            btn.append(a)
        if len(ctg) %2 == 1:
            btn.append([KeyboardButton(ctg[-1][1])])
        btn.append([KeyboardButton('Orqaga')])
        return ReplyKeyboardMarkup(btn, resize_keyboard=True)
    if type == 'brand':
        brand = get_brand()
        btn = []
        for i in range(0, len(brand) - 1, 2):
            a = [KeyboardButton(brand[i][0]), KeyboardButton(brand[i + 1][0])]
            btn.append(a)
        if len(brand) % 2 == 1:
            btn.append([KeyboardButton(brand[-1][0])])
        btn.append([KeyboardButton('Orqaga')])
        return ReplyKeyboardMarkup(btn, resize_keyboard=True)




def main():
    Token = "API_TOKEN"
    updater = Updater(Token)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, for_message))
    updater.dispatcher.add_handler(MessageHandler(Filters.contact, for_contact))
    updater.dispatcher.add_handler(CallbackQueryHandler(for_inline))




    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()