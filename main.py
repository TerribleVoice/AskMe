from keyboard.kb_kick import kb_kick
from database.config import username_bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from database.database_main import database
from keyboard.kb_captcha import kb_captcha_1, kb_captcha_2, kb_captcha_3, kb_captcha_4, kb_captcha_5, kb_captcha_6, kb_captcha_7
from aiogram import types, Dispatcher, executor, Bot
from config.config_telegram import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import datetime
import asyncio
import aioschedule
import csv
import random
from contextlib import suppress
from aiogram.utils.exceptions import (MessageToEditNotFound, MessageCantBeEdited, MessageCantBeDeleted,
                                      MessageToDeleteNotFound)

async def delete_message(message: types.Message, sleep_time: int = 0):
    await asyncio.sleep(sleep_time)
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await message.delete()

id_send_users = 870590792 # id человека, которому доступна функция рассылки

bot = Bot(token=TOKEN)

dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler(commands=['KickRedFlag'])
async def KickRedFlag_command(message: types.Message):
    message_chat_id = message.chat.id
    if message_chat_id < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        check_attack = database.get_attack_chat(id_chat=message_chat_id)
        if check_attack[0][0] == True:
            pass
        else:
            user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            user_id_is_admin = user_admin['status']
            if user_id_is_admin != 'member':
                users = database.get_users_kdf(id_chat=message_chat_id)
                if users == []:
                    await message.answer("You have 0 users with a red flag in this chat!")
                else:
                    await message.answer(f"You have {len(users)} users with a red flag in this chat, and now the bot will kick them!")
                    for user in users:
                        id_user = user[0]
                        id_chat = user[1]
                        await bot.kick_chat_member(chat_id=id_chat, user_id=id_user)
                        database.delete_user_from_kdf(id_user=id_user, id_chat=id_chat)

            else:
                await message.reply(text='You do not have permission to do this!')




@dp.message_handler(commands=['start']) # /start (пользователь выбирает язык под себя)
async def start_command_hello_user(message: types.Message):
    chat_user = message.chat.id
    if chat_user > 0:
        # Список всех языков
        keyboard_language = InlineKeyboardMarkup()
        keyboard_language_button_ru = InlineKeyboardButton(text='🇷🇺Русский', callback_data='ru')
        keyboard_language_button_eng = InlineKeyboardButton(text='🇬🇧English', callback_data='gb')
        keyboard_language_button_arab = InlineKeyboardButton(text='🇸🇦العربية', callback_data='sa')
        keyboard_language_button_it = InlineKeyboardButton(text='🇮🇹Italiano', callback_data='it')
        keyboard_language_button_esp = InlineKeyboardButton(text='🇪🇸Espanol', callback_data='esp')
        keyboard_language_button_norw = InlineKeyboardButton(text='🇳🇴Norwegian', callback_data='norw')
        keyboard_language_button_ind = InlineKeyboardButton(text='🇮🇩Indonesian', callback_data='ind')
        keyboard_language_button_rom = InlineKeyboardButton(text='🇷🇴Romanian', callback_data='rom')
        keyboard_language_button_slovak = InlineKeyboardButton(text='🇸🇰Slovak', callback_data='slov')
        keyboard_language_button_fin = InlineKeyboardButton(text='🇫🇮Finnish', callback_data='fin')
        keyboard_language_button_eesti = InlineKeyboardButton(text='🇪🇪Eesti', callback_data='eesti')
        keyboard_language_button_port = InlineKeyboardButton(text='🇧🇷Portugues Brasil🇵🇹', callback_data='port_bras')
        keyboard_language_button_chin = InlineKeyboardButton(text='🇨🇳Chinese', callback_data='chin')
        keyboard_language_button_deu = InlineKeyboardButton(text='🇩🇪Deutsch', callback_data='deu')
        keyboard_language_button_french = InlineKeyboardButton(text='🇫🇷French', callback_data='fren')
        keyboard_language_button_kor = InlineKeyboardButton(text='🇰🇵Korean', callback_data='kor')
        keyboard_language_button_czech = InlineKeyboardButton(text='🇨🇿Czech', callback_data='czech')
        keyboard_language_button_turk = InlineKeyboardButton(text='🇹🇷Turkce', callback_data='turk')
        keyboard_language_button_cat = InlineKeyboardButton(text='🇪🇸Catalan', callback_data='catalan')
        keyboard_language_button_hung = InlineKeyboardButton(text='🇭🇺Hungarian', callback_data='hung')
        keyboard_language_button_bulg = InlineKeyboardButton(text='🇧🇬Bulgarian', callback_data='bulg')

        keyboard_language.add(keyboard_language_button_ru, keyboard_language_button_eng)
        keyboard_language.add(keyboard_language_button_arab, keyboard_language_button_it)
        keyboard_language.add(keyboard_language_button_esp, keyboard_language_button_norw)
        keyboard_language.add(keyboard_language_button_ind, keyboard_language_button_rom)
        keyboard_language.add(keyboard_language_button_slovak, keyboard_language_button_fin)
        keyboard_language.add(keyboard_language_button_eesti, keyboard_language_button_port)
        keyboard_language.add(keyboard_language_button_chin, keyboard_language_button_deu)
        keyboard_language.add(keyboard_language_button_french, keyboard_language_button_czech)
        keyboard_language.add(keyboard_language_button_turk, keyboard_language_button_cat)
        keyboard_language.add(keyboard_language_button_hung, keyboard_language_button_bulg)

        await message.answer('Choose language', reply_markup=keyboard_language)

# Начало (выбор языка)
# Когда пользователь выбрал язык
@dp.callback_query_handler(text='ru')
async def choose_language_ru(call: types.CallbackQuery):
    database.check_user_who_in_all_users(id_user=call.from_user.id,
                                         first_name=call.from_user.first_name,
                                         language='ru')
    kb_start = InlineKeyboardMarkup(resize_keyboard=True)
    kb_button_commands = InlineKeyboardButton(text='Узнать о возможностях бота', callback_data='commands')
    kb_button_invite_chat = InlineKeyboardButton(text='Добавить в чат', url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase', callback_data='invite_chat')
    kb_button_site = InlineKeyboardButton(text='Сайт', url='https://redop.netlify.app', callback_data='our_site')
    kb_button_channel = InlineKeyboardButton(text='Наш канал', url='https://t.me/official_redop', callback_data='our_channel')
    kb_button_change_language = InlineKeyboardButton(text='Сменить язык', callback_data='change_language')
    kb_button_captcha = InlineKeyboardButton(text='Настройка каптчи', callback_data='settings_captcha')
    kb_start.add(kb_button_invite_chat, kb_button_channel)
    kb_start.add(kb_button_site, kb_button_commands)
    kb_start.add(kb_button_change_language)
    kb_start.add(kb_button_captcha)

    user_name = call.values['from']['first_name']
    user_id = call.values['from']['id']
    try:
        database.update_user_language(id_user=user_id, language='ru')
    except Exception as ex:
        database.check_user_who_in_all_users(id_user=user_id, first_name=user_name, language='ru')
    await call.message.answer(f"""Redop – инновационное решение для борьбы со спамом в Телеграме. Бот предлагает каждому новому пользователю совершить несколько действий в течение одной минуты. Обычным пользователям не составит труда их выполнить, однако вредоносным ботам он отказывает в доступе. 

В настоящее время поддержкой бота @Redop_AntiSpam_bot занимается https://redop.netlify.app/  

Если у вас возникнут какие-то вопросы, то вы всегда можете обратиться за помощью на нашем сайте или в контактах в описании бота. 

Наши специалисты с радостью ответят вам на любые вопросы.

Мы благодарны за то, что вы сделали правильный выбор для безопасности и модерации своих групп на платформе Telegram.""")

    await call.message.answer("""
Для успешной работы с ботом, вам необходимо:

1. Добавить Redop в группу и назначьте его администратором.

2. После входа вы увидите список ваших групп, в которые добавлен Redop bot.""", reply_markup=kb_start)


@dp.callback_query_handler(text='gb')
async def choose_language_ru(call: types.CallbackQuery):
    database.check_user_who_in_all_users(id_user=call.from_user.id,
                                         first_name=call.from_user.first_name,
                                         language='gb')
    kb_start = InlineKeyboardMarkup(resize_keyboard=True)
    kb_button_commands = InlineKeyboardButton(text='Learn about the capabilities of the bot', callback_data='commands')
    kb_button_invite_chat = InlineKeyboardButton(text='Add a chat',
                                                 url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                 callback_data='invite_chat')
    kb_button_site = InlineKeyboardButton(text='Website', url='https://redop.netlify.app', callback_data='our_site')
    kb_button_channel = InlineKeyboardButton(text='Our channel', url='https://t.me/official_redop',
                                             callback_data='our_channel')
    kb_button_change_language = InlineKeyboardButton(text='Change language', callback_data='change_language')
    kb_button_captcha = InlineKeyboardButton(text='Settings captcha', callback_data='settings_captcha')
    kb_start.add(kb_button_invite_chat, kb_button_channel)
    kb_start.add(kb_button_site, kb_button_commands)
    kb_start.add(kb_button_change_language)
    kb_start.add(kb_button_captcha)

    user_name = call.values['from']['first_name']
    user_id = call.values['from']['id']
    try:
        database.update_user_language(id_user=user_id, language='gb')
    except Exception as ex:
        database.check_user_who_in_all_users(id_user=user_id, first_name=user_name, language='gb')
    await call.message.answer(f"""Redop is an innovative solution for fighting spam in Telegram. The bot prompts each new user to perform several actions within one minute. Normal users will have no trouble completing them, but it denies access to malicious bots. 

The @Redop_AntiSpam_bot is currently supported by https://redop.netlify.app/  

If you have any questions, you can always ask for help on our website or in the contacts in the bot description. 

Our specialists will be happy to answer any questions you may have.

We are grateful that you have made the right choice for the security and moderation of your groups on the Telegram platform.""")

    await call.message.answer("""

To successfully work with the bot, you need:

1. Add Redop to the group and appoint him as an administrator.

2. After logging in, you will see a list of your groups to which Redop bot has been added.

Translated with www.DeepL.com/Translator (free version)""", reply_markup=kb_start)


@dp.callback_query_handler(text='bulg')
async def choose_language_ru(call: types.CallbackQuery):
    database.check_user_who_in_all_users(id_user=call.from_user.id,
                                         first_name=call.from_user.first_name,
                                         language='bulg')
    kb_start = InlineKeyboardMarkup(resize_keyboard=True)
    kb_button_commands = InlineKeyboardButton(text='Команди', callback_data='commands')
    kb_button_invite_chat = InlineKeyboardButton(text='Добавяне към чат',
                                                 url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                 callback_data='invite_chat')
    kb_button_site = InlineKeyboardButton(text='Нашият уебсайт', url='https://redop.netlify.app',
                                          callback_data='our_site')
    kb_button_channel = InlineKeyboardButton(text='Нашият канал', url='https://t.me/official_redop',
                                             callback_data='our_channel')
    kb_button_change_language = InlineKeyboardButton(text='Промяна на езика', callback_data='change_language')
    kb_button_captcha = InlineKeyboardButton(text='Промяна на captcha', callback_data='settings_captcha')
    kb_start.add(kb_button_invite_chat, kb_button_channel)
    kb_start.add(kb_button_site, kb_button_commands)
    kb_start.add(kb_button_change_language)
    kb_start.add(kb_button_captcha)

    user_name = call.values['from']['first_name']
    user_id = call.values['from']['id']
    try:
        database.update_user_language(id_user=user_id, language='bulg')
    except Exception as ex:
        database.check_user_who_in_all_users(id_user=user_id, first_name=user_name, language='bulg')
    await call.message.answer(f"""Redop е иновативно антиспам решение за Telegram. Ботът подканва всеки нов потребител да извърши няколко действия в рамките на една минута. Нормалните потребители нямат проблеми да ги изпълнят, но той отказва достъп на злонамерени ботове. 

В момента ботът @Redop_AntiSpam_bot се поддържа от https://redop.netlify.app/.  

Ако имате някакви въпроси, винаги можете да потърсите помощ на нашия уебсайт или в контактите в описанието на бота. 

Нашите служители ще се радват да отговорят на всички ваши въпроси.

Оценяваме факта, че сте направили правилния избор за сигурността и модерирането на вашите групи в платформата Telegram.""")

    await call.message.answer("""
За да работите успешно с бота, трябва да:

1. Да добавите Redop към групата и да го назначите за администратор.

2. След като влезете в системата, ще видите списък с вашите групи, към които е добавен ботът Redop.
    """, reply_markup=kb_start)


@dp.callback_query_handler(text='hung')
async def choose_language_ru(call: types.CallbackQuery):
    database.check_user_who_in_all_users(id_user=call.from_user.id,
                                         first_name=call.from_user.first_name,
                                         language='hung')
    kb_start = InlineKeyboardMarkup(resize_keyboard=True)
    kb_button_commands = InlineKeyboardButton(text='Parancsok', callback_data='commands')
    kb_button_invite_chat = InlineKeyboardButton(text='Hozzáadás a chathez',
                                                 url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                 callback_data='invite_chat')
    kb_button_site = InlineKeyboardButton(text='Weboldalunk', url='https://redop.netlify.app', callback_data='our_site')
    kb_button_channel = InlineKeyboardButton(text='Csatornánk', url='https://t.me/official_redop',
                                             callback_data='our_channel')
    kb_button_change_language = InlineKeyboardButton(text='Nyelvváltás', callback_data='change_language')
    kb_button_captcha = InlineKeyboardButton(text='Captcha módosítása', callback_data='settings_captcha')
    kb_start.add(kb_button_invite_chat, kb_button_channel)
    kb_start.add(kb_button_site, kb_button_commands)
    kb_start.add(kb_button_change_language)
    kb_start.add(kb_button_captcha)

    user_name = call.values['from']['first_name']
    user_id = call.values['from']['id']
    try:
        database.update_user_language(id_user=user_id, language='hung')
    except Exception as ex:
        database.check_user_who_in_all_users(id_user=user_id, first_name=user_name, language='hung')
    await call.message.answer(f"""A Redop egy innovatív spamellenes megoldás a Telegram számára. A bot minden új felhasználót egy percen belül több művelet elvégzésére szólít fel. A normál felhasználóknak nem okoz gondot ezek elvégzése, de a rosszindulatú botoktól megtagadja a hozzáférést. 

A @Redop_AntiSpam_botot jelenleg a https://redop.netlify.app/ tartja fenn.  

Ha bármilyen kérdésed van, bármikor kérhetsz segítséget a weboldalunkon vagy a bot leírásában található elérhetőségeken. 

Munkatársaink szívesen válaszolnak minden kérdésére.

Nagyra értékeljük, hogy jó döntést hoztál a Telegram platformon lévő csoportjaid biztonsága és moderálása érdekében.""")

    await call.message.answer("""
A bot sikeres működéséhez a következőkre van szükséged:

1. Adja hozzá Redopot a csoporthoz, és nevezze ki adminisztrátornak.

2. Miután bejelentkeztél, látni fogod a csoportjaid listáját, amelyekhez a Redop botot hozzáadtad.
    """, reply_markup=kb_start)


@dp.callback_query_handler(text='catalan')
async def choose_language_ru(call: types.CallbackQuery):
    database.check_user_who_in_all_users(id_user=call.from_user.id,
                                         first_name=call.from_user.first_name,
                                         language='catalan')
    kb_start = InlineKeyboardMarkup(resize_keyboard=True)
    kb_button_commands = InlineKeyboardButton(text='Scopri cosa possiamo fare', callback_data='commands')
    kb_button_invite_chat = InlineKeyboardButton(text='Aggiungi alla chat',
                                                 url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                 callback_data='invite_chat')
    kb_button_site = InlineKeyboardButton(text='Sito web', url='https://redop.netlify.app', callback_data='our_site')
    kb_button_channel = InlineKeyboardButton(text='Il nostro canale', url='https://t.me/official_redop',
                                             callback_data='our_channel')
    kb_button_change_language = InlineKeyboardButton(text='Cambiare la lingua', callback_data='change_language')
    kb_button_captcha = InlineKeyboardButton(text='Impostazione CAPTCHA', callback_data='settings_captcha')
    kb_start.add(kb_button_invite_chat, kb_button_channel)
    kb_start.add(kb_button_site, kb_button_commands)
    kb_start.add(kb_button_change_language)
    kb_start.add(kb_button_captcha)

    user_name = call.values['from']['first_name']
    user_id = call.values['from']['id']
    try:
        database.update_user_language(id_user=user_id, language='catalan')
    except Exception as ex:
        database.check_user_who_in_all_users(id_user=user_id, first_name=user_name, language='catalan')
    await call.message.answer(f"""Redop es una innovadora solución antispam para Telegram. El bot pide a cada nuevo usuario que realice varias acciones en un minuto. Los usuarios normales no tienen problemas para completarlas, pero deniega el acceso a los bots maliciosos. 

El @Redop_AntiSpam_bot es mantenido actualmente por https://redop.netlify.app/.  

Si tienes alguna duda, siempre puedes pedir ayuda en nuestro sitio web o en los contactos de la descripción del bot. 

Nuestro personal estará encantado de responder a tus preguntas.

Apreciamos el hecho de que hayas hecho la elección correcta para la seguridad y moderación de tus grupos en la plataforma Telegram.""")

    await call.message.answer("""
Para trabajar con éxito con el bot, necesitas:

1. Añadir a Redop al grupo y nombrarlo administrador.

2. Una vez conectado, verás una lista de tus grupos a los que se ha añadido el bot Redop.
    """, reply_markup=kb_start)


@dp.callback_query_handler(text='turk')
async def choose_language_ru(call: types.CallbackQuery):
    database.check_user_who_in_all_users(id_user=call.from_user.id,
                                         first_name=call.from_user.first_name,
                                         language='turk')
    kb_start = InlineKeyboardMarkup(resize_keyboard=True)
    kb_button_commands = InlineKeyboardButton(text='Komutlar', callback_data='commands')
    kb_button_invite_chat = InlineKeyboardButton(text='Sohbete ekle',
                                                 url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                 callback_data='invite_chat')
    kb_button_site = InlineKeyboardButton(text='Web sitemiz', url='https://redop.netlify.app',
                                          callback_data='our_site')
    kb_button_channel = InlineKeyboardButton(text='Bizim kanalımız', url='https://t.me/official_redop',
                                             callback_data='our_channel')
    kb_button_change_language = InlineKeyboardButton(text='Dili değiştir', callback_data='change_language')
    kb_button_captcha = InlineKeyboardButton(text='Captcha yı değiştir', callback_data='settings_captcha')
    kb_start.add(kb_button_invite_chat, kb_button_channel)
    kb_start.add(kb_button_site, kb_button_commands)
    kb_start.add(kb_button_change_language)
    kb_start.add(kb_button_captcha)

    user_name = call.values['from']['first_name']
    user_id = call.values['from']['id']
    try:
        database.update_user_language(id_user=user_id, language='turk')
    except Exception as ex:
        database.check_user_who_in_all_users(id_user=user_id, first_name=user_name, language='turk')
    await call.message.answer(f"""Redop, Telegram için yenilikçi bir anti-spam çözümüdür. Bot, her yeni kullanıcıdan bir dakika içinde birkaç eylem gerçekleştirmesini ister. Normal kullanıcılar bunları tamamlamakta sorun yaşamaz, ancak kötü niyetli botlara erişimi engeller. 

Redop_AntiSpam_bot şu anda https://redop.netlify.app/ tarafından korunmaktadır.  

Herhangi bir sorunuz varsa, web sitemizden veya bot açıklamasındaki iletişim bölümünden her zaman yardım isteyebilirsiniz. 

Personelimiz sorularınızı yanıtlamaktan mutluluk duyacaktır.

Telegram platformundaki gruplarınızın güvenliği ve denetimi için doğru seçimi yaptığınız için teşekkür ederiz.""")

    await call.message.answer("""
Bot ile başarılı bir şekilde çalışmak için yapmanız gerekenler

1. Redop'u gruba ekleyin ve onu yönetici olarak atayın.

2. Giriş yaptıktan sonra, Redop botunun eklendiği gruplarınızın bir listesini göreceksiniz.
""", reply_markup=kb_start)


@dp.callback_query_handler(text='czech')
async def choose_language_ru(call: types.CallbackQuery):
    database.check_user_who_in_all_users(id_user=call.from_user.id,
                                         first_name=call.from_user.first_name,
                                         language='czech')
    kb_start = InlineKeyboardMarkup(resize_keyboard=True)
    kb_button_commands = InlineKeyboardButton(text='Příkazy', callback_data='commands')
    kb_button_invite_chat = InlineKeyboardButton(text='Přidat do chatu',
                                                 url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                 callback_data='invite_chat')
    kb_button_site = InlineKeyboardButton(text='Naše webové stránky', url='https://redop.netlify.app',
                                          callback_data='our_site')
    kb_button_channel = InlineKeyboardButton(text='Náš kanál', url='https://t.me/official_redop',
                                             callback_data='our_channel')
    kb_button_change_language = InlineKeyboardButton(text='Změnit jazyk', callback_data='change_language')
    kb_button_captcha = InlineKeyboardButton(text='Změna captcha', callback_data='settings_captcha')
    kb_start.add(kb_button_invite_chat, kb_button_channel)
    kb_start.add(kb_button_site, kb_button_commands)
    kb_start.add(kb_button_change_language)
    kb_start.add(kb_button_captcha)

    user_name = call.values['from']['first_name']
    user_id = call.values['from']['id']
    try:
        database.update_user_language(id_user=user_id, language='czech')
    except Exception as ex:
        database.check_user_who_in_all_users(id_user=user_id, first_name=user_name, language='czech')
    await call.message.answer(f"""Redop je inovativní antispamové řešení pro Telegram. Bot vyzve každého nového uživatele, aby během jedné minuty provedl několik akcí. Běžní uživatelé nemají problém s jejich dokončením, ale škodlivým botům zamezí přístup. 

O @Redop_AntiSpam_bot se v současné době stará https://redop.netlify.app/.  

V případě jakýchkoli dotazů můžete kdykoli požádat o pomoc na našich webových stránkách nebo v kontaktech v popisu bota. 

Naši zaměstnanci vám rádi zodpoví všechny vaše dotazy.

Vážíme si toho, že jste se rozhodli správně pro zabezpečení a moderování svých skupin na platformě Telegram.""")

    await call.message.answer("""
Pro úspěšnou práci s botem je třeba:

1. Přidat Redopa do skupiny a jmenovat ho správcem.

2. Po přihlášení se zobrazí seznam vašich skupin, do kterých byl bot Redop přidán.
""", reply_markup=kb_start)


@dp.callback_query_handler(text='kor')
async def choose_language_ru(call: types.CallbackQuery):
    database.check_user_who_in_all_users(id_user=call.from_user.id,
                                         first_name=call.from_user.first_name,
                                         language='kor')
    kb_start = InlineKeyboardMarkup(resize_keyboard=True)
    kb_button_commands = InlineKeyboardButton(text='명령어', callback_data='commands')
    kb_button_invite_chat = InlineKeyboardButton(text='채팅에 추가하기',
                                                 url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                 callback_data='invite_chat')
    kb_button_site = InlineKeyboardButton(text='웹사이트', url='https://redop.netlify.app',
                                          callback_data='our_site')
    kb_button_channel = InlineKeyboardButton(text='채널', url='https://t.me/official_redop',
                                             callback_data='our_channel')
    kb_button_change_language = InlineKeyboardButton(text='언어 변경', callback_data='change_language')
    kb_button_captcha = InlineKeyboardButton(text='언어 변경', callback_data='settings_captcha')
    kb_start.add(kb_button_invite_chat, kb_button_channel)
    kb_start.add(kb_button_site, kb_button_commands)
    kb_start.add(kb_button_change_language)
    kb_start.add(kb_button_captcha)

    user_name = call.values['from']['first_name']
    user_id = call.values['from']['id']
    try:
        database.update_user_language(id_user=user_id, language='kor')
    except Exception as ex:
        database.check_user_who_in_all_users(id_user=user_id, first_name=user_name, language='kor')
    await call.message.answer(f"""Redop은 텔레그램을 위한 혁신적인 스팸 방지 솔루션입니다. 이 봇은 새로운 사용자에게 1분 이내에 몇 가지 작업을 수행하라는 메시지를 띄웁니다. 일반 사용자들은 이 작업을 완료하는데 문제가 없지만, 악성 봇에 대한 접근은 거부합니다. 

Redop_AntiSpam_봇은 현재 https://redop.netlify.app/ 에서 관리하고 있습니다.  

궁금한 점이 있으면 언제든지 트위터 웹사이트나 봇 설명에 있는 연락처로 도움을 요청할 수 있습니다. 

저희 직원이 기꺼이 질문에 답변해 드리겠습니다.

텔레그램 플랫폼에서 그룹의 보안과 관리를 위해 올바른 선택을 해주셔서 감사합니다.""")

    await call.message.answer("""
봇을 성공적으로 사용하려면, 다음을 수행해야 합니다:

1. Redop을 그룹에 추가하고, 그를 관리자로 지정합니다.

2. 로그인하면, 레드돕 봇이 추가된 그룹 목록이 표시됩니다.
""", reply_markup=kb_start)


@dp.callback_query_handler(text='fren')
async def choose_language_ru(call: types.CallbackQuery):
    database.check_user_who_in_all_users(id_user=call.from_user.id,
                                         first_name=call.from_user.first_name,
                                         language='fren')
    kb_start = InlineKeyboardMarkup(resize_keyboard=True)
    kb_button_commands = InlineKeyboardButton(text='Commandes', callback_data='commands')
    kb_button_invite_chat = InlineKeyboardButton(text='Ajouter au chat',
                                                 url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                 callback_data='invite_chat')
    kb_button_site = InlineKeyboardButton(text='Notre site web', url='https://redop.netlify.app',
                                          callback_data='our_site')
    kb_button_channel = InlineKeyboardButton(text='Notre chaîne', url='https://t.me/official_redop',
                                             callback_data='our_channel')
    kb_button_change_language = InlineKeyboardButton(text='Changer de langue', callback_data='change_language')
    kb_button_captcha = InlineKeyboardButton(text='Changer de captcha', callback_data='settings_captcha')
    kb_start.add(kb_button_invite_chat, kb_button_channel)
    kb_start.add(kb_button_site, kb_button_commands)
    kb_start.add(kb_button_change_language)
    kb_start.add(kb_button_captcha)

    user_name = call.values['from']['first_name']
    user_id = call.values['from']['id']
    try:
        database.update_user_language(id_user=user_id, language='fren')
    except Exception as ex:
        database.check_user_who_in_all_users(id_user=user_id, first_name=user_name, language='fren')
    await call.message.answer(f"""Redop est une solution anti-spam innovante pour Telegram. Le robot demande à chaque nouvel utilisateur d'effectuer plusieurs actions en une minute. Les utilisateurs normaux n'ont aucun mal à les accomplir, mais il refuse l'accès aux bots malveillants. 

Le @Redop_AntiSpam_bot est actuellement maintenu par https://redop.netlify.app/.  

Si vous avez des questions, vous pouvez toujours demander de l'aide sur notre site Web ou dans les contacts figurant dans la description du bot. 

Notre personnel se fera un plaisir de répondre à toutes vos questions.

Nous apprécions le fait que vous ayez fait le bon choix pour la sécurité et la modération de vos groupes sur la plateforme Telegram.""")

    await call.message.answer("""
Pour travailler avec succès avec le bot, vous devez :

1. Ajouter Redop au groupe et le nommer en tant qu'administrateur.

2. Une fois connecté, vous verrez une liste de vos groupes auxquels Redop bot a été ajouté.
""", reply_markup=kb_start)


@dp.callback_query_handler(text='deu')
async def choose_language_ru(call: types.CallbackQuery):
    database.check_user_who_in_all_users(id_user=call.from_user.id,
                                         first_name=call.from_user.first_name,
                                         language='deu')
    kb_start = InlineKeyboardMarkup(resize_keyboard=True)
    kb_button_commands = InlineKeyboardButton(text='Befehle', callback_data='commands')
    kb_button_invite_chat = InlineKeyboardButton(text='Zum Chat hinzufügen',
                                                 url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                 callback_data='invite_chat')
    kb_button_site = InlineKeyboardButton(text='Unser Standort', url='https://redop.netlify.app',
                                          callback_data='our_site')
    kb_button_channel = InlineKeyboardButton(text='Unser Kanal', url='https://t.me/official_redop',
                                             callback_data='our_channel')
    kb_button_change_language = InlineKeyboardButton(text='Sprache ändern', callback_data='change_language')
    kb_button_captcha = InlineKeyboardButton(text='Captcha ändern', callback_data='settings_captcha')
    kb_start.add(kb_button_invite_chat, kb_button_channel)
    kb_start.add(kb_button_site, kb_button_commands)
    kb_start.add(kb_button_change_language)
    kb_start.add(kb_button_captcha)

    user_name = call.values['from']['first_name']
    user_id = call.values['from']['id']
    try:
        database.update_user_language(id_user=user_id, language='deu')
    except Exception as ex:
        database.check_user_who_in_all_users(id_user=user_id, first_name=user_name, language='deu')
    await call.message.answer(f"""Redop ist eine innovative Anti-Spam-Lösung für Telegram. Der Bot fordert jeden neuen Benutzer auf, innerhalb einer Minute mehrere Aktionen durchzuführen. Normale Benutzer haben keine Probleme, diese auszuführen, aber bösartigen Bots wird der Zugang verweigert. 

Der @Redop_AntiSpam_bot wird derzeit von https://redop.netlify.app/ betreut.  

Wenn Sie Fragen haben, können Sie jederzeit auf unserer Website oder unter Kontakte in der Bot-Beschreibung um Hilfe bitten. 

Unsere Mitarbeiter werden Ihnen gerne alle Fragen beantworten.

Wir freuen uns, dass Sie die richtige Wahl für die Sicherheit und Moderation Ihrer Gruppen auf der Telegram-Plattform getroffen haben.""")

    await call.message.answer("""
Um erfolgreich mit dem Bot arbeiten zu können, müssen Sie:

1. Fügen Sie Redop zu der Gruppe hinzu und ernennen Sie ihn zum Administrator.

2. Sobald Sie eingeloggt sind, sehen Sie eine Liste Ihrer Gruppen, zu denen der Redop-Bot hinzugefügt wurde.
""", reply_markup=kb_start)


@dp.callback_query_handler(text='chin')
async def choose_language_ru(call: types.CallbackQuery):
    database.check_user_who_in_all_users(id_user=call.from_user.id,
                                         first_name=call.from_user.first_name,
                                         language='chin')
    kb_start = InlineKeyboardMarkup(resize_keyboard=True)
    kb_button_commands = InlineKeyboardButton(text='命令', callback_data='commands')
    kb_button_invite_chat = InlineKeyboardButton(text='添加到聊天中',
                                                 url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                 callback_data='invite_chat')
    kb_button_site = InlineKeyboardButton(text='我们的网站', url='https://redop.netlify.app', callback_data='our_site')
    kb_button_channel = InlineKeyboardButton(text='我们的渠道', url='https://t.me/official_redop',
                                             callback_data='our_channel')
    kb_button_change_language = InlineKeyboardButton(text='改变语言', callback_data='change_language')
    kb_button_captcha = InlineKeyboardButton(text='更改验证码', callback_data='settings_captcha')
    kb_start.add(kb_button_invite_chat, kb_button_channel)
    kb_start.add(kb_button_site, kb_button_commands)
    kb_start.add(kb_button_change_language)
    kb_start.add(kb_button_captcha)

    user_name = call.values['from']['first_name']
    user_id = call.values['from']['id']
    try:
        database.update_user_language(id_user=user_id, language='chin')
    except Exception as ex:
        database.check_user_who_in_all_users(id_user=user_id, first_name=user_name, language='chin')
    await call.message.answer(f"""Redop是Telegram的一个创新反垃圾邮件解决方案。该机器人提示每个新用户在一分钟内执行几个动作。正常用户完成这些动作没有问题，但它拒绝了恶意机器人的访问。

@Redop_AntiSpam_bot 目前由 https://redop.netlify.app/ 

如果你有任何问题，你可以随时在我们的网站或机器人描述中的联系人中寻求帮助。

我们的工作人员将很乐意回答您的任何问题。

我们感谢你为Telegram平台上的群组的安全和管理做出的正确选择。""")

    await call.message.answer("""
要成功使用机器人，你需要： 1:

1. 将Redop添加到群组并任命他为管理员。

2. 2. 登录后，你将看到你的群组列表，其中Redop机器人已被添加到其中。
""", reply_markup=kb_start)


@dp.callback_query_handler(text='port_bras')
async def choose_language_ru(call: types.CallbackQuery):
    database.check_user_who_in_all_users(id_user=call.from_user.id,
                                         first_name=call.from_user.first_name,
                                         language='port_bras')
    kb_start = InlineKeyboardMarkup(resize_keyboard=True)
    kb_button_commands = InlineKeyboardButton(text='Comandos', callback_data='commands')
    kb_button_invite_chat = InlineKeyboardButton(text='Adicionar ao bate-papo',
                                                 url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                 callback_data='invite_chat')
    kb_button_site = InlineKeyboardButton(text='Nosso site', url='https://redop.netlify.app', callback_data='our_site')
    kb_button_channel = InlineKeyboardButton(text='Nosso canal', url='https://t.me/official_redop',
                                             callback_data='our_channel')
    kb_button_change_language = InlineKeyboardButton(text='Mudar o idioma', callback_data='change_language')
    kb_button_captcha = InlineKeyboardButton(text='Mudança captcha', callback_data='settings_captcha')
    kb_start.add(kb_button_invite_chat, kb_button_channel)
    kb_start.add(kb_button_site, kb_button_commands)
    kb_start.add(kb_button_change_language)
    kb_start.add(kb_button_captcha)

    user_name = call.values['from']['first_name']
    user_id = call.values['from']['id']
    try:
        database.update_user_language(id_user=user_id, language='port_bras')
    except Exception as ex:
        database.check_user_who_in_all_users(id_user=user_id, first_name=user_name, language='port_bras')
    await call.message.answer(f"""Redop é uma solução inovadora anti-spam para Telegramas. O robô solicita que cada novo usuário execute várias ações em um minuto. Usuários normais não têm dificuldade em completá-las, mas nega o acesso a bots maliciosos. 

O @Redop_AntiSpam_bot é atualmente mantido por https://redop.netlify.app/.  

Se você tiver alguma dúvida, você pode sempre pedir ajuda em nosso site ou em contatos na descrição do bot. 

Nossa equipe ficará feliz em responder a quaisquer perguntas que você possa ter.

Agradecemos o fato de você ter feito a escolha certa para a segurança e moderação de seus grupos na plataforma Telegramas.""")

    await call.message.answer("""
Para trabalhar com sucesso com o bot, você precisa fazê-lo:

1. Adicionar o Redop ao grupo e nomeá-lo como administrador.

2. Uma vez logado, você verá uma lista de seus grupos aos quais o bot Redop foi adicionado.
""", reply_markup=kb_start)


@dp.callback_query_handler(text='eesti')
async def choose_language_ru(call: types.CallbackQuery):
    database.check_user_who_in_all_users(id_user=call.from_user.id,
                                         first_name=call.from_user.first_name,
                                         language='eesti')
    kb_start = InlineKeyboardMarkup(resize_keyboard=True)
    kb_button_commands = InlineKeyboardButton(text='Käsklused', callback_data='commands')
    kb_button_invite_chat = InlineKeyboardButton(text='Lisa vestlusesse',
                                                 url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                 callback_data='invite_chat')
    kb_button_site = InlineKeyboardButton(text='Meie veebileht', url='https://redop.netlify.app',
                                          callback_data='our_site')
    kb_button_channel = InlineKeyboardButton(text='Meie kanal', url='https://t.me/official_redop',
                                             callback_data='our_channel')
    kb_button_change_language = InlineKeyboardButton(text='Keele muutmine', callback_data='change_language')
    kb_button_captcha = InlineKeyboardButton(text='Muuda captcha', callback_data='settings_captcha')
    kb_start.add(kb_button_invite_chat, kb_button_channel)
    kb_start.add(kb_button_site, kb_button_commands)
    kb_start.add(kb_button_change_language)
    kb_start.add(kb_button_captcha)

    user_name = call.values['from']['first_name']
    user_id = call.values['from']['id']
    try:
        database.update_user_language(id_user=user_id, language='eesti')
    except Exception as ex:
        database.check_user_who_in_all_users(id_user=user_id, first_name=user_name, language='eesti')
    await call.message.answer(f"""Redop on uuenduslik spämmivastane lahendus Telegrami jaoks. Bot palub igal uuel kasutajal ühe minuti jooksul teha mitmeid toiminguid. Tavalistel kasutajatel ei ole probleeme nende täitmisega, kuid see keelab juurdepääsu pahatahtlikele botidele. 

@Redop_AntiSpam_bot'i hooldab praegu https://redop.netlify.app/.  

Kui teil on küsimusi, võite alati küsida abi meie veebisaidil või boti kirjelduses olevatest kontaktidest. 

Meie töötajad vastavad hea meelega teie küsimustele.

Me hindame seda, et olete teinud õige valiku oma rühmade turvalisuse ja modereerimise kohta Telegrami platvormil.""")

    await call.message.answer("""
Botiga edukaks töötamiseks peate:

1. Lisage Redop gruppi ja määrake ta administraatoriks.

2. Kui olete sisse loginud, näete oma rühmade nimekirja, kuhu Redop bot on lisatud.
""", reply_markup=kb_start)


@dp.callback_query_handler(text='fin')
async def choose_language_ru(call: types.CallbackQuery):
    database.check_user_who_in_all_users(id_user=call.from_user.id,
                                         first_name=call.from_user.first_name,
                                         language='fin')
    kb_start = InlineKeyboardMarkup(resize_keyboard=True)
    kb_button_commands = InlineKeyboardButton(text='Komennot', callback_data='commands')
    kb_button_invite_chat = InlineKeyboardButton(text='Lisää keskusteluun',
                                                 url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                 callback_data='invite_chat')
    kb_button_site = InlineKeyboardButton(text='Verkkosivustomme', url='https://redop.netlify.app',
                                          callback_data='our_site')
    kb_button_channel = InlineKeyboardButton(text='Kanavamme', url='https://t.me/official_redop',
                                             callback_data='our_channel')
    kb_button_change_language = InlineKeyboardButton(text='Vaihda kieli', callback_data='change_language')
    kb_button_captcha = InlineKeyboardButton(text='Vaihda captcha', callback_data='settings_captcha')
    kb_start.add(kb_button_invite_chat, kb_button_channel)
    kb_start.add(kb_button_site, kb_button_commands)
    kb_start.add(kb_button_change_language)
    kb_start.add(kb_button_captcha)

    user_name = call.values['from']['first_name']
    user_id = call.values['from']['id']
    try:
        database.update_user_language(id_user=user_id, language='fin')
    except Exception as ex:
        database.check_user_who_in_all_users(id_user=user_id, first_name=user_name, language='fin')
    await call.message.answer(f"""Redop on innovatiivinen roskapostinestoratkaisu Telegramille. Botti kehottaa jokaista uutta käyttäjää suorittamaan joukon toimenpiteitä yhden minuutin kuluessa. Normaaleilla käyttäjillä ei ole ongelmia suorittaa niitä, mutta se estää pääsyn haitallisilta boteilta. 

@Redop_AntiSpam_botti on tällä hetkellä https://redop.netlify.app/ ylläpitämä.  

Jos sinulla on kysyttävää, voit aina pyytää apua verkkosivustollamme tai botin kuvauksessa olevien yhteystietojen avulla. 

Henkilökuntamme vastaa mielellään kysymyksiisi.

Arvostamme sitä, että olet tehnyt oikean valinnan Telegram-alustan ryhmienne turvallisuuden ja moderoinnin suhteen.""")

    await call.message.answer("""
Jotta voisit työskennellä onnistuneesti botin kanssa, sinun on:

1. Lisää Redop ryhmään ja määritä hänet ylläpitäjäksi.

2. Kun olet kirjautunut sisään, näet luettelon ryhmistäsi, joihin Redop-botti on lisätty.
""", reply_markup=kb_start)


@dp.callback_query_handler(text='slov')
async def choose_language_ru(call: types.CallbackQuery):
    database.check_user_who_in_all_users(id_user=call.from_user.id,
                                         first_name=call.from_user.first_name,
                                         language='slov')
    kb_start = InlineKeyboardMarkup(resize_keyboard=True)
    kb_button_commands = InlineKeyboardButton(text='Príkazy', callback_data='commands')
    kb_button_invite_chat = InlineKeyboardButton(text='Pridať do chatu',
                                                 url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                 callback_data='invite_chat')
    kb_button_site = InlineKeyboardButton(text='Naša webová stránka', url='https://redop.netlify.app',
                                          callback_data='our_site')
    kb_button_channel = InlineKeyboardButton(text='Náš kanál', url='https://t.me/official_redop',
                                             callback_data='our_channel')
    kb_button_change_language = InlineKeyboardButton(text='zmeniť jazyk', callback_data='change_language')
    kb_button_captcha = InlineKeyboardButton(text='zmeniť captcha', callback_data='settings_captcha')
    kb_start.add(kb_button_invite_chat, kb_button_channel)
    kb_start.add(kb_button_site, kb_button_commands)
    kb_start.add(kb_button_change_language)
    kb_start.add(kb_button_captcha)

    user_name = call.values['from']['first_name']
    user_id = call.values['from']['id']
    try:
        database.update_user_language(id_user=user_id, language='slov')
    except Exception as ex:
        database.check_user_who_in_all_users(id_user=user_id, first_name=user_name, language='slov')
    await call.message.answer(f"""Redop je inovatívne antispamové riešenie pre Telegram. Bot vyzve každého nového používateľa, aby v priebehu jednej minúty vykonal sériu akcií. Bežní používatelia nemajú problém s ich dokončením, ale škodlivým botom odopiera prístup. 

V súčasnosti je @Redop_AntiSpam_bot udržiavaný na stránke https://redop.netlify.app/.  

V prípade akýchkoľvek otázok môžete vždy požiadať o pomoc pomocou kontaktných údajov na našej webovej stránke alebo v popise bota. 

Naši pracovníci vám radi odpovedia na vaše otázky.

Oceňujeme, že ste sa rozhodli správne, pokiaľ ide o bezpečnosť a moderovanie vašich skupín na platforme Telegram.""")

    await call.message.answer("""
Aby ste mohli s botom úspešne pracovať, musíte:

1. Pridať Redop do skupiny a priradiť ho ako správcu.

2. Po prihlásení sa zobrazí zoznam vašich skupín, do ktorých bol pridaný bot Redop.
""", reply_markup=kb_start)


@dp.callback_query_handler(text='rom')
async def choose_language_ru(call: types.CallbackQuery):
    database.check_user_who_in_all_users(id_user=call.from_user.id,
                                         first_name=call.from_user.first_name,
                                         language='rom')
    kb_start = InlineKeyboardMarkup(resize_keyboard=True)
    kb_button_commands = InlineKeyboardButton(text='Comenzi', callback_data='commands')
    kb_button_invite_chat = InlineKeyboardButton(text='Adăugați la chat',
                                                 url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                 callback_data='invite_chat')
    kb_button_site = InlineKeyboardButton(text='Site-ul nostru', url='https://redop.netlify.app',
                                          callback_data='our_site')
    kb_button_channel = InlineKeyboardButton(text='Canalul nostru', url='https://t.me/official_redop',
                                             callback_data='our_channel')
    kb_button_change_language = InlineKeyboardButton(text='Schimbați limba', callback_data='change_language')
    kb_button_captcha = InlineKeyboardButton(text='Schimbați captcha', callback_data='settings_captcha')
    kb_start.add(kb_button_invite_chat, kb_button_channel)
    kb_start.add(kb_button_site, kb_button_commands)
    kb_start.add(kb_button_change_language)
    kb_start.add(kb_button_captcha)

    user_name = call.values['from']['first_name']
    user_id = call.values['from']['id']
    try:
        database.update_user_language(id_user=user_id, language='rom')
    except Exception as ex:
        database.check_user_who_in_all_users(id_user=user_id, first_name=user_name, language='rom')
    await call.message.answer(f"""Redop este o soluție anti-spam inovatoare pentru Telegram. Robotul solicită fiecărui utilizator nou să efectueze o serie de acțiuni în decurs de un minut. Utilizatorii obișnuiți nu au nicio problemă în a le finaliza, dar refuză accesul roboților rău intenționați. 

@Redop_AntiSpam_bot este întreținut în prezent de https://redop.netlify.app/.  

Dacă aveți întrebări, puteți oricând să cereți ajutor folosind datele de contact de pe site-ul nostru sau din descrierea botului. 

Personalul nostru va fi bucuros să vă răspundă la întrebări.

Apreciem că ați făcut alegerea corectă în ceea ce privește securitatea și moderarea grupurilor dvs. pe platforma Telegram.""")

    await call.message.answer("""
Pentru a lucra cu succes cu botul, trebuie să:

1. Adăugați Redop la grup și atribuiți-i funcția de administrator.

2. După ce vă conectați, veți vedea o listă a grupurilor dvs. la care a fost adăugat botul Redop.
""", reply_markup=kb_start)


@dp.callback_query_handler(text='ind')
async def choose_language_ru(call: types.CallbackQuery):
    database.check_user_who_in_all_users(id_user=call.from_user.id,
                                         first_name=call.from_user.first_name,
                                         language='ind')
    kb_start = InlineKeyboardMarkup(resize_keyboard=True)
    kb_button_commands = InlineKeyboardButton(text='Perintah', callback_data='commands')
    kb_button_invite_chat = InlineKeyboardButton(text='Tambahkan ke obrolan',
                                                 url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                 callback_data='invite_chat')
    kb_button_site = InlineKeyboardButton(text='Situs web kami', url='https://redop.netlify.app',
                                          callback_data='our_site')
    kb_button_channel = InlineKeyboardButton(text='Saluran kami', url='https://t.me/official_redop',
                                             callback_data='our_channel')
    kb_button_change_language = InlineKeyboardButton(text='Mengubah bahasa', callback_data='change_language')
    kb_button_captcha = InlineKeyboardButton(text='Ubah captcha', callback_data='settings_captcha')
    kb_start.add(kb_button_invite_chat, kb_button_channel)
    kb_start.add(kb_button_site, kb_button_commands)
    kb_start.add(kb_button_change_language)
    kb_start.add(kb_button_captcha)

    user_name = call.values['from']['first_name']
    user_id = call.values['from']['id']
    try:
        database.update_user_language(id_user=user_id, language='ind')
    except Exception as ex:
        database.check_user_who_in_all_users(id_user=user_id, first_name=user_name, language='ind')
    await call.message.answer(f"""Redop adalah solusi anti-spam yang inovatif untuk Telegram. Bot ini meminta setiap pengguna baru untuk melakukan serangkaian tindakan dalam waktu satu menit. Pengguna normal tidak memiliki masalah dalam menyelesaikannya, tetapi bot ini menolak akses ke bot jahat. 

Bot @Redop_AntiSpam_bot saat ini dikelola oleh https://redop.netlify.app/.  

Jika Anda memiliki pertanyaan, Anda selalu dapat meminta bantuan dengan menggunakan detail kontak di situs web kami atau dalam deskripsi bot. 

Staf kami akan dengan senang hati menjawab pertanyaan Anda.

Kami menghargai bahwa Anda telah membuat pilihan yang tepat tentang keamanan dan moderasi grup Anda di platform Telegram.""")

    await call.message.answer("""
Agar berhasil bekerja dengan bot, Anda perlu:

1. Tambahkan Redop ke grup dan tetapkan dia sebagai administrator.

2. Setelah Anda masuk, Anda akan melihat daftar grup Anda di mana bot Redop telah ditambahkan.
""", reply_markup=kb_start)


@dp.callback_query_handler(text='norw')
async def choose_language_ru(call: types.CallbackQuery):
    database.check_user_who_in_all_users(id_user=call.from_user.id,
                                         first_name=call.from_user.first_name,
                                         language='norw')
    kb_start = InlineKeyboardMarkup(resize_keyboard=True)
    kb_button_commands = InlineKeyboardButton(text='Finn ut hva vi kan gjøre', callback_data='commands')
    kb_button_invite_chat = InlineKeyboardButton(text='Legg til i chat',
                                                 url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                 callback_data='invite_chat')
    kb_button_site = InlineKeyboardButton(text='Vår nettside', url='https://redop.netlify.app',
                                          callback_data='our_site')
    kb_button_channel = InlineKeyboardButton(text='Vår kanal', url='https://t.me/official_redop',
                                             callback_data='our_channel')
    kb_button_change_language = InlineKeyboardButton(text='Endre språk', callback_data='change_language')
    kb_button_captcha = InlineKeyboardButton(text='Endre captchaen', callback_data='settings_captcha')
    kb_start.add(kb_button_invite_chat, kb_button_channel)
    kb_start.add(kb_button_site, kb_button_commands)
    kb_start.add(kb_button_change_language)
    kb_start.add(kb_button_captcha)

    user_name = call.values['from']['first_name']
    user_id = call.values['from']['id']
    try:
        database.update_user_language(id_user=user_id, language='norw')
    except Exception as ex:
        database.check_user_who_in_all_users(id_user=user_id, first_name=user_name, language='norw')
    await call.message.answer(f"""Redop er en innovativ anti-spam-løsning for Telegram. Boten ber hver nye bruker om å utføre en rekke handlinger i løpet av ett minutt. Vanlige brukere har ingen problemer med å fullføre dem, men det nekter tilgang til ondsinnede roboter. 

@Redop_AntiSpam_bot vedlikeholdes for tiden av https://redop.netlify.app/.  

Hvis du har spørsmål, kan du alltid be om hjelp ved å bruke kontaktinformasjonen på nettstedet vårt eller i botbeskrivelsen. 

Våre ansatte svarer gjerne på spørsmålene dine.

Vi setter pris på at du har tatt det riktige valget når det gjelder sikkerhet og moderering av gruppene dine på Telegram-plattformen.""")

    await call.message.answer("""
For å jobbe vellykket med boten, må du:

1. legge Redop til gruppen og tilordne ham som administrator.

2. Når du er logget inn, vil du se en liste over gruppene dine som Redop-boten er lagt til.
""", reply_markup=kb_start)


@dp.callback_query_handler(text='esp')
async def choose_language_ru(call: types.CallbackQuery):
    database.check_user_who_in_all_users(id_user=call.from_user.id,
                                         first_name=call.from_user.first_name,
                                         language='esp')
    kb_start = InlineKeyboardMarkup(resize_keyboard=True)
    kb_button_commands = InlineKeyboardButton(text='Descubra lo que podemos hacer', callback_data='commands')
    kb_button_invite_chat = InlineKeyboardButton(text='Añadir al chat',
                                                 url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                 callback_data='invite_chat')
    kb_button_site = InlineKeyboardButton(text='Nuestro sitio web', url='https://redop.netlify.app',
                                          callback_data='our_site')
    kb_button_channel = InlineKeyboardButton(text='Nuestro canal', url='https://t.me/official_redop',
                                             callback_data='our_channel')
    kb_button_change_language = InlineKeyboardButton(text='Cambiar el idioma', callback_data='change_language')
    kb_button_captcha = InlineKeyboardButton(text='Configuración de Captcha', callback_data='settings_captcha')
    kb_start.add(kb_button_invite_chat, kb_button_channel)
    kb_start.add(kb_button_site, kb_button_commands)
    kb_start.add(kb_button_change_language)
    kb_start.add(kb_button_captcha)

    user_name = call.values['from']['first_name']
    user_id = call.values['from']['id']
    try:
        database.update_user_language(id_user=user_id, language='esp')
    except Exception as ex:
        database.check_user_who_in_all_users(id_user=user_id, first_name=user_name, language='esp')
    await call.message.answer(f"""Redop es una innovadora solución antispam para Telegram. El bot pide a cada nuevo usuario que realice una serie de acciones en un minuto. Los usuarios normales no tienen problemas para completarlas, pero deniega el acceso a los bots maliciosos. 

El @Redop_AntiSpam_bot está actualmente mantenido por https://redop.netlify.app/.  

Si tienes alguna duda, siempre puedes pedir ayuda utilizando los datos de contacto que aparecen en nuestro sitio web o en la descripción del bot. 

Nuestro personal estará encantado de responder a tus preguntas.

Apreciamos que hayas tomado la decisión correcta sobre la seguridad y moderación de tus grupos en la plataforma Telegram.""")

    await call.message.answer("""
Para trabajar con éxito con el bot, necesitas:

1. Añadir a Redop al grupo y asignarle como administrador.

2. Una vez que hayas iniciado sesión, verás una lista de tus grupos en los que se ha añadido el bot Redop.
""", reply_markup=kb_start)


@dp.callback_query_handler(text='it')
async def choose_language_ru(call: types.CallbackQuery):
    database.check_user_who_in_all_users(id_user=call.from_user.id,
                                         first_name=call.from_user.first_name,
                                         language='it')
    kb_start = InlineKeyboardMarkup(resize_keyboard=True)
    kb_button_commands = InlineKeyboardButton(text='Scopri cosa possiamo fare', callback_data='commands')
    kb_button_invite_chat = InlineKeyboardButton(text='Aggiungi alla chat',
                                                 url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                 callback_data='invite_chat')
    kb_button_site = InlineKeyboardButton(text='Sito web', url='https://redop.netlify.app', callback_data='our_site')
    kb_button_channel = InlineKeyboardButton(text='Il nostro canale', url='https://t.me/official_redop',
                                             callback_data='our_channel')
    kb_button_change_language = InlineKeyboardButton(text='Cambiare la lingua', callback_data='change_language')
    kb_button_captcha = InlineKeyboardButton(text='Impostazione CAPTCHA', callback_data='settings_captcha')
    kb_start.add(kb_button_invite_chat, kb_button_channel)
    kb_start.add(kb_button_site, kb_button_commands)
    kb_start.add(kb_button_change_language)
    kb_start.add(kb_button_captcha)

    user_name = call.values['from']['first_name']
    user_id = call.values['from']['id']
    try:
        database.update_user_language(id_user=user_id, language='it')
    except Exception as ex:
        database.check_user_who_in_all_users(id_user=user_id, first_name=user_name, language='it')
    await call.message.answer(f"""Redop è un'innovativa soluzione anti-spam per Telegram. Il bot chiede a ogni nuovo utente di eseguire una serie di azioni entro un minuto. Gli utenti normali non hanno problemi a completarle, ma nega l'accesso ai bot maligni. 

Il @Redop_AntiSpam_bot è attualmente gestito da https://redop.netlify.app/.  

Se avete domande, potete sempre chiedere aiuto utilizzando i dettagli di contatto sul nostro sito web o nella descrizione del bot. 

Il nostro personale sarà lieto di rispondere alle vostre domande.

Siamo lieti che abbiate fatto la scelta giusta per quanto riguarda la sicurezza e la moderazione dei vostri gruppi sulla piattaforma Telegram.""")

    await call.message.answer("""
Per poter lavorare con successo con il bot, è necessario che:

1. Aggiungere Redop al gruppo e assegnargli il ruolo di amministratore.

2. Una volta effettuato l'accesso, vedrete un elenco dei vostri gruppi in cui è stato aggiunto il bot Redop.
""", reply_markup=kb_start)


@dp.callback_query_handler(text='sa')
async def choose_language_ru(call: types.CallbackQuery):
    database.check_user_who_in_all_users(id_user=call.from_user.id,
                                         first_name=call.from_user.first_name,
                                         language='sa')
    kb_start = InlineKeyboardMarkup(resize_keyboard=True)
    kb_button_commands = InlineKeyboardButton(text='تعرف على قدرات الروبوت', callback_data='commands')
    kb_button_invite_chat = InlineKeyboardButton(text='إضافة دردشة   ',
                                                 url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                 callback_data='invite_chat')
    kb_button_site = InlineKeyboardButton(text='الموقع الإلكتروني   ', url='https://redop.netlify.app',
                                          callback_data='our_site')
    kb_button_channel = InlineKeyboardButton(text='قناتنا', url='https://t.me/official_redop',
                                             callback_data='our_channel')
    kb_button_change_language = InlineKeyboardButton(text='تغيير اللغة', callback_data='change_language')
    kb_button_captcha = InlineKeyboardButton(text='إعداد Captcha', callback_data='settings_captcha')
    kb_start.add(kb_button_invite_chat, kb_button_channel)
    kb_start.add(kb_button_site, kb_button_commands)
    kb_start.add(kb_button_change_language)
    kb_start.add(kb_button_captcha)

    user_name = call.values['from']['first_name']
    user_id = call.values['from']['id']
    try:
        database.update_user_language(id_user=user_id, language='sa')
    except Exception as ex:
        database.check_user_who_in_all_users(id_user=user_id, first_name=user_name, language='sa')
    await call.message.answer(f""" لمكافحة البريد العشوائي لـ Telegram. يطلب الروبوت من كل مستخدم جديد تنفيذ عدة إجراءات في غضون دقيقة واحدة. لن يواجه المستخدمون العاديون أي مشكلة في إكمالها ، لكنه سيمنع الوصول إلى برامج الروبوت الضارة.

تتم صيانةRedop_AntiSpam_bot حاليًا بواسطة https://redop.netlify.app/.

إذا كانت لديك أي أسئلة ، فيمكنك دائمًا طلب المساعدة من جهات الاتصال على موقعنا على الويب أو في وصف الروبوت.

سيكون موظفونا سعداء للإجابة على أسئلتك.

نحن نقدر أنك اتخذت القرار الصحيح فيما يتعلق بأمان مجموعاتك والاعتدال فيها على منصة Telegram.
""")

    await call.message.answer("""
للعمل بنجاح مع الروبوت ، يجب عليك:

1. أضف Redop إلى المجموعة واجعله مسؤولاً.

2. بمجرد تسجيل الدخول ، سترى قائمة بالمجموعات الخاصة بك حيث تمت إضافة روبوت Redop
""", reply_markup=kb_start)

# Все языки закончились.


class SendMessageChat(StatesGroup): # Функция, позволяющая корректно отправлять с подтверждением расссылку по чатам
    message = State()
    confirm = State()


@dp.message_handler(commands=['greeting']) # функция, позволяющая отвечать пользователю в случае пройденной каптчи (ON)
async def greeting_command(message: types.Message):
    chat_user = message.chat.id
    if chat_user < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        user_id_is_admin = user_admin['status']
        if user_id_is_admin != 'member':
            database.set_greeting_chat(id_chat=chat_user)
            await message.reply(text='Now after passing the captcha, the bot will welcome the user!')
        else:
            await message.reply(text='You do not have permission to do this!')

@dp.message_handler(commands=['ungreeting']) # функция, позволяющая отвечать пользователю в случае пройденной каптчи (OFF)
async def greeting_command(message: types.Message):
    chat_user = message.chat.id
    if chat_user < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        user_id_is_admin = user_admin['status']
        if user_id_is_admin != 'member':
            database.delete_entry_chat(id_chat=chat_user)
            await message.reply(text='Now after passing the captcha, the bot will not welcome the user!')
        else:
            await message.reply(text='You do not have permission to do this!')


@dp.message_handler(commands=['deleteEntryMessage']) # удалять сообщение о вступлении в чат человека (ON)
async def deleteentrymessage_command(message: types.Message):
    chat_user = message.chat.id
    if chat_user < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        user_id_is_admin = user_admin['status']
        if user_id_is_admin != 'member':
            database.set_entry_chat(id_chat=chat_user)
            await message.reply(text='Entry messages are now deleted!')
        else:
            await message.reply(text='You do not have permission to do this!')


@dp.message_handler(commands=['undeleteEntryMessage']) # удалять сообщение о вступлении в чат человека (OFF)
async def deleteentrymessage_command(message: types.Message):
    chat_user = message.chat.id
    if chat_user < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        user_id_is_admin = user_admin['status']
        if user_id_is_admin != 'member':
            database.delete_entry_chat(id_chat=chat_user)
            await message.reply(text='Entry messages are now not deleted!')
        else:
            await message.reply(text='You do not have permission to do this!')

@dp.message_handler(commands=['attackon']) # делает все команды бота недоступными пользователям
async def restrict_command(message: types.Message):
    chat_user = message.chat.id
    if chat_user < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        user_id_is_admin = user_admin['status']
        if user_id_is_admin == 'creator':
            database.set_attack_chat(id_chat=chat_user, status=True)
        else:
            await message.reply(text='You do not have permission to do this!')

@dp.message_handler(commands=['attackoff']) # делает все команды бота доступными пользователям (по умол.)
async def restrict_command(message: types.Message):
    chat_user = message.chat.id
    if chat_user < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        user_id_is_admin = user_admin['status']
        if user_id_is_admin == 'creator':
            database.set_attack_chat(id_chat=chat_user, status=False)
        else:
            await message.reply(text='You do not have permission to do this!')


@dp.message_handler(commands=['lock']) # функция, делающая команды бота доступными только админам
async def lock_command(message: types.Message):
    chat_user = message.chat.id
    if chat_user < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        check_attack = database.get_attack_chat(id_chat=chat_user)
        if check_attack[0][0] == True:
            pass
        else:
            user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            user_id_is_admin = user_admin['status']
            if user_id_is_admin != 'member':
                database.add_lock_chat(id_chat=chat_user)
                await message.reply('Now users will not be able to use user commands!')
            else:
                await message.reply(text='You do not have permission to do this!')


@dp.message_handler(commands=['unlock']) # аналог lock
async def lock_command(message: types.Message):
    chat_user = message.chat.id
    if chat_user < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        check_attack = database.get_attack_chat(id_chat=chat_user)
        if check_attack[0][0] == True:
            pass
        else:
            user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            user_id_is_admin = user_admin['status']
            if user_id_is_admin != 'member':
                database.delete_lock_chat(id_chat=chat_user)
                await message.reply('Now users will be able to use user commands!')
            else:
                await message.reply(text='You do not have permission to do this!')

@dp.message_handler(commands=['send_users']) # рассылка пользователям
async def send_chat_users(message: types.Message):
    if message.chat.id == id_send_users:
        await message.answer('Введите текст для рассылки')
        await SendMessageChat.message.set()
@dp.message_handler(state=SendMessageChat.message) # функция рассылки
async def sendmessagechat_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['message'] = message.text
    await message.answer('Вы уверены, что готовы сделать рассылку?'
                         'Текст рассылки:'
                         f'{data["message"]}\n'
                         '✅Если вы уверены, напишите "УВЕРЕН"✅')
    await SendMessageChat.confirm.set()

@dp.message_handler(state=SendMessageChat.confirm) # подтверждение рассылки
async def sendmessagechat_confirm(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['confirm'] = message.text
    if data['confirm'] == 'УВЕРЕН':
        chats_id = database.all_chats()
        for chat in chats_id:
            try:
                await bot.send_message(chat_id=int(chat[0]), text=data['message'])
            except Exception as ex:
                pass
        await state.finish()
    else:
        await message.answer('Слово, введенное вами не соответствует с ключевым словом!')
        await state.finish()

class CheckChannel(StatesGroup):
    username = State()

@dp.message_handler(commands=['warning']) # функция warning
async def warning_message(message: types.Message):
    chat_user = message.chat.id
    if chat_user < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        check_attack = database.get_attack_chat(id_chat=chat_user)
        if check_attack[0][0] == True:
            pass
        else:
            user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            user_id_is_admin = user_admin['status']
            if user_id_is_admin != 'member':
                database.warning_on(chat_id=chat_user)
                language_captcha = database.get_language_captcha(id_chat=message.chat.id)
                if language_captcha == []:

                    warning_access = await message.answer('Artificial Intelligence successfully activated ✅')
                    await message.answer("""Dear users, your safety is important to us, so we recommend you not to post your personal information, as well as any other information about yourself. 

Do not follow any third-party links that are not sent by the chat administrator.

Thank you for your attention and have a nice day!
""")
                    asyncio.create_task(delete_message(warning_message, 60))
                elif language_captcha[0][0] == 'ru':

                    warning_access = await message.answer('Искусственный интеллект успешно активирован ✅')
                    await message.answer("""Уважаемые пользователи, для нас важна ваша безопасность, поэтому мы рекомендуем вам не размещать свою личную информацию, а также любую другую информацию о себе. 

Не переходите по сторонним ссылкам, не присланным администратором чата.

Спасибо за внимание и хорошего дня!
                    """)
                    asyncio.create_task(delete_message(warning_message, 60))
                elif language_captcha[0][0] == 'gb':

                    warning_access = await message.answer('Artificial Intelligence successfully activated ✅')
                    await message.answer("""Dear users, your safety is important to us, so we recommend you not to post your personal information, as well as any other information about yourself. 

Do not follow any third-party links that are not sent by the chat administrator.

Thank you for your attention and have a nice day!
                    """)
                    asyncio.create_task(delete_message(warning_message, 60))
            else:
                await message.reply(text='You do not have permission to do this!')

@dp.message_handler(commands=['unwarning']) # выключение warning
async def warning_message(message: types.Message):
    chat_user = message.chat.id
    if chat_user < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        check_attack = database.get_attack_chat(id_chat=chat_user)
        if check_attack[0][0] == True:
            pass
        else:
            user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            user_id_is_admin = user_admin['status']
            if user_id_is_admin != 'member':
                database.warning_off(chat_id=chat_user)
                await message.answer('Now the bot will not notify about security')
            else:
                await message.reply(text='You do not have permission to do this!')

@dp.message_handler(commands=['/skipOldUsers']) # функция skipOldUsers
async def skipOldUsersCommand(message: types.Message):
    chat_user = message.chat.id
    if chat_user < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        check_attack = database.get_attack_chat(id_chat=chat_user)
        if check_attack[0][0] == True:
            pass
        else:
            user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            user_id_is_admin = user_admin['status']
            if user_id_is_admin != 'member':
                database.skipoldusers_action(id_chat=chat_user, status=True)
                await message.answer('Now people with an ID below 1,000,000,000 will not receive the captcha')
            else:
                await message.reply(text='You do not have permission to do this!')

@dp.message_handler(commands=['/unskipOldUsers']) # аналог функции /skipOldUsers
async def skipOldUsersCommand(message: types.Message):
    chat_user = message.chat.id
    if chat_user < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        check_attack = database.get_attack_chat(id_chat=chat_user)
        if check_attack[0][0] == True:
            pass
        else:
            user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            user_id_is_admin = user_admin['status']
            if user_id_is_admin != 'member':
                database.skipoldusers_action(id_chat=chat_user, status=False)
                await message.answer('Now people with an ID below 1,000,000,000 will receive the captcha')
            else:
                await message.reply(text='You do not have permission to do this!')
class ChangeTypeCaptcha(StatesGroup): # Изменение типа каптчи
    chat_name = State()

class ChangeLanguageCaptcha(StatesGroup): # Изменение языка каптчи
    chat_name = State()

@dp.callback_query_handler(text='settings_captcha') # Настройка каптчи в лс у бота
async def settings_captcha_command(call: types.CallbackQuery):
    keyboard_choose = InlineKeyboardMarkup()
    keyboard_choose_button1 = InlineKeyboardButton(text='◾Type Captcha◾', callback_data='type_captcha') # Измеение типа каптчи
    keyboard_choose_button2 = InlineKeyboardButton(text='◾Language Captcha◾', callback_data='language_captcha') # Изменение языка каптчи
    keyboard_choose.add(keyboard_choose_button1)
    keyboard_choose.add(keyboard_choose_button2)
    await call.message.answer('Choose', reply_markup=keyboard_choose)

@dp.callback_query_handler(text='language_captcha') # Изменение языка каптчи
async def language_captcha_command(call: types.CallbackQuery):
    await call.message.answer('Введите название канала, в котором вы являетесь создателем.')
    await ChangeLanguageCaptcha.chat_name.set()

@dp.message_handler(state=ChangeLanguageCaptcha.chat_name)
async def sendmessagechat_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['chat_name'] = message.text
    all_chats_creator = database.get_all_chats_creator(chat_name=data['chat_name'], id_creator=message.from_user.id)
    if all_chats_creator == []:
        await message.answer('Чата не найдено!')
        await state.finish()
    else:
        chat_id = database.get_chat_name_id(chat_name=data['chat_name'], id_creator=message.from_user.id)
        keyboard_language = InlineKeyboardMarkup()
        keyboard_language_button_ru = InlineKeyboardButton(text='🇷🇺Русский', callback_data='ru_captcha')
        keyboard_language_button_eng = InlineKeyboardButton(text='🇬🇧English', callback_data='gb_captcha')

        keyboard_language.add(keyboard_language_button_ru, keyboard_language_button_eng)
        await message.answer(f'{chat_id} | {data["chat_name"]}', reply_markup=keyboard_language)

        await state.finish()

# Начало:
# Доступные языки каптчи (Русский/Английский) описаны снизу.

@dp.callback_query_handler(text='ru_captcha')
async def ru_captcha_command(call: types.CallbackQuery):
    chat_id = call.message.html_text.split('|')[0].lstrip()
    database.add_chatcaptcha(id_chat=int(chat_id), language='ru')
    await call.message.answer('✅Settings applied✅')


@dp.callback_query_handler(text='gb_captcha')
async def ru_captcha_command(call: types.CallbackQuery):
    chat_id = call.message.html_text.split('|')[0].lstrip()
    database.add_chatcaptcha(id_chat=int(chat_id), language='gb')
    await call.message.answer('✅Settings applied✅')

# Конец.

@dp.callback_query_handler(text='type_captcha') # Изменение типа каптчи
async def type_captcha_command(call: types.CallbackQuery):
    await call.message.answer('Введите название канала, в котором вы являетесь создателем.')
    await ChangeTypeCaptcha.chat_name.set()

@dp.message_handler(state=ChangeTypeCaptcha.chat_name)
async def sendmessagechat_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['chat_name'] = message.text
    all_chats_creator = database.get_all_chats_creator(chat_name=data['chat_name'], id_creator=message.from_user.id)
    print(all_chats_creator)
    if all_chats_creator == []:
        await message.answer('Чата не найдено!')
        await state.finish()
    else:
        keyboard_captcha = InlineKeyboardMarkup(row_width=4)
        keyboard_captcha_button1 = InlineKeyboardButton(text='Simple', callback_data='standart_captcha_ls')
        keyboard_captcha_button2 = InlineKeyboardButton(text='Button', callback_data='highstandart_captcha_ls')
        keyboard_captcha_button3 = InlineKeyboardButton(text='Word', callback_data='word_captcha_ls')
        keyboard_captcha_button4 = InlineKeyboardButton(text='Math', callback_data='math_ex_ls')
        keyboard_captcha.add(keyboard_captcha_button1, keyboard_captcha_button2, keyboard_captcha_button3, keyboard_captcha_button4)
        await message.answer(f"{all_chats_creator[0][0]} | {all_chats_creator[0][1]}\n<b>Please, select the test type for the newcomers:</b>\n\n· <b>Simple</b> - bot will ask to send anything to the chat\n· <b>Word</b> - bot will aks to send word\n· <b>Button</b> - bot will ask to press a button-captcha\n· <b>Math</b> - bot will ask to pass the example", reply_markup=keyboard_captcha, parse_mode='HTML')
        await state.finish()

# Типы каптчи (выбор) в лс:

@dp.callback_query_handler(text='math_ex_ls') # Выбор пользователя поставить в чат математическую каптчу
async def meth_ex_ls_command(call: types.CallbackQuery):
    html_text = call.message.html_text.split('|')
    chat_id = int(html_text[0].lstrip())
    id_chat = database.chat_id_in_list_chats(chat_id=chat_id)[0][0]
    status = database.get_id_admin_in_list_admins(id_user=call['from']['id'], chat_id=id_chat)
    if status != []:
        await call.message.delete()
        database.update_type_captcha(id_chat=chat_id, type=4)
    else:
        await call.answer(text='You do not have permission to do this!')

@dp.callback_query_handler(text='word_captcha_ls') # Выбор пользователя поставить в чат языковую каптчу
async def word_captcha_ls_command(call: types.CallbackQuery):
    html_text = call.message.html_text.split('|')

    chat_id = int(html_text[0].lstrip())
    id_chat = database.chat_id_in_list_chats(chat_id=chat_id)[0][0]
    status = database.get_id_admin_in_list_admins(id_user=call['from']['id'], chat_id=id_chat)
    if status != []:
        await call.message.delete()
        database.update_type_captcha(id_chat=chat_id, type=3)
    else:
        await call.answer(text='You do not have permission to do this!')
@dp.callback_query_handler(text='highstandart_captcha_ls') # Выбор пользователя поставить в чат картинку-каптчу
async def highstandart_captcha_ls_command(call: types.CallbackQuery):
    html_text = call.message.html_text.split('|')

    chat_id = int(html_text[0].lstrip())
    id_chat = database.chat_id_in_list_chats(chat_id=chat_id)[0][0]
    status = database.get_id_admin_in_list_admins(id_user=call['from']['id'], chat_id=id_chat)
    if status != []:
        await call.message.delete()
        database.update_type_captcha(id_chat=chat_id, type=2)
    else:
        await call.answer(text='You do not have permission to do this!')

@dp.callback_query_handler(text='standart_captcha_ls') # Выбор пользователя поставить в чат обычную каптчу
async def standart_captcha_ls_command(call: types.CallbackQuery):
    html_text = call.message.html_text.split('|')

    chat_id = int(html_text[0].lstrip())
    id_chat = database.chat_id_in_list_chats(chat_id=chat_id)[0][0]
    status = database.get_id_admin_in_list_admins(id_user=call['from']['id'], chat_id=id_chat)
    if status != []:
        await call.message.delete()
        database.update_type_captcha(id_chat=chat_id, type=1)
    else:
        await call.answer(text='You do not have permission to do this!')

# Конец типов каптч


@dp.callback_query_handler(text='commands') # показывает пользователю команды бота (в лс)
async def start_command_commands(call: types.CallbackQuery):
    user_id = call.values['from']['id']
    language = database.check_language_user(id_user=user_id)[0][0]

    if language == 'ru':
        kb_start = InlineKeyboardMarkup(resize_keyboard=True)
        kb_button_commands = InlineKeyboardButton(text='Узнать о возможностях бота', callback_data='commands')
        kb_button_invite_chat = InlineKeyboardButton(text='Добавить в чат',
                                                     url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                     callback_data='invite_chat')
        kb_button_site = InlineKeyboardButton(text='Сайт', url='https://redop.netlify.app', callback_data='our_site')
        kb_button_channel = InlineKeyboardButton(text='Наш канал', url='https://t.me/official_redop',
                                                 callback_data='our_channel')
        kb_button_change_language = InlineKeyboardButton(text='Сменить язык', callback_data='change_language')
        kb_start.add(kb_button_invite_chat, kb_button_channel)
        kb_start.add(kb_button_site, kb_button_commands)
        kb_start.add(kb_button_change_language)
        await call.message.answer("""Список команд в чатах:
⭐ /warning - включает оповещение для пользователей, о важности неразглашения своих персональных данных (включить)
⭐ /unwarning - выключает оповещение для пользователей, о важности неразглашения своих персональных данных (выключить)
⭐ /captcha - установить тип каптчи
⭐ /KickRedFlag - вызывает удаление из группы всех пользователей, которые были распознаны ботом как вредоносные
⭐ /ban  - забанить пользователя (переслать сообщение в чате с нарушителем)
⭐ /unban {id-user} - разбанить пользователя
⭐ /mute {минут} - замутить пользователя
⭐ /warn  - дать пользователю предупреждение (переслать сообщение в чате с нарушителем)
⭐ /acquit {id-user} - очистка всех предупреждений пользователя
⭐ /status - узнать информацию в чате
⭐ /pin - ответ на сообщение, которое будет закрепленно
⭐ /unpin - ответ на сообщение, которое будет открепленно
⭐ /banlist - список забаненных людей
⭐ /forwardon - активировать блокировку ссылок в сообщениях для обычных пользователей
⭐ /forwardoff - отключить блокировку ссылок в сообщениях
⭐ /silenceon - отключить чат
⭐ /silenceoff - включить чат
⭐ /cdoctor - проверка административных прав бота в группе.
⭐ /reload_admins - список админов чата.
⭐ /skipOldUsers - не спрашивать каптчу у пользователей, ID ниже 1.000.000.000
⭐ /unskipOldUsers - выкл. режим skipOldUsers
⭐ /lock - все команды будут доступны только админам
⭐ /unlock - предоставить доступ пользовательских команд пользователям
⭐ /attackon - делает все команды бота недоступными
⭐ /attackoff - делает все команды бота снова доступными
⭐ /deleteEntryMessage - удалять сообщения о вступлении пользователя в группу
⭐ /undeleteEntryMessage - оставить сообщения о вступлении пользователя в группу
⭐ /greeting - сообщать пользователю о пройденной каптче
⭐ /ungreeting - не сообщать пользователю о пройденной каптче

Некоторые команды <b>доступны только админам чата.</b>""", reply_markup=kb_start, parse_mode="HTML")


    elif language == 'sa':
        kb_start = InlineKeyboardMarkup(resize_keyboard=True)
        kb_button_commands = InlineKeyboardButton(text='تعرف على قدرات الروبوت', callback_data='commands')
        kb_button_invite_chat = InlineKeyboardButton(text='إضافة دردشة   ',
                                                     url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                     callback_data='invite_chat')
        kb_button_site = InlineKeyboardButton(text='الموقع الإلكتروني   ', url='https://redop.netlify.app', callback_data='our_site')
        kb_button_channel = InlineKeyboardButton(text='قناتنا', url='https://t.me/official_redop', callback_data='our_channel')
        kb_button_change_language = InlineKeyboardButton(text='تغيير اللغة', callback_data='change_language')
        kb_start.add(kb_button_invite_chat, kb_button_channel)
        kb_start.add(kb_button_site, kb_button_commands)
        kb_start.add(kb_button_change_language)

        await call.message.answer("""List of commands in chats:
⭐ /warning - enables the notification for users, about the importance of non-disclosure of their personal data (enable)
⭐ /unwarning - turns off the notification for users about the importance of non-disclosure of their personal data (off)
⭐ /captcha - set captcha type
⭐ /KickRedFlag - causes all users that have been detected by the bot as malicious to be removed from the group
⭐ /ban - ban the user (send a chat message to the offender)
⭐ /unban {id-user} - Unban the user
⭐ /mute {minute} - make a user sick
⭐ /warn - give the user a warning (forward a chat message to the offender)
⭐ /acquit {id-user} - Clear all warnings of the user
⭐ /status - see information in chat
⭐ /pin - reply to the message to be pinned
⭐ /unpin - reply to a message that will be detached
⭐ /banlist - list of people banned
⭐ /forwardon - enable link blocking in posts for normal users
⭐ /forwardoff - disable link blocking in posts
⭐ /silenceon - disable chat
⭐ /silenceoff - turn on chat
⭐ /cdoctor - check the administrative rights of the bot in the group.
⭐ /reload_admins - list of chat admins.
⭐ /skipOldUsers - do not ask captcha for users with ID below 1.000.000.000
⭐ /unskipOldUsers - turn off skipOldUsers mode
⭐ /lock - all commands will be available only for admins
⭐ /unlock - give access to user commands to users
⭐ /attackon - make all bot commands unavailable
⭐ /attackoff - makes all bot commands available again
⭐ /deleteEntryMessage - deletes messages when a user joins a group
⭐ /undeleteEntryMessage - leave messages about user's joining the group
⭐ /greeting - inform user about passed captcha
⭐ /ungreeting - do not inform the user about passed captcha

Some <b>commands are only available to chat admins.</b>""", reply_markup=kb_start, parse_mode="HTML")

    else:
        kb_start = InlineKeyboardMarkup(resize_keyboard=True)
        kb_button_commands = InlineKeyboardButton(text='Learn about the capabilities of the bot',
                                                  callback_data='commands')
        kb_button_invite_chat = InlineKeyboardButton(text='Add a chat',
                                                     url='https://t.me/Redop_AntiSpam_bot?startgroup=hbase',
                                                     callback_data='invite_chat')
        kb_button_site = InlineKeyboardButton(text='Website', url='https://redop.netlify.app', callback_data='')
        kb_button_channel = InlineKeyboardButton(text='Our channel', url='https://t.me/official_redop',
                                                 callback_data='our_channel')
        kb_button_change_language = InlineKeyboardButton(text='Change language', callback_data='change_language')
        kb_start.add(kb_button_invite_chat, kb_button_channel)
        kb_start.add(kb_button_site, kb_button_commands)
        kb_start.add(kb_button_change_language)
        await call.message.answer("""List of commands in chats:
⭐ /warning - enables the notification for users, about the importance of non-disclosure of their personal data (enable)
⭐ /unwarning - turns off the notification for users about the importance of non-disclosure of their personal data (off)
⭐ /captcha - set captcha type
⭐ /KickRedFlag - causes all users that have been detected by the bot as malicious to be removed from the group
⭐ /ban - ban the user (send a chat message to the offender)
⭐ /unban {id-user} - Unban the user
⭐ /mute {minute} - make a user sick
⭐ /warn - give the user a warning (forward a chat message to the offender)
⭐ /acquit {id-user} - Clear all warnings of the user
⭐ /status - see information in chat
⭐ /pin - reply to the message to be pinned
⭐ /unpin - reply to a message that will be detached
⭐ /banlist - list of people banned
⭐ /forwardon - enable link blocking in posts for normal users
⭐ /forwardoff - disable link blocking in posts
⭐ /silenceon - disable chat
⭐ /silenceoff - turn on chat
⭐ /cdoctor - check the administrative rights of the bot in the group.
⭐ /reload_admins - list of chat admins.
⭐ /skipOldUsers - do not ask captcha for users with ID below 1.000.000.000
⭐ /unskipOldUsers - turn off skipOldUsers mode
⭐ /lock - all commands will be available only for admins
⭐ /unlock - give access to user commands to users
⭐ /attackon - make all bot commands unavailable
⭐ /attackoff - makes all bot commands available again
⭐ /deleteEntryMessage - deletes messages when a user joins a group
⭐ /undeleteEntryMessage - leave messages about user's joining the group
⭐ /greeting - inform user about passed captcha
⭐ /ungreeting - do not inform the user about passed captcha

Some <b>commands are only available to chat admins.</b>""", reply_markup=kb_start, parse_mode="HTML")

@dp.message_handler(commands=['help']) # пользователь в чате/в лс с ботом может написать /help и он получит все доступные команды бота
async def help_command(message: types.Message):
    await message.reply(text="""List of commands in chats:
⭐ /warning - enables the notification for users, about the importance of non-disclosure of their personal data (enable)
⭐ /unwarning - turns off the notification for users about the importance of non-disclosure of their personal data (off)
⭐ /captcha - set captcha type
⭐ /KickRedFlag - causes all users that have been detected by the bot as malicious to be removed from the group
⭐ /ban - ban the user (send a chat message to the offender)
⭐ /unban {id-user} - Unban the user
⭐ /mute {minute} - make a user sick
⭐ /warn - give the user a warning (forward a chat message to the offender)
⭐ /acquit {id-user} - Clear all warnings of the user
⭐ /status - see information in chat
⭐ /pin - reply to the message to be pinned
⭐ /unpin - reply to a message that will be detached
⭐ /banlist - list of people banned
⭐ /forwardon - enable link blocking in posts for normal users
⭐ /forwardoff - disable link blocking in posts
⭐ /silenceon - disable chat
⭐ /silenceoff - turn on chat
⭐ /cdoctor - check the administrative rights of the bot in the group.
⭐ /reload_admins - list of chat admins.
⭐ /skipOldUsers - do not ask captcha for users with ID below 1.000.000.000
⭐ /unskipOldUsers - turn off skipOldUsers mode
⭐ /lock - all commands will be available only for admins
⭐ /unlock - give access to user commands to users
⭐ /attackon - make all bot commands unavailable
⭐ /attackoff - makes all bot commands available again
⭐ /deleteEntryMessage - deletes messages when a user joins a group
⭐ /undeleteEntryMessage - leave messages about user's joining the group
⭐ /greeting - inform user about passed captcha
⭐ /ungreeting - do not inform the user about passed captcha

Some <b>commands are only available to chat admins.</b>""", parse_mode='HTML')


@dp.callback_query_handler(text='change_language') # Кнопка в лс о смене языка
async def change_language_command(call: types.CallbackQuery):
    keyboard_language = InlineKeyboardMarkup()
    keyboard_language_button_ru = InlineKeyboardButton(text='🇷🇺Русский', callback_data='ru')
    keyboard_language_button_eng = InlineKeyboardButton(text='🇬🇧English', callback_data='gb')
    keyboard_language_button_arab = InlineKeyboardButton(text='🇸🇦العربية', callback_data='sa')
    keyboard_language_button_it = InlineKeyboardButton(text='🇮🇹Italiano', callback_data='it')
    keyboard_language_button_esp = InlineKeyboardButton(text='🇪🇸Espanol', callback_data='esp')
    keyboard_language_button_norw = InlineKeyboardButton(text='🇳🇴Norwegian', callback_data='norw')
    keyboard_language_button_ind = InlineKeyboardButton(text='🇮🇩Indonesian', callback_data='ind')
    keyboard_language_button_rom = InlineKeyboardButton(text='🇷🇴Romanian', callback_data='rom')
    keyboard_language_button_slovak = InlineKeyboardButton(text='🇸🇰Slovak', callback_data='slov')
    keyboard_language_button_fin = InlineKeyboardButton(text='🇫🇮Finnish', callback_data='fin')
    keyboard_language_button_eesti = InlineKeyboardButton(text='🇪🇪Eesti', callback_data='eesti')
    keyboard_language_button_port = InlineKeyboardButton(text='🇧🇷Portugues Brasil🇵🇹', callback_data='port_bras')
    keyboard_language_button_chin = InlineKeyboardButton(text='🇨🇳Chinese', callback_data='chin')
    keyboard_language_button_deu = InlineKeyboardButton(text='🇩🇪Deutsch', callback_data='deu')
    keyboard_language_button_french = InlineKeyboardButton(text='🇫🇷French', callback_data='fren')
    keyboard_language_button_czech = InlineKeyboardButton(text='🇨🇿Czech', callback_data='czech')
    keyboard_language_button_turk = InlineKeyboardButton(text='🇹🇷Turkce', callback_data='turk')
    keyboard_language_button_cat = InlineKeyboardButton(text='🇪🇸Catalan', callback_data='catalan')
    keyboard_language_button_hung = InlineKeyboardButton(text='🇭🇺Hungarian', callback_data='hung')
    keyboard_language_button_bulg = InlineKeyboardButton(text='🇧🇬Bulgarian', callback_data='bulg')

    keyboard_language.add(keyboard_language_button_ru, keyboard_language_button_eng)
    keyboard_language.add(keyboard_language_button_arab, keyboard_language_button_it)
    keyboard_language.add(keyboard_language_button_esp, keyboard_language_button_norw)
    keyboard_language.add(keyboard_language_button_ind, keyboard_language_button_rom)
    keyboard_language.add(keyboard_language_button_slovak, keyboard_language_button_fin)
    keyboard_language.add(keyboard_language_button_eesti, keyboard_language_button_port)
    keyboard_language.add(keyboard_language_button_chin, keyboard_language_button_deu)
    keyboard_language.add(keyboard_language_button_french, keyboard_language_button_czech)
    keyboard_language.add(keyboard_language_button_turk, keyboard_language_button_cat)
    keyboard_language.add(keyboard_language_button_hung, keyboard_language_button_bulg)

    await call.message.answer('Choose language', reply_markup=keyboard_language)

@dp.message_handler(commands=['cdoctor']) # команда /cdoctor в чате, показывает доступные разрешения бота в чате
async def cdoctor_button(message: types.Message):
    message_chat_id = message.chat.id
    if message_chat_id < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        check_attack = database.get_attack_chat(id_chat=message_chat_id)
        if check_attack[0][0] == True:
            pass
        else:
            lock_chat = database.check_lock_chat(id_chat=message_chat_id)
            if lock_chat != []:
                user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
                user_id_is_admin = user_admin['status']
                if user_id_is_admin != 'member':
                    bot_status_in_chat = await bot.get_chat_administrators(chat_id=message_chat_id)
                    for bot_status in bot_status_in_chat:
                        if bot_status['user']['username'] == username_bot:
                            can_be_edited = bot_status['can_be_edited']
                            can_manage_chat = bot_status['can_manage_chat']
                            can_change_info = bot_status['can_change_info']
                            can_delete_messages = bot_status['can_delete_messages']
                            can_invite_users = bot_status['can_invite_users']
                            can_restrict_members = bot_status['can_restrict_members']
                            can_pin_messages = bot_status['can_pin_messages']
                            can_manage_topics = bot_status['can_manage_topics']
                            can_promote_members = bot_status['can_promote_members']
                            can_manage_video_chats = bot_status['can_manage_video_chats']
                            is_anonymous = bot_status['is_anonymous']
                            can_manage_voice_chats = bot_status['can_manage_voice_chats']
                            await message.answer(f"""
Bot rights in this chat:
<b>Can edit</b> - {can_be_edited}
<b>Can manage chat</b> - {can_manage_chat}
<b>Can change information</b> - {can_change_info}
<b>Can delete messages</b> - {can_delete_messages}
<b>Can invite new members</b> - {can_invite_users}
<b>Can restrict users in some way</b> - {can_restrict_members}
<b>Can pin messages</b> - {can_pin_messages}
<b>Can manage topics</b> - {can_manage_topics}
<b>Can promote users in anything</b> - {can_promote_members}
<b>Can manage video chats</b> - {can_manage_video_chats}
<b>Bot - anonymous</b> - {is_anonymous}
<b>Can manage voice chats</b> - {can_manage_voice_chats}
""", parse_mode='HTML')
                else:
                    await message.reply(text='You do not have permission to do this!')
            else:
                bot_status_in_chat = await bot.get_chat_administrators(chat_id=message_chat_id)
                for bot_status in bot_status_in_chat:
                    if bot_status['user']['username'] == username_bot:
                        can_be_edited = bot_status['can_be_edited']
                        can_manage_chat = bot_status['can_manage_chat']
                        can_change_info = bot_status['can_change_info']
                        can_delete_messages = bot_status['can_delete_messages']
                        can_invite_users = bot_status['can_invite_users']
                        can_restrict_members = bot_status['can_restrict_members']
                        can_pin_messages = bot_status['can_pin_messages']
                        can_manage_topics = bot_status['can_manage_topics']
                        can_promote_members = bot_status['can_promote_members']
                        can_manage_video_chats = bot_status['can_manage_video_chats']
                        is_anonymous = bot_status['is_anonymous']
                        can_manage_voice_chats = bot_status['can_manage_voice_chats']
                        await message.answer(f"""
Bot rights in this chat:
<b>Can edit</b> - {can_be_edited}
<b>Can manage chat</b> - {can_manage_chat}
<b>Can change information</b> - {can_change_info}
<b>Can delete messages</b> - {can_delete_messages}
<b>Can invite new members</b> - {can_invite_users}
<b>Can restrict users in some way</b> - {can_restrict_members}
<b>Can pin messages</b> - {can_pin_messages}
<b>Can manage topics</b> - {can_manage_topics}
<b>Can promote users in anything</b> - {can_promote_members}
<b>Can manage video chats</b> - {can_manage_video_chats}
<b>Bot - anonymous</b> - {is_anonymous}
<b>Can manage voice chats</b> - {can_manage_voice_chats}
""", parse_mode='HTML')

@dp.message_handler(commands=['reload_admins']) # список всех админов чата
async def reload_admins_button(message: types.Message):
    message_chat_id = message.chat.id
    if message_chat_id < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        check_attack = database.get_attack_chat(id_chat=message_chat_id)
        if check_attack[0][0] == True:
            pass
        else:
            lock_chat = database.check_lock_chat(id_chat=message_chat_id)
            if lock_chat != []:
                user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
                user_id_is_admin = user_admin['status']
                if user_id_is_admin != 'member':
                    all_admins = await bot.get_chat_administrators(message_chat_id)
                    for admin in all_admins:
                        await message.answer(f' Chat Administrator:\n'
                                             f"@{admin['user']['username']} - {admin['user']['first_name']}"
                                             '')
                else:
                    await message.reply(text='You do not have permission to do this!')
            else:
                all_admins = await bot.get_chat_administrators(message_chat_id)
                for admin in all_admins:
                    await message.answer(f' Chat Administrator:\n'
                                         f"@{admin['user']['username']} - {admin['user']['first_name']}"
                                         '')

@dp.message_handler(commands=['status']) # функция дает пользователю узнать кто он в группе
async def get_all_users_who_in_chat(message: types.Message):
    message_chat_id = message.chat.id
    if message_chat_id < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        check_attack = database.get_attack_chat(id_chat=message_chat_id)
        if check_attack[0][0] == True:
            pass
        else:
            chat_id = database.chat_id_in_list_chats(chat_id=message.chat.id)[0][0]
            user_warns = database.user_warns(message.from_user.id, chat_id=chat_id)
            if user_warns != []:
                all_users = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
                user_id = all_users['user']['id']
                first_name = all_users['user']['first_name']
                username = all_users['user']['username']
                status = all_users['status']
                await message.answer(f"""
            Info about <b>{username}</b>:
Your <b>ID</b>: {user_id}
<b>Name</b>: {first_name}
You have <b>{user_warns[0][1]} warnings!</b>
In the group you are <b>{status}!</b>
    
            """, parse_mode='HTML')
            else:
                all_users = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
                user_id = all_users['user']['id']
                first_name = all_users['user']['first_name']
                username = all_users['user']['username']
                status = all_users['status']
                await message.answer(f"""
            Info about <b>{username}</b>:
Your <b>ID</b>: {user_id}
<b>Name</b>: {first_name}
In the group you are <b>{status}!</b>
""", parse_mode='HTML')


@dp.message_handler(commands=['mute']) # команда мута
async def mute_user(message: types.Message):
    message_chat_id = message.chat.id
    if message_chat_id < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        check_attack = database.get_attack_chat(id_chat=message_chat_id)
        if check_attack[0][0] == True:
            pass
        else:
            user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            user_id_is_admin = user_admin['status']
            if user_id_is_admin != 'member':
                first_name_user_reply = message.reply_to_message.from_user.first_name
                id_user_reply = message.reply_to_message.from_user.id
                chat_id = database.chat_id_in_list_chats(chat_id=message.chat.id)[0][0]
                admin_or_no = database.user_in_admin_list(id_user_reply, chat_id=chat_id)
                if admin_or_no == []:  # Жалоба не на модератора
                    try:
                        mute_valid = message.text.split(' ')
                        minutes = mute_valid[-1]
                        dt = datetime.datetime.now() + datetime.timedelta(minutes=int(minutes))
                        mute = bot.restrict_chat_member(message.chat.id, id_user_reply, until_date=dt.timestamp())
                        await mute
                        await message.reply(f'User <b>{first_name_user_reply}</b> has been muted for <b>{int(minutes)}</b> minutes!', parse_mode='HTML')
                    except Exception as ex:
                        await message.reply('Enter minutes!')
                else:
                    await message.reply("You can't muddy an admin!")
            else:
                await message.reply(text='You do not have permission to do this!')

@dp.message_handler(commands=['warn']) # команда о выдаче предупреждения
async def get_warn_user(message: types.Message):
    message_chat_id = message.chat.id
    if message_chat_id < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        check_attack = database.get_attack_chat(id_chat=message_chat_id)
        if check_attack[0][0] == True:
            pass
        else:
            user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            user_id_is_admin = user_admin['status']
            if user_id_is_admin != 'member':
                try:
                    id_user_reply = message.reply_to_message.from_user.id
                    first_name_user_reply = message.reply_to_message.from_user.first_name
                    chat_id = database.chat_id_in_list_chats(chat_id=message.chat.id)[0][0]
                    admin_or_no = database.user_in_admin_list(id_user_reply, chat_id=chat_id)
                    print(admin_or_no)
                    if admin_or_no == []: # Жалоба не на модератора
                        result = database.check_user_in_warn(id_user=id_user_reply, first_name=first_name_user_reply, status='member', chat_id=chat_id)
                        if result != None:
                            await message.reply(f'The user {id_user_reply} | {first_name_user_reply} already has {result} alerts, would you like to kick them?', reply_markup=kb_kick)
                        else:
                            await message.reply(f'User {id_user_reply} | {first_name_user_reply} received a warning!')
                    else:
                        await message.reply('You cannot report a moderator')
                except Exception as ex:
                    await message.reply('Forward along with the offending message!')
            else:
                await message.reply(text='You do not have permission to do this!')


@dp.callback_query_handler(text='yeskick') # подтвердить кик
async def kick_member(call: types.CallbackQuery):
    await call.message.delete()

    message_call = call.message.text
    id_user_to_kick = (message_call.split(' |'))[0]
    id_user_to_kick_right = (id_user_to_kick.split('The user ')[1]).replace(' ', '')

    chat_id = database.chat_id_in_list_chats(chat_id=call.message.chat.id)[0][0]

    database.add_user_ban_list(id_user=int(id_user_to_kick_right), by_admin=call.message.from_user.id, chat_id=chat_id)

    kick = bot.ban_chat_member(chat_id=call.message.chat.id, user_id=int(id_user_to_kick_right))
    await kick

@dp.message_handler(commands=['ban']) # команда бан
async def ban_user(message: types.Message):
    message_call = message.chat.id
    if message_call < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        check_attack = database.get_attack_chat(id_chat=message_call)
        if check_attack[0][0] == True:
            pass
        else:
            user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            user_id_is_admin = user_admin['status']
            if user_id_is_admin != 'member':
                id_user_reply = message.reply_to_message.from_user.id
                first_name_user_reply = message.reply_to_message.from_user.first_name
                chat_id = database.chat_id_in_list_chats(chat_id=message.chat.id)[0][0]
                admin_or_no = database.user_in_admin_list(id_user_reply, chat_id=chat_id)
                if admin_or_no == []:
                    result = database.get_id_admin_in_list_admins(id_user=message.from_user.id, chat_id=chat_id)
                    database.add_user_ban_list(id_user=id_user_reply, by_admin=result[0][0], chat_id=chat_id)
                    kick = bot.ban_chat_member(chat_id=message.chat.id, user_id=int(id_user_reply))
                    await kick
                    await message.reply(f'User <b>{first_name_user_reply}</b> was successfully banned!', parse_mode='HTML')

                else:
                    await message.reply('You cannot ban an administrator!')
            else:
                await message.reply('You do not have permission to do this!')

@dp.message_handler(commands=['unban']) # разбан пользователя
async def unban_users(message: types.Message):
    message_chat = message.chat.id
    if message_chat < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        check_attack = database.get_attack_chat(id_chat=message_chat)
        if check_attack[0][0] == True:
            pass
        else:
            user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            user_id_is_admin = user_admin['status']
            if user_id_is_admin != 'member':
                try:
                    chat_id = database.chat_id_in_list_chats(chat_id=message.chat.id)[0][0]
                    id_user_banned = message.text.split(' ')[-1]
                    database.delete_user_ban_list(id_user=id_user_banned, chat_id=chat_id)
                    unban_user = bot.unban_chat_member(chat_id=message.chat.id, user_id=int(id_user_banned))
                    await unban_user
                    await message.reply('The user has been unbanned!')
                except Exception as ex:
                    await message.reply('Please enter a valid user id!')
            else:
                await message.reply('You do not have rights to this command!')

@dp.message_handler(commands=['banlist']) # список людей, которые находятся в бане
async def ban_list(message: types.Message):
    message_chat_id = message.chat.id
    if message_chat_id < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        check_attack = database.get_attack_chat(id_chat=message_chat_id)
        if check_attack[0][0] == True:
            pass
        else:
            chat_id = database.chat_id_in_list_chats(chat_id=message.chat.id)[0][0]
            result = database.ban_list_users(chat_id=chat_id)
            if result == []:
                await message.answer('There are no banned users!')
            else:
                myData = result
                myFile = open('banned.csv', 'w')
                with myFile:
                    writer = csv.writer(myFile)
                    writer.writerows(myData)

                await message.reply_document(open('banned.csv', 'rb'))

@dp.callback_query_handler(text='nokick') # не кикать (команда)
async def delete_message_to_kick(callback_query: types.CallbackQuery):
    await callback_query.message.delete()

@dp.message_handler(commands=['acquit'])
async def acquit_user_warns(message: types.Message):
    message_call = message.chat.id
    if message_call < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        check_attack = database.get_attack_chat(id_chat=message_call)
        if check_attack[0][0] == True:
            pass
        else:
            user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            user_id_is_admin = user_admin['status']
            if user_id_is_admin != 'member':
                try:
                    id_user_reply = message.reply_to_message.from_user.id
                    chat_id = database.chat_id_in_list_chats(chat_id=message.chat.id)[0][0]
                    database.acquit_all_warns_user(id_user=id_user_reply, chat_id=chat_id)
                    await message.reply('<b>All warnings have been successfully removed!</b>', parse_mode='HTML')
                except Exception as ex:
                    await message.reply('Forward along with the offending message!')
            else:
                await message.reply('You do not have permission to do this')


@dp.message_handler(commands=['pin'])
async def pin_message(message: types.Message):
    message_call = message.chat.id
    if message_call < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        check_attack = database.get_attack_chat(id_chat=message_call)
        if check_attack[0][0] == True:
            pass
        else:
            user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            user_id_is_admin = user_admin['status']
            if user_id_is_admin != 'member':
                try:
                    id_message_reply = message.reply_to_message.message_id
                    pin = bot.pin_chat_message(chat_id=message.chat.id, message_id=id_message_reply)
                    await pin
                    await message.reply('<b>Message pinned successfully!</b>', parse_mode='HTML')
                except Exception as ex:
                    await message.reply('Forward the message you want to pin!')
            else:
                await message.reply('You do not have permission to do this!')

@dp.message_handler(commands=['unpin'])
async def unpin_message(message: types.Message):
    message_call = message.chat.id
    if message_call < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        check_attack = database.get_attack_chat(id_chat=message_call)
        if check_attack[0][0] == True:
            pass
        else:
            user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            user_id_is_admin = user_admin['status']
            if user_id_is_admin != 'member':
                try:
                    id_message_reply = message.reply_to_message.message_id
                    pin = bot.unpin_chat_message(chat_id=message.chat.id, message_id=id_message_reply)
                    await pin
                    await message.reply('<b>Post successfully unpinned!</b>', parse_mode='HTML')
                except Exception as ex:
                    await message.reply('Forward the message you want to unpin!')
            else:
                await message.reply('You do not have permission to do this!')

@dp.message_handler(commands=['kick'])
async def kick_user_from_chat(message: types.Message):
    message_chat_id = message.chat.id
    if message_chat_id < 0:
        check_attack = database.get_attack_chat(id_chat=message_chat_id)
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        if check_attack[0][0] == True:
            pass
        else:
            user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            user_id_is_admin = user_admin['status']
            if user_id_is_admin != 'member':
                first_name_user_reply = message.reply_to_message.from_user.first_name
                id_user_reply = message.reply_to_message.from_user.id
                chat_id = database.chat_id_in_list_chats(chat_id=message.chat.id)[0][0]
                admin_or_no = database.user_in_admin_list(id_user_reply, chat_id=chat_id)
                if admin_or_no == []:
                    try:
                        mute_valid = message.text.split(' ')
                        minutes = mute_valid[-1]
                        dt = datetime.datetime.now() + datetime.timedelta(minutes=int(minutes))
                        mute = bot.kick_chat_member(message.chat.id, id_user_reply, until_date=dt.timestamp())
                        await mute
                        await message.reply(
                            f'User <b>{first_name_user_reply}</b> got kicked for<b>{int(minutes)}</b> minutes!',
                            parse_mode='HTML')
                    except Exception as ex:
                        await message.reply('Enter minutes!')
                else:
                    await message.reply('You cannot kick an admin!')
            else:
                await message.reply(text='You do not have permission to do this!')

@dp.message_handler(commands=['silenceon'])
async def silence_on_chat(message: types.Message):
    message_chat_id = message.chat.id
    if message_chat_id < 0:
        check_attack = database.get_attack_chat(id_chat=message_chat_id)
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        if check_attack[0][0] == True:
            pass
        else:
            user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            user_id_is_admin = user_admin['status']
            if user_id_is_admin != 'member':
                database.silence_on(chat_id=message.chat.id)
                await message.reply('<b>Chat is now unable to speak!</b>', parse_mode='HTML')
            else:
                await message.reply(text='You do not have permission to do this!')

@dp.message_handler(commands=['silenceoff'])
async def silence_off_chat(message: types.Message):
    message_chat_id = message.chat.id
    if message_chat_id < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        check_attack = database.get_attack_chat(id_chat=message_chat_id)
        if check_attack[0][0] == True:
            pass
        else:
            user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            user_id_is_admin = user_admin['status']
            if user_id_is_admin != 'member':
                database.silence_off(chat_id=message.chat.id)
                await message.reply('<b>Chat can now speak!</b>', parse_mode='HTML')
            else:
                await message.reply(text='You do not have permission to do this!')

@dp.message_handler(commands=['forwardon'])
async def forward_on_chat(message: types.Message):
    message_chat_id = message.chat.id
    if message_chat_id < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        check_attack = database.get_attack_chat(id_chat=message_chat_id)
        if check_attack[0][0] == True:
            pass
        else:
            user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            user_id_is_admin = user_admin['status']
            if user_id_is_admin != 'member':
                database.forward_on(chat_id=message.chat.id)
                await message.reply('<b>Link blocking activated!</b>', parse_mode='HTML')
            else:
                await message.reply(text='You do not have permission to do this!')

@dp.message_handler(commands=['forwardoff'])
async def forward_off_chat(message: types.Message):
    message_chat_id = message.chat.id
    if message_chat_id < 0:
        captcha_now = database.get_user_captcha_chat(id_user=message.from_user.id)
        if captcha_now != []:
            await message.delete()
            await message.answer('You need to pass the captcha the bot sent you')
            await message.delete()
        check_attack = database.get_attack_chat(id_chat=message_chat_id)
        if check_attack[0][0] == True:
            pass
        else:
            user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            user_id_is_admin = user_admin['status']
            if user_id_is_admin != 'member':
                database.forward_off(chat_id=message.chat.id)
                await message.reply('<b>Link blocking disabled!</b>', parse_mode='HTML')
            else:
                await message.reply(text='You do not have permission to do this!')

@dp.message_handler(content_types=['new_chat_members'])
async def new_member(message: types.Message):
    who_invite = message.from_user.id
    all_admins = await bot.get_chat_administrators(chat_id=message.chat.id)
    x = 0
    for admin in all_admins:
        print(admin)
        if admin['user']['id'] == who_invite:
            x = 1
    print(x)
    if x == 0:
        # Проверка фото и дата создания
        images = bot.get_user_profile_photos(user_id=who_invite, limit=1)
        if images == [] and who_invite > 7000000000:
            database.add_table_user_kdf(id_user=who_invite, id_chat=message.chat.id)
        try:
            language_captcha = database.get_language_captcha(id_chat=message.chat.id)[0][0]
        except Exception as ex:
            language_captcha = []
        captcha_type = database.get_type_captcha(id_chat=message.chat.id)[0][0]
        print(captcha_type)
        skipoldusers = database.skipoldusers_check(id_chat=message.chat.id)
        check_entry = database.get_entry_chat(id_chat=message.chat.id)
        if check_entry != []:
            await message.delete()
        try:
            if skipoldusers[0][0] == True:
                if message.from_user.id < 1000000000:
                    print(2)
                    pass
                else:
                    if captcha_type == 4:
                        if language_captcha == []:
                            random_message = random.randint(1, 10)
                            word = database.get_math_example(number=random_message)[0][0]
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            await message.answer(f"""
                                                {message.from_user.first_name}, сhat out the solution to this example  {word[0][1]} {word[0][3]} {word[0][2]} !\nYou have 60 seconds
                                                """)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=4,
                                                     day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1)
                        elif language_captcha[0][0] == 'ru':
                            random_message = random.randint(1, 10)
                            word = database.get_math_example(number=random_message)[0][0]
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            await message.answer(f"""
                                                {message.from_user.first_name}, напиши в чат решение этого примера  {word[0][1]} {word[0][3]} {word[0][2]} !\nУ тебя есть 60 секунд
                                                """)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=4,
                                                     day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1)
                        elif language_captcha[0][0] == 'gb':
                            random_message = random.randint(1, 10)
                            word = database.get_math_example(number=random_message)[0][0]
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            await message.answer(f"""
                                                {message.from_user.first_name}, сhat out the solution to this example  {word[0][1]} {word[0][3]} {word[0][2]} !\nYou have 60 seconds
                                                """)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=4,
                                                     day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1)

                    if captcha_type == 3:
                        if language_captcha == []:
                            random_message = random.randint(1, 12)
                            word = database.get_secret_word(number=random_message)[0][0]
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            await message.answer(f"""
                                                {message.from_user.first_name}, write a code word in the chat room - {word}!\nYou have 60 seconds.
                                                """)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id,
                                                     day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1)

                        elif language_captcha[0][0] == 'ru':
                            random_message = random.randint(1, 12)
                            word = database.get_secret_word(number=random_message)[0][0]
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            await message.answer(f"""
                                                {message.from_user.first_name}, напиши в чат кодовое слово - {word}!\nУ тебя есть 60 секунд
                                                """)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id,
                                                     day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1)

                        elif language_captcha[0][0] == 'gb':
                            random_message = random.randint(1, 12)
                            word = database.get_secret_word(number=random_message)[0][0]
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            await message.answer(f"""
                                                {message.from_user.first_name}, write a code word in the chat room - {word}!\nYou have 60 seconds.
                                                """)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id,
                                                     day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1)

                    if captcha_type == 1:
                        if language_captcha == []:
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            await message.answer(f"""
    {message.from_user.first_name}, Write something in the chat room so we know you're not a bot!\nYou have 60 seconds
                                                """)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=1,
                                                     day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1)

                        elif language_captcha[0][0] == 'ru':
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            await message.answer(f"""
    {message.from_user.first_name}, напиши что-нибудь в чат, так мы поймем, что ты не бот!\nУ тебя есть 60 секунд
                                                """)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=1,
                                                     day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1)

                        elif language_captcha[0][0] == 'gb':
                            random_message = random.randint(1, 12)
                            word = database.get_secret_word(number=random_message)[0][0]
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            await message.answer(f"""
    {message.from_user.first_name}, Write something in the chat room so we know you're not a bot!\nYou have 60 seconds
                                                """)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=1,
                                                     day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1)

                    if captcha_type == 2: # ===F=GFG=DG
                        digit = random.randint(1, 7)
                        print('fsdfsdfs')
                        if language_captcha == []:
                            if digit == 1:
                                img = open('bot/images/captcha_apple.jpg', 'rb')
                                await bot.send_photo(message.chat.id, photo=img,
                                                     caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                     reply_markup=kb_captcha_1)
                                time_now = datetime.datetime.now()
                                time_lose = time_now + datetime.timedelta(minutes=1)
                                database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                         day=datetime.datetime.now().day,
                                                         month=datetime.datetime.now().month,
                                                         year=datetime.datetime.now().year,
                                                         h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                         s1=datetime.datetime.now().second,
                                                         h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                         message_id=message.message_id + 1
                                                         )
                            if digit == 2:
                                img = open('bot/images/captcha_cucumber.jpg', 'rb')
                                await bot.send_photo(message.chat.id, photo=img,
                                                     caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                     reply_markup=kb_captcha_2)
                                time_now = datetime.datetime.now()
                                time_lose = time_now + datetime.timedelta(minutes=1)
                                database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                         day=datetime.datetime.now().day,
                                                         month=datetime.datetime.now().month,
                                                         year=datetime.datetime.now().year,
                                                         h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                         s1=datetime.datetime.now().second,
                                                         h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                         message_id=message.message_id + 1
                                                         )

                            if digit == 3:
                                img = open('bot/images/captcha_grape.jpg', 'rb')
                                await bot.send_photo(message.chat.id, photo=img,
                                                     caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                     reply_markup=kb_captcha_3)
                                time_now = datetime.datetime.now()
                                time_lose = time_now + datetime.timedelta(minutes=1)
                                database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                         day=datetime.datetime.now().day,
                                                         month=datetime.datetime.now().month,
                                                         year=datetime.datetime.now().year,
                                                         h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                         s1=datetime.datetime.now().second,
                                                         h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                         message_id=message.message_id + 1
                                                         )

                            if digit == 4:
                                img = open('bot/images/captcha_pizza.jpg', 'rb')
                                await bot.send_photo(message.chat.id, photo=img,
                                                     caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                     reply_markup=kb_captcha_4)
                                time_now = datetime.datetime.now()
                                time_lose = time_now + datetime.timedelta(minutes=1)
                                database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                         day=datetime.datetime.now().day,
                                                         month=datetime.datetime.now().month,
                                                         year=datetime.datetime.now().year,
                                                         h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                         s1=datetime.datetime.now().second,
                                                         h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                         message_id=message.message_id + 1
                                                         )

                            if digit == 5:
                                img = open('bot/images/captcha_pretzel.jpg', 'rb')
                                await bot.send_photo(message.chat.id, photo=img,
                                                     caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                     reply_markup=kb_captcha_5)
                                time_now = datetime.datetime.now()
                                time_lose = time_now + datetime.timedelta(minutes=1)
                                database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                         day=datetime.datetime.now().day,
                                                         month=datetime.datetime.now().month,
                                                         year=datetime.datetime.now().year,
                                                         h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                         s1=datetime.datetime.now().second,
                                                         h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                         message_id=message.message_id + 1
                                                         )

                            if digit == 6:
                                img = open('bot/images/captcha_cherry.jpg', 'rb')
                                await bot.send_photo(message.chat.id, photo=img,
                                                     caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                     reply_markup=kb_captcha_6)
                                time_now = datetime.datetime.now()
                                time_lose = time_now + datetime.timedelta(minutes=1)
                                database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                         day=datetime.datetime.now().day,
                                                         month=datetime.datetime.now().month,
                                                         year=datetime.datetime.now().year,
                                                         h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                         s1=datetime.datetime.now().second,
                                                         h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                         message_id=message.message_id + 1
                                                         )

                            if digit == 7:
                                img = open('bot/images/captcha_banana.jpg', 'rb')
                                await bot.send_photo(message.chat.id, photo=img,
                                                     caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                     reply_markup=kb_captcha_7)
                                time_now = datetime.datetime.now()
                                time_lose = time_now + datetime.timedelta(minutes=1)
                                database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                         day=datetime.datetime.now().day,
                                                         month=datetime.datetime.now().month,
                                                         year=datetime.datetime.now().year,
                                                         h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                         s1=datetime.datetime.now().second,
                                                         h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                         message_id=message.message_id + 1
                                                         )

                        elif language_captcha[0][0] == 'ru':
                            if digit == 1:
                                img = open('bot/images/captcha_apple.jpg', 'rb')
                                await bot.send_photo(message.chat.id, photo=img,
                                                     caption=f"{message.from_user.id}|Тебе необходимо пройти каптчу!\nЧто изображено на картинке?",
                                                     reply_markup=kb_captcha_1)
                                time_now = datetime.datetime.now()
                                time_lose = time_now + datetime.timedelta(minutes=1)
                                database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                         day=datetime.datetime.now().day,
                                                         month=datetime.datetime.now().month,
                                                         year=datetime.datetime.now().year,
                                                         h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                         s1=datetime.datetime.now().second,
                                                         h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                         message_id=message.message_id + 1
                                                         )
                            if digit == 2:
                                img = open('bot/images/captcha_cucumber.jpg', 'rb')
                                await bot.send_photo(message.chat.id, photo=img,
                                                     caption=f"{message.from_user.id}|Тебе необходимо пройти каптчу!\nЧто изображено на картинке?",
                                                     reply_markup=kb_captcha_2)
                                time_now = datetime.datetime.now()
                                time_lose = time_now + datetime.timedelta(minutes=1)
                                database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                         day=datetime.datetime.now().day,
                                                         month=datetime.datetime.now().month,
                                                         year=datetime.datetime.now().year,
                                                         h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                         s1=datetime.datetime.now().second,
                                                         h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                         message_id=message.message_id + 1
                                                         )

                            if digit == 3:
                                img = open('bot/images/captcha_grape.jpg', 'rb')
                                await bot.send_photo(message.chat.id, photo=img,
                                                     caption=f"{message.from_user.id}|Тебе необходимо пройти каптчу!\nЧто изображено на картинке?",
                                                     reply_markup=kb_captcha_3)
                                time_now = datetime.datetime.now()
                                time_lose = time_now + datetime.timedelta(minutes=1)
                                database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                         day=datetime.datetime.now().day,
                                                         month=datetime.datetime.now().month,
                                                         year=datetime.datetime.now().year,
                                                         h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                         s1=datetime.datetime.now().second,
                                                         h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                         message_id=message.message_id + 1
                                                         )

                            if digit == 4:
                                img = open('bot/images/captcha_pizza.jpg', 'rb')
                                await bot.send_photo(message.chat.id, photo=img,
                                                     caption=f"{message.from_user.id}|Тебе необходимо пройти каптчу!\nЧто изображено на картинке?",
                                                     reply_markup=kb_captcha_4)
                                time_now = datetime.datetime.now()
                                time_lose = time_now + datetime.timedelta(minutes=1)
                                database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                         day=datetime.datetime.now().day,
                                                         month=datetime.datetime.now().month,
                                                         year=datetime.datetime.now().year,
                                                         h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                         s1=datetime.datetime.now().second,
                                                         h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                         message_id=message.message_id + 1
                                                         )

                            if digit == 5:
                                img = open('bot/images/captcha_pretzel.jpg', 'rb')
                                await bot.send_photo(message.chat.id, photo=img,
                                                     caption=f"{message.from_user.id}|Тебе необходимо пройти каптчу!\nЧто изображено на картинке?",
                                                     reply_markup=kb_captcha_5)
                                time_now = datetime.datetime.now()
                                time_lose = time_now + datetime.timedelta(minutes=1)
                                database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                         day=datetime.datetime.now().day,
                                                         month=datetime.datetime.now().month,
                                                         year=datetime.datetime.now().year,
                                                         h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                         s1=datetime.datetime.now().second,
                                                         h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                         message_id=message.message_id + 1
                                                         )

                            if digit == 6:
                                img = open('bot/images/captcha_cherry.jpg', 'rb')
                                await bot.send_photo(message.chat.id, photo=img,
                                                     caption=f"{message.from_user.id}|Тебе необходимо пройти каптчу!\nЧто изображено на картинке?",
                                                     reply_markup=kb_captcha_6)
                                time_now = datetime.datetime.now()
                                time_lose = time_now + datetime.timedelta(minutes=1)
                                database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                         day=datetime.datetime.now().day,
                                                         month=datetime.datetime.now().month,
                                                         year=datetime.datetime.now().year,
                                                         h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                         s1=datetime.datetime.now().second,
                                                         h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                         message_id=message.message_id + 1
                                                         )

                            if digit == 7:
                                img = open('bot/images/captcha_banana.jpg', 'rb')
                                await bot.send_photo(message.chat.id, photo=img,
                                                     caption=f"{message.from_user.id}|Тебе необходимо пройти каптчу!\nЧто изображено на картинке?",
                                                     reply_markup=kb_captcha_7)
                                time_now = datetime.datetime.now()
                                time_lose = time_now + datetime.timedelta(minutes=1)
                                database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                         day=datetime.datetime.now().day,
                                                         month=datetime.datetime.now().month,
                                                         year=datetime.datetime.now().year,
                                                         h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                         s1=datetime.datetime.now().second,
                                                         h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                         message_id=message.message_id + 1
                                                         )

                        elif language_captcha[0][0] == 'gb':
                            if digit == 1:
                                img = open('bot/images/captcha_apple.jpg', 'rb')
                                await bot.send_photo(message.chat.id, photo=img,
                                                     caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                     reply_markup=kb_captcha_1)
                                time_now = datetime.datetime.now()
                                time_lose = time_now + datetime.timedelta(minutes=1)
                                database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                         day=datetime.datetime.now().day,
                                                         month=datetime.datetime.now().month,
                                                         year=datetime.datetime.now().year,
                                                         h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                         s1=datetime.datetime.now().second,
                                                         h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                         message_id=message.message_id + 1
                                                         )
                            if digit == 2:
                                img = open('bot/images/captcha_cucumber.jpg', 'rb')
                                await bot.send_photo(message.chat.id, photo=img,
                                                     caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                     reply_markup=kb_captcha_2)
                                time_now = datetime.datetime.now()
                                time_lose = time_now + datetime.timedelta(minutes=1)
                                database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                         day=datetime.datetime.now().day,
                                                         month=datetime.datetime.now().month,
                                                         year=datetime.datetime.now().year,
                                                         h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                         s1=datetime.datetime.now().second,
                                                         h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                         message_id=message.message_id + 1
                                                         )

                            if digit == 3:
                                img = open('bot/images/captcha_grape.jpg', 'rb')
                                await bot.send_photo(message.chat.id, photo=img,
                                                     caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                     reply_markup=kb_captcha_3)
                                time_now = datetime.datetime.now()
                                time_lose = time_now + datetime.timedelta(minutes=1)
                                database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                         day=datetime.datetime.now().day,
                                                         month=datetime.datetime.now().month,
                                                         year=datetime.datetime.now().year,
                                                         h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                         s1=datetime.datetime.now().second,
                                                         h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                         message_id=message.message_id + 1
                                                         )

                            if digit == 4:
                                img = open('bot/images/captcha_pizza.jpg', 'rb')
                                await bot.send_photo(message.chat.id, photo=img,
                                                     caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                     reply_markup=kb_captcha_4)
                                time_now = datetime.datetime.now()
                                time_lose = time_now + datetime.timedelta(minutes=1)
                                database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                         day=datetime.datetime.now().day,
                                                         month=datetime.datetime.now().month,
                                                         year=datetime.datetime.now().year,
                                                         h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                         s1=datetime.datetime.now().second,
                                                         h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                         message_id=message.message_id + 1
                                                         )

                            if digit == 5:
                                img = open('bot/images/captcha_pretzel.jpg', 'rb')
                                await bot.send_photo(message.chat.id, photo=img,
                                                     caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                     reply_markup=kb_captcha_5)
                                time_now = datetime.datetime.now()
                                time_lose = time_now + datetime.timedelta(minutes=1)
                                database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                         day=datetime.datetime.now().day,
                                                         month=datetime.datetime.now().month,
                                                         year=datetime.datetime.now().year,
                                                         h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                         s1=datetime.datetime.now().second,
                                                         h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                         message_id=message.message_id + 1
                                                         )

                            if digit == 6:
                                img = open('bot/images/captcha_cherry.jpg', 'rb')
                                await bot.send_photo(message.chat.id, photo=img,
                                                     caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                     reply_markup=kb_captcha_6)
                                time_now = datetime.datetime.now()
                                time_lose = time_now + datetime.timedelta(minutes=1)
                                database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                         day=datetime.datetime.now().day,
                                                         month=datetime.datetime.now().month,
                                                         year=datetime.datetime.now().year,
                                                         h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                         s1=datetime.datetime.now().second,
                                                         h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                         message_id=message.message_id + 1
                                                         )

                            if digit == 7:
                                img = open('bot/images/captcha_banana.jpg', 'rb')
                                await bot.send_photo(message.chat.id, photo=img,
                                                     caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                     reply_markup=kb_captcha_7)
                                time_now = datetime.datetime.now()
                                time_lose = time_now + datetime.timedelta(minutes=1)
                                database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                         day=datetime.datetime.now().day,
                                                         month=datetime.datetime.now().month,
                                                         year=datetime.datetime.now().year,
                                                         h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                         s1=datetime.datetime.now().second,
                                                         h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                         message_id=message.message_id + 1
                                                         )



            else:
                if captcha_type == 4:
                    print('russsiiiia')
                    print(language_captcha)
                    if language_captcha == []:
                        print('no')
                        random_message = random.randint(1, 9)
                        word = database.get_math_example(number=random_message)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        await message.answer(f"""
                                            {message.from_user.first_name}, сhat out the solution to this example  {word[0][1]} {word[0][3]} {word[0][2]} !\nYou have 60 seconds
                                            """)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=4,
                                                 day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1)

                    elif language_captcha == 'ru':
                        print('ru')
                        random_message = random.randint(1, 9)
                        word = database.get_math_example(number=random_message)
                        print(word)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        await message.answer(f"""
                                            {message.from_user.first_name}, напиши в чат решение этого примера  {word[0][1]} {word[0][3]} {word[0][2]} !\nУ тебя есть 60 секунд
                                            """)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=4,
                                                 day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1)

                    elif language_captcha == 'gb':
                        print('gb')
                        random_message = random.randint(1, 9)
                        word = database.get_math_example(number=random_message)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        await message.answer(f"""
                                            {message.from_user.first_name}, сhat out the solution to this example  {word[0][1]} {word[0][3]} {word[0][2]} !\nYou have 60 seconds
                                            """)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=4,
                                                 day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1)

                if captcha_type == 3:
                    if language_captcha == []:
                        random_message = random.randint(1, 12)
                        word = database.get_secret_word(number=random_message)[0][0]
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        await message.answer(f"""
                                            {message.from_user.first_name}, write a code word in the chat room - {word}!\nYou have 60 seconds.
                                            """)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id,  type=3,
                                                 day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1)

                    elif language_captcha[0][0] == 'ru':
                        random_message = random.randint(1, 12)
                        word = database.get_secret_word(number=random_message)[0][0]
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        await message.answer(f"""
                                            {message.from_user.first_name}, напиши в чат кодовое слово - {word}!\nУ тебя есть 60 секунд
                                            """)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=3,
                                                 day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1)

                    elif language_captcha[0][0] == 'gb':
                        random_message = random.randint(1, 12)
                        word = database.get_secret_word(number=random_message)[0][0]
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        await message.answer(f"""
                                            {message.from_user.first_name}, write a code word in the chat room - {word}!\nYou have 60 seconds.
                                            """)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=3,
                                                 day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1)

                if captcha_type == 1:
                    if language_captcha == []:
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        await message.answer(f"""
                    {message.from_user.first_name}, Write something in the chat room so we know you're not a bot!\nYou have 60 seconds
                                                                """)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=1,
                                                 day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1)

                    elif language_captcha[0][0] == 'ru':
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        await message.answer(f"""
                    {message.from_user.first_name}, напиши что-нибудь в чат, так мы поймем, что ты не бот!\nУ тебя есть 60 секунд
                                                                """)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=1,
                                                 day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1)

                    elif language_captcha[0][0] == 'gb':
                        random_message = random.randint(1, 12)
                        word = database.get_secret_word(number=random_message)[0][0]
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        await message.answer(f"""
                    {message.from_user.first_name}, Write something in the chat room so we know you're not a bot!\nYou have 60 seconds
                                                                """)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=1,
                                                 day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1)
                if captcha_type == 2:
                    print('fsdfs') # tyt
                    digit = random.randint(1, 7)
                    print(digit)
                    print(language_captcha)
                    if language_captcha == []:
                        if digit == 1:
                            img = open('bot/images/captcha_apple.jpg', 'rb')
                            await bot.send_photo(message.chat.id, photo=img,
                                                 caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                 reply_markup=kb_captcha_1)
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                     day=datetime.datetime.now().day,
                                                     month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1
                                                     )
                        if digit == 2:
                            img = open('bot/images/captcha_cucumber.jpg', 'rb')
                            await bot.send_photo(message.chat.id, photo=img,
                                                 caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                 reply_markup=kb_captcha_2)
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                     day=datetime.datetime.now().day,
                                                     month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1
                                                     )

                        if digit == 3:
                            img = open('bot/images/captcha_grape.jpg', 'rb')
                            await bot.send_photo(message.chat.id, photo=img,
                                                 caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                 reply_markup=kb_captcha_3)
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                     day=datetime.datetime.now().day,
                                                     month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1
                                                     )

                        if digit == 4:
                            img = open('bot/images/captcha_pizza.jpg', 'rb')
                            await bot.send_photo(message.chat.id, photo=img,
                                                 caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                 reply_markup=kb_captcha_4)
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                     day=datetime.datetime.now().day,
                                                     month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1
                                                     )

                        if digit == 5:
                            img = open('bot/images/captcha_pretzel.jpg', 'rb')
                            await bot.send_photo(message.chat.id, photo=img,
                                                 caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                 reply_markup=kb_captcha_5)
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                     day=datetime.datetime.now().day,
                                                     month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1
                                                     )

                        if digit == 6:
                            img = open('bot/images/captcha_cherry.jpg', 'rb')
                            await bot.send_photo(message.chat.id, photo=img,
                                                 caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                 reply_markup=kb_captcha_6)
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                     day=datetime.datetime.now().day,
                                                     month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1
                                                     )

                        if digit == 7:
                            img = open('bot/images/captcha_banana.jpg', 'rb')
                            await bot.send_photo(message.chat.id, photo=img,
                                                 caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                 reply_markup=kb_captcha_7)
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                     day=datetime.datetime.now().day,
                                                     month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1
                                                     )

                    elif language_captcha == 'ru':
                        if digit == 1:
                            img = open('bot/images/captcha_apple.jpg', 'rb')
                            await bot.send_photo(message.chat.id, photo=img,
                                                 caption=f"{message.from_user.id}|Тебе необходимо пройти каптчу!\nЧто изображено на картинке?",
                                                 reply_markup=kb_captcha_1)
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                     day=datetime.datetime.now().day,
                                                     month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1
                                                     )
                        if digit == 2:
                            img = open('bot/images/captcha_cucumber.jpg', 'rb')
                            await bot.send_photo(message.chat.id, photo=img,
                                                 caption=f"{message.from_user.id}|Тебе необходимо пройти каптчу!\nЧто изображено на картинке?",
                                                 reply_markup=kb_captcha_2)
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                     day=datetime.datetime.now().day,
                                                     month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1
                                                     )

                        if digit == 3:
                            img = open('bot/images/captcha_grape.jpg', 'rb')
                            await bot.send_photo(message.chat.id, photo=img,
                                                 caption=f"{message.from_user.id}|Тебе необходимо пройти каптчу!\nЧто изображено на картинке?",
                                                 reply_markup=kb_captcha_3)
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                     day=datetime.datetime.now().day,
                                                     month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1
                                                     )

                        if digit == 4:
                            img = open('bot/images/captcha_pizza.jpg', 'rb')
                            await bot.send_photo(message.chat.id, photo=img,
                                                 caption=f"{message.from_user.id}|Тебе необходимо пройти каптчу!\nЧто изображено на картинке?",
                                                 reply_markup=kb_captcha_4)
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                     day=datetime.datetime.now().day,
                                                     month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1
                                                     )

                        if digit == 5:
                            img = open('bot/images/captcha_pretzel.jpg', 'rb')
                            await bot.send_photo(message.chat.id, photo=img,
                                                 caption=f"{message.from_user.id}|Тебе необходимо пройти каптчу!\nЧто изображено на картинке?",
                                                 reply_markup=kb_captcha_5)
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                     day=datetime.datetime.now().day,
                                                     month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1
                                                     )

                        if digit == 6:
                            img = open('bot/images/captcha_cherry.jpg', 'rb')
                            await bot.send_photo(message.chat.id, photo=img,
                                                 caption=f"{message.from_user.id}|Тебе необходимо пройти каптчу!\nЧто изображено на картинке?",
                                                 reply_markup=kb_captcha_6)
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                     day=datetime.datetime.now().day,
                                                     month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1
                                                     )

                        if digit == 7:
                            img = open('bot/images/captcha_banana.jpg', 'rb')
                            await bot.send_photo(message.chat.id, photo=img,
                                                 caption=f"{message.from_user.id}|Тебе необходимо пройти каптчу!\nЧто изображено на картинке?",
                                                 reply_markup=kb_captcha_7)
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                     day=datetime.datetime.now().day,
                                                     month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1
                                                     )

                    elif language_captcha == 'gb':
                        if digit == 1:
                            img = open('bot/images/captcha_apple.jpg', 'rb')
                            await bot.send_photo(message.chat.id, photo=img,
                                                 caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                 reply_markup=kb_captcha_1)
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                     day=datetime.datetime.now().day,
                                                     month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1
                                                     )
                        if digit == 2:
                            img = open('bot/images/captcha_cucumber.jpg', 'rb')
                            await bot.send_photo(message.chat.id, photo=img,
                                                 caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                 reply_markup=kb_captcha_2)
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                     day=datetime.datetime.now().day,
                                                     month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1
                                                     )

                        if digit == 3:
                            img = open('bot/images/captcha_grape.jpg', 'rb')
                            await bot.send_photo(message.chat.id, photo=img,
                                                 caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                 reply_markup=kb_captcha_3)
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                     day=datetime.datetime.now().day,
                                                     month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1
                                                     )

                        if digit == 4:
                            img = open('bot/images/captcha_pizza.jpg', 'rb')
                            await bot.send_photo(message.chat.id, photo=img,
                                                 caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                 reply_markup=kb_captcha_4)
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                     day=datetime.datetime.now().day,
                                                     month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1
                                                     )

                        if digit == 5:
                            img = open('bot/images/captcha_pretzel.jpg', 'rb')
                            await bot.send_photo(message.chat.id, photo=img,
                                                 caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                 reply_markup=kb_captcha_5)
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                     day=datetime.datetime.now().day,
                                                     month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1
                                                     )

                        if digit == 6:
                            img = open('bot/images/captcha_cherry.jpg', 'rb')
                            await bot.send_photo(message.chat.id, photo=img,
                                                 caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                 reply_markup=kb_captcha_6)
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                     day=datetime.datetime.now().day,
                                                     month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1
                                                     )

                        if digit == 7:
                            img = open('bot/images/captcha_banana.jpg', 'rb')
                            await bot.send_photo(message.chat.id, photo=img,
                                                 caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                                 reply_markup=kb_captcha_7)
                            time_now = datetime.datetime.now()
                            time_lose = time_now + datetime.timedelta(minutes=1)
                            database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                     day=datetime.datetime.now().day,
                                                     month=datetime.datetime.now().month,
                                                     year=datetime.datetime.now().year,
                                                     h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                     s1=datetime.datetime.now().second,
                                                     h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                     message_id=message.message_id + 1
                                                     )
        except Exception as ex:
            if captcha_type == 4:
                if language_captcha == []:
                    random_message = random.randint(1, 10)
                    word = database.get_math_example(number=random_message)
                    time_now = datetime.datetime.now()
                    time_lose = time_now + datetime.timedelta(minutes=1)
                    await message.answer(f"""
                                        {message.from_user.first_name}, сhat out the solution to this example  {word[0][1]} {word[0][3]} {word[0][2]} !\nYou have 60 seconds
                                        """)
                    database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=4,
                                             day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                             year=datetime.datetime.now().year,
                                             h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                             s1=datetime.datetime.now().second,
                                             h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                             message_id=message.message_id + 1)

                elif language_captcha[0][0] == 'ru':
                    random_message = random.randint(1, 10)
                    word = database.get_math_example(number=random_message)
                    time_now = datetime.datetime.now()
                    time_lose = time_now + datetime.timedelta(minutes=1)
                    await message.answer(f"""
                                        {message.from_user.first_name}, напиши в чат решение этого примера  {word[0][1]} {word[0][3]} {word[0][2]} !\nУ тебя есть 60 секунд
                                        """)
                    database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=4,
                                             day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                             year=datetime.datetime.now().year,
                                             h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                             s1=datetime.datetime.now().second,
                                             h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                             message_id=message.message_id + 1)

                elif language_captcha[0][0] == 'gb':
                    random_message = random.randint(1, 10)
                    word = database.get_math_example(number=random_message)
                    time_now = datetime.datetime.now()
                    time_lose = time_now + datetime.timedelta(minutes=1)
                    await message.answer(f"""
                                        {message.from_user.first_name}, сhat out the solution to this example  {word[0][1]} {word[0][3]} {word[0][2]} !\nYou have 60 seconds
                                        """)
                    database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=4,
                                             day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                             year=datetime.datetime.now().year,
                                             h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                             s1=datetime.datetime.now().second,
                                             h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                             message_id=message.message_id + 1)

            if captcha_type == 3:
                if language_captcha == []:
                    random_message = random.randint(1, 12)
                    word = database.get_secret_word(number=random_message)[0][0]
                    time_now = datetime.datetime.now()
                    time_lose = time_now + datetime.timedelta(minutes=1)
                    await message.answer(f"""
                                        {message.from_user.first_name}, write a code word in the chat room - {word}!\nYou have 60 seconds.
                                        """)
                    database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id,
                                             day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                             year=datetime.datetime.now().year,
                                             h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                             s1=datetime.datetime.now().second,
                                             h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                             message_id=message.message_id + 1)

                elif language_captcha[0][0] == 'ru':
                    random_message = random.randint(1, 12)
                    word = database.get_secret_word(number=random_message)[0][0]
                    time_now = datetime.datetime.now()
                    time_lose = time_now + datetime.timedelta(minutes=1)
                    await message.answer(f"""
                                        {message.from_user.first_name}, напиши в чат кодовое слово - {word}!\nУ тебя есть 60 секунд
                                        """)
                    database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id,
                                             day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                             year=datetime.datetime.now().year,
                                             h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                             s1=datetime.datetime.now().second,
                                             h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                             message_id=message.message_id + 1)

                elif language_captcha[0][0] == 'gb':
                    random_message = random.randint(1, 12)
                    word = database.get_secret_word(number=random_message)[0][0]
                    time_now = datetime.datetime.now()
                    time_lose = time_now + datetime.timedelta(minutes=1)
                    await message.answer(f"""
                                        {message.from_user.first_name}, write a code word in the chat room - {word}!\nYou have 60 seconds.
                                        """)
                    database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id,
                                             day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                             year=datetime.datetime.now().year,
                                             h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                             s1=datetime.datetime.now().second,
                                             h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                             message_id=message.message_id + 1)

            if captcha_type == 1:
                if language_captcha == []:
                    time_now = datetime.datetime.now()
                    time_lose = time_now + datetime.timedelta(minutes=1)
                    await message.answer(f"""
                {message.from_user.first_name}, Write something in the chat room so we know you're not a bot!\nYou have 60 seconds
                                                            """)
                    database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id,
                                             day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                             year=datetime.datetime.now().year,
                                             h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                             s1=datetime.datetime.now().second,
                                             h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                             message_id=message.message_id + 1, type=1)

                elif language_captcha[0][0] == 'ru':
                    time_now = datetime.datetime.now()
                    time_lose = time_now + datetime.timedelta(minutes=1)
                    await message.answer(f"""
                {message.from_user.first_name}, напиши что-нибудь в чат, так мы поймем, что ты не бот!\nУ тебя есть 60 секунд
                                                            """)
                    database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id,
                                             day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                             year=datetime.datetime.now().year,
                                             h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                             s1=datetime.datetime.now().second,
                                             h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                             message_id=message.message_id + 1, type=1)

                elif language_captcha[0][0] == 'gb':
                    random_message = random.randint(1, 12)
                    word = database.get_secret_word(number=random_message)[0][0]
                    time_now = datetime.datetime.now()
                    time_lose = time_now + datetime.timedelta(minutes=1)
                    await message.answer(f"""
                {message.from_user.first_name}, Write something in the chat room so we know you're not a bot!\nYou have 60 seconds
                                                            """)
                    database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id,
                                             day=datetime.datetime.now().day, month=datetime.datetime.now().month,
                                             year=datetime.datetime.now().year,
                                             h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                             s1=datetime.datetime.now().second,
                                             h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                             message_id=message.message_id + 1, type=1)

            if captcha_type == 2:
                print('fsdfаываываываываыs')

                digit = random.randint(1, 7)
                if language_captcha == []:
                    if digit == 1:
                        img = open('bot/images/captcha_apple.jpg', 'rb')
                        await bot.send_photo(message.chat.id, photo=img,
                                             caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                             reply_markup=kb_captcha_1)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                 day=datetime.datetime.now().day,
                                                 month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1
                                                 )
                    if digit == 2:
                        img = open('bot/images/captcha_cucumber.jpg', 'rb')
                        await bot.send_photo(message.chat.id, photo=img,
                                             caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                             reply_markup=kb_captcha_2)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                 day=datetime.datetime.now().day,
                                                 month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1
                                                 )

                    if digit == 3:
                        img = open('bot/images/captcha_grape.jpg', 'rb')
                        await bot.send_photo(message.chat.id, photo=img,
                                             caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                             reply_markup=kb_captcha_3)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                 day=datetime.datetime.now().day,
                                                 month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1
                                                 )

                    if digit == 4:
                        img = open('bot/images/captcha_pizza.jpg', 'rb')
                        await bot.send_photo(message.chat.id, photo=img,
                                             caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                             reply_markup=kb_captcha_4)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                 day=datetime.datetime.now().day,
                                                 month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1
                                                 )

                    if digit == 5:
                        img = open('bot/images/captcha_pretzel.jpg', 'rb')
                        await bot.send_photo(message.chat.id, photo=img,
                                             caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                             reply_markup=kb_captcha_5)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                 day=datetime.datetime.now().day,
                                                 month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1
                                                 )

                    if digit == 6:
                        img = open('bot/images/captcha_cherry.jpg', 'rb')
                        await bot.send_photo(message.chat.id, photo=img,
                                             caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                             reply_markup=kb_captcha_6)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                 day=datetime.datetime.now().day,
                                                 month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1
                                                 )

                    if digit == 7:
                        img = open('bot/images/captcha_banana.jpg', 'rb')
                        await bot.send_photo(message.chat.id, photo=img,
                                             caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                             reply_markup=kb_captcha_7)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                 day=datetime.datetime.now().day,
                                                 month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1
                                                 )

                elif language_captcha[0][0] == 'ru':
                    if digit == 1:
                        img = open('bot/images/captcha_apple.jpg', 'rb')
                        await bot.send_photo(message.chat.id, photo=img,
                                             caption=f"{message.from_user.id}|Тебе необходимо пройти каптчу!\nЧто изображено на картинке?",
                                             reply_markup=kb_captcha_1)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                 day=datetime.datetime.now().day,
                                                 month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1
                                                 )
                    if digit == 2:
                        img = open('bot/images/captcha_cucumber.jpg', 'rb')
                        await bot.send_photo(message.chat.id, photo=img,
                                             caption=f"{message.from_user.id}|Тебе необходимо пройти каптчу!\nЧто изображено на картинке?",
                                             reply_markup=kb_captcha_2)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                 day=datetime.datetime.now().day,
                                                 month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1
                                                 )

                    if digit == 3:
                        img = open('bot/images/captcha_grape.jpg', 'rb')
                        await bot.send_photo(message.chat.id, photo=img,
                                             caption=f"{message.from_user.id}|Тебе необходимо пройти каптчу!\nЧто изображено на картинке?",
                                             reply_markup=kb_captcha_3)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                 day=datetime.datetime.now().day,
                                                 month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1
                                                 )

                    if digit == 4:
                        img = open('bot/images/captcha_pizza.jpg', 'rb')
                        await bot.send_photo(message.chat.id, photo=img,
                                             caption=f"{message.from_user.id}|Тебе необходимо пройти каптчу!\nЧто изображено на картинке?",
                                             reply_markup=kb_captcha_4)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                 day=datetime.datetime.now().day,
                                                 month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1
                                                 )

                    if digit == 5:
                        img = open('bot/images/captcha_pretzel.jpg', 'rb')
                        await bot.send_photo(message.chat.id, photo=img,
                                             caption=f"{message.from_user.id}|Тебе необходимо пройти каптчу!\nЧто изображено на картинке?",
                                             reply_markup=kb_captcha_5)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                 day=datetime.datetime.now().day,
                                                 month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1
                                                 )

                    if digit == 6:
                        img = open('bot/images/captcha_cherry.jpg', 'rb')
                        await bot.send_photo(message.chat.id, photo=img,
                                             caption=f"{message.from_user.id}|Тебе необходимо пройти каптчу!\nЧто изображено на картинке?",
                                             reply_markup=kb_captcha_6)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                 day=datetime.datetime.now().day,
                                                 month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1
                                                 )

                    if digit == 7:
                        img = open('bot/images/captcha_banana.jpg', 'rb')
                        await bot.send_photo(message.chat.id, photo=img,
                                             caption=f"{message.from_user.id}|Тебе необходимо пройти каптчу!\nЧто изображено на картинке?",
                                             reply_markup=kb_captcha_7)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                 day=datetime.datetime.now().day,
                                                 month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1
                                                 )

                elif language_captcha[0][0] == 'gb':
                    if digit == 1:
                        img = open('bot/images/captcha_apple.jpg', 'rb')
                        await bot.send_photo(message.chat.id, photo=img,
                                             caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                             reply_markup=kb_captcha_1)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                 day=datetime.datetime.now().day,
                                                 month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1
                                                 )
                    if digit == 2:
                        img = open('bot/images/captcha_cucumber.jpg', 'rb')
                        await bot.send_photo(message.chat.id, photo=img,
                                             caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                             reply_markup=kb_captcha_2)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                 day=datetime.datetime.now().day,
                                                 month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1
                                                 )

                    if digit == 3:
                        img = open('bot/images/captcha_grape.jpg', 'rb')
                        await bot.send_photo(message.chat.id, photo=img,
                                             caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                             reply_markup=kb_captcha_3)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                 day=datetime.datetime.now().day,
                                                 month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1
                                                 )

                    if digit == 4:
                        img = open('bot/images/captcha_pizza.jpg', 'rb')
                        await bot.send_photo(message.chat.id, photo=img,
                                             caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                             reply_markup=kb_captcha_4)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                 day=datetime.datetime.now().day,
                                                 month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1
                                                 )

                    if digit == 5:
                        img = open('bot/images/captcha_pretzel.jpg', 'rb')
                        await bot.send_photo(message.chat.id, photo=img,
                                             caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                             reply_markup=kb_captcha_5)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                 day=datetime.datetime.now().day,
                                                 month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1
                                                 )

                    if digit == 6:
                        img = open('bot/images/captcha_cherry.jpg', 'rb')
                        await bot.send_photo(message.chat.id, photo=img,
                                             caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                             reply_markup=kb_captcha_6)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                 day=datetime.datetime.now().day,
                                                 month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1
                                                 )

                    if digit == 7:
                        img = open('bot/images/captcha_banana.jpg', 'rb')
                        await bot.send_photo(message.chat.id, photo=img,
                                             caption=f"{message.from_user.id}|You need to pass the captcha!\nWhat is shown in the picture?",
                                             reply_markup=kb_captcha_7)
                        time_now = datetime.datetime.now()
                        time_lose = time_now + datetime.timedelta(minutes=1)
                        database.add_user_captha(id_user=message.from_user.id, id_chat=message.chat.id, type=2,
                                                 day=datetime.datetime.now().day,
                                                 month=datetime.datetime.now().month,
                                                 year=datetime.datetime.now().year,
                                                 h1=datetime.datetime.now().hour, m1=datetime.datetime.now().minute,
                                                 s1=datetime.datetime.now().second,
                                                 h2=time_lose.hour, m2=time_lose.minute, s2=time_lose.second,
                                                 message_id=message.message_id + 1
                                                 )

@dp.message_handler(commands=['captcha'])
async def capctha_command(message: types.Message):
    if message.chat.id < 0:
        user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        user_id_is_admin = user_admin['status']
        if user_id_is_admin != 'member':
            keyboard_captcha = InlineKeyboardMarkup(row_width=4)
            keyboard_captcha_button1 = InlineKeyboardButton(text='Simple', callback_data='standart_captcha')
            keyboard_captcha_button2 = InlineKeyboardButton(text='Button', callback_data='highstandart_captcha')
            keyboard_captcha_button3 = InlineKeyboardButton(text='Word', callback_data='word_captcha')
            keyboard_captcha_button4 = InlineKeyboardButton(text='Math', callback_data='math_ex')
            keyboard_captcha.add(keyboard_captcha_button1, keyboard_captcha_button2, keyboard_captcha_button3, keyboard_captcha_button4)
            await message.answer(f"""
<b>Please, select the test type for the newcomers:</b>\n\n· <b>Simple</b> - bot will ask to send anything to the chat\n· <b>Word</b> - bot will aks to send word\n· <b>Button</b> - bot will ask to press a button-captcha\n· <b>Math</b> - bot will ask to pass the example""", reply_markup=keyboard_captcha, parse_mode='HTML')
        else:
            await message.reply(text='You do not have permission to do this!')


@dp.callback_query_handler(text='math_ex')
async def meth_ex_command(call: types.CallbackQuery):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    id_chat = database.chat_id_in_list_chats(chat_id=chat_id)[0][0]
    status = database.get_id_admin_in_list_admins(id_user=user_id, chat_id=id_chat)
    if status != []:
        await call.message.delete()
        database.update_type_captcha(id_chat=chat_id, type=4)
    else:
        await call.answer(text='You do not have permission to do this!')

@dp.callback_query_handler(text='word_captcha')
async def word_captcha_command(call: types.CallbackQuery):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    id_chat = database.chat_id_in_list_chats(chat_id=chat_id)[0][0]
    status = database.get_id_admin_in_list_admins(id_user=user_id, chat_id=id_chat)
    if status != []:
        await call.message.delete()
        database.update_type_captcha(id_chat=chat_id, type=3)
    else:
        await call.answer(text='You do not have permission to do this!')
@dp.callback_query_handler(text='highstandart_captcha')
async def highstandart_captcha_command(call: types.CallbackQuery):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    id_chat = database.chat_id_in_list_chats(chat_id=chat_id)[0][0]
    status = database.get_id_admin_in_list_admins(id_user=user_id, chat_id=id_chat)
    if status != []:
        await call.message.delete()
        database.update_type_captcha(id_chat=chat_id, type=2)
    else:
        await call.answer(text='You do not have permission to do this!')


@dp.callback_query_handler(text='standart_captcha')
async def standart_captcha_command(call: types.CallbackQuery):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    id_chat = database.chat_id_in_list_chats(chat_id=chat_id)[0][0]
    status = database.get_id_admin_in_list_admins(id_user=user_id, chat_id=id_chat)
    if status != []:
        await call.message.delete()
        database.update_type_captcha(id_chat=chat_id, type=1)
    else:
        await call.answer(text='You do not have permission to do this!')


@dp.callback_query_handler(text='captcha_win')
async def captcha_win_user(call: types.CallbackQuery):
    message_text = call.message.html_text
    correct_user = message_text.split('|')[0]
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    if int(correct_user) == user_id:
        user_captcha = database.check_user_captcha(id_user=user_id, id_chat=chat_id)
        print(user_captcha)
        time_now = datetime.datetime.now()
        nashe_vremya = datetime.datetime(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute,
                                         time_now.second)
        dedlain_kto_napisal_nam = datetime.datetime(user_captcha[0][6], user_captcha[0][5], user_captcha[0][4],
                                                    user_captcha[0][10], user_captcha[0][11], user_captcha[0][12])
        checking = int((dedlain_kto_napisal_nam - nashe_vremya).days)
        print(checking)
        if checking <= -1:
            await bot.kick_chat_member(chat_id=user_captcha[0][2], user_id=user_captcha[0][1])
            await bot.delete_message(chat_id=user_captcha[0][2], message_id=user_captcha[0][13])
            await bot.delete_message(chat_id=user_captcha[0][2], message_id=user_captcha[0][13])
            database.delete_captcha_user(id_user=user_captcha[0][1], id_chat=user_captcha[0][2])

        else:
            database.delete_captcha_user(id_user=user_id, id_chat=chat_id)
            await bot.delete_message(chat_id=chat_id, message_id=user_captcha[0][13])
            await bot.delete_message(chat_id=chat_id, message_id=user_captcha[0][13])
    else:
        pass

@dp.callback_query_handler(text='captcha_lose')
async def captcha_lose_user(call: types.CallbackQuery):
    message_text = call.message.html_text
    correct_user = message_text.split('|')[0]
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    if int(correct_user) == user_id:
        user_captcha = database.check_user_captcha(id_user=user_id, id_chat=chat_id)
        await bot.kick_chat_member(chat_id=user_captcha[0][2], user_id=user_captcha[0][1])
        await bot.delete_message(chat_id=user_captcha[0][2], message_id=user_captcha[0][13])
        await bot.delete_message(chat_id=user_captcha[0][2], message_id=user_captcha[0][13])
        database.delete_captcha_user(id_user=user_captcha[0][1], id_chat=user_captcha[0][2])
    else:
        pass

@dp.message_handler()
async def get_message_from_group(message: types.Message):
    if message.chat.id < 0:
        chat_id = message.chat.id
        info_chat = await bot.get_chat(chat_id=chat_id)
        creator_chat = await bot.get_chat_administrators(chat_id)
        for creator in creator_chat:
            if creator['status'] == 'creator':
                id_creator = creator['user']['id']
        id_chat = info_chat['id']
        title_chat = info_chat['title']
        invite_link = info_chat['invite_link']

        add_chat = database.check_chat_in_all_chats(chat_id=chat_id, name_chat=title_chat, link_chat=invite_link, creator=int(id_creator))
        if add_chat != False:
            await message.answer("Make sure @Redop_AntiSpam_bot is your chat administrator. To fully familiarize yourself with our telegram bot, you can click on the button to learn about our bot's features, inside the menu of our bot.")
        list_chat_admins = await bot.get_chat_administrators(chat_id=chat_id)
        for admin in list_chat_admins:
            user_id = admin['user']['id']
            first_name = admin['user']['first_name']
            status = admin['status']
            chat_id = id_chat
            id_chat_in_list_chat = database.chat_id_in_list_chats(chat_id=chat_id)[0][0]
            database.check_admins_in_list_chat(id_user=user_id, first_name=first_name, status=status, chat_id=id_chat_in_list_chat)


        user_captcha = database.check_user_captcha(id_user=message.from_user.id, id_chat=message.chat.id)
        if user_captcha == []:
            all_users = database.check_all_users_captcha()
            for user in all_users:
                time_now = datetime.datetime.now()
                dt1 = datetime.datetime(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute,
                                        time_now.second)
                dt2 = datetime.datetime(user[6], user[5], user[4], user[10], user[11], user[12])
                dt3 = int((dt2 - dt1).days)
                print(dt3)
                if dt3 < 0:
                    print(user)
                    await bot.kick_chat_member(chat_id=user[2], user_id=user[1])
                    await bot.delete_message(chat_id=user[2], message_id=user[13])
                    await bot.delete_message(chat_id=user[2], message_id=message.message_id)
                else:
                    pass

        else:
            type = database.get_type_captcha(id_chat=message.chat.id)[0][0]
            if type == 4:
                get_word = database.get_result_value(word=int(message.text))
                if get_word == []:
                    await bot.kick_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
                    await bot.delete_message(chat_id=message.chat.id, message_id=user_captcha[0][13])
                    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                else:
                    database.delete_captcha_user(id_user=message.from_user.id, id_chat=chat_id)
                    await bot.delete_message(chat_id=chat_id, message_id=user_captcha[0][13])
                    await bot.delete_message(chat_id=chat_id, message_id=message.message_id)


            if type == 3:
                get_word = database.get_word_value(word=message.text)
                if get_word == []:
                    await bot.kick_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
                    await bot.delete_message(chat_id=message.chat.id, message_id=user_captcha[0][13])
                    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

                else:
                    database.delete_captcha_user(id_user=message.from_user.id, id_chat=chat_id)
                    await bot.delete_message(chat_id=chat_id, message_id=user_captcha[0][13])
                    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

            else:
                user_id = message.from_user.id
                chat_id = message.chat.id
                captcha_type = database.get_type_captcha(id_chat=chat_id)[0][0]
                if captcha_type == 1:
                    time_now = datetime.datetime.now()
                    nashe_vremya = datetime.datetime(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute,
                                                     time_now.second)
                    dedlain_kto_napisal_nam = datetime.datetime(user_captcha[0][6], user_captcha[0][5], user_captcha[0][4],
                                                                user_captcha[0][10], user_captcha[0][11], user_captcha[0][12])
                    checking = int((dedlain_kto_napisal_nam - nashe_vremya).days)
                    print(checking)
                    if checking < 0:
                        await bot.kick_chat_member(chat_id=user_captcha[0][2], user_id=user_captcha[0][1])
                        await bot.delete_message(chat_id=user_captcha[0][2], message_id=user_captcha[0][13])
                        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                        database.delete_captcha_user(id_user=user_captcha[0][1], id_chat=user_captcha[0][2])


                    else:
                        database.delete_captcha_user(id_user=user_id, id_chat=chat_id)
                        await bot.delete_message(chat_id=chat_id, message_id=user_captcha[0][13])
                        await bot.delete_message(chat_id=chat_id, message_id=message.message_id)

            all_users = database.check_all_users_captcha()
            for user in all_users:
                time_now = datetime.datetime.now()
                dt1 = datetime.datetime(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute,
                                        time_now.second)
                dt2 = datetime.datetime(user[6], user[5], user[4], user[10], user[11], user[12])
                dt3 = int((dt2 - dt1).days)
                if dt3 < 0:
                    await bot.kick_chat_member(chat_id=user[2], user_id=user[1])
                    await bot.delete_message(chat_id=user[2], message_id=user[-1])
                    await bot.delete_message(chat_id=user[2], message_id=message.message_id)
                    database.delete_captcha_user(id_user=user[1], id_chat=user[2])

                else:
                    pass

        limition_chat = database.get_limition_chat(chat_id=message.chat.id)
        if limition_chat[0][2] == True:
            dt_string = datetime.datetime.now().strftime("%H:%M:%S")
            if (dt_string == "18:00:00"):  # Если строка с датой и временем равна строке с нужной датой и временем, то выводится дата и время
                await message.answer('Dear users, for your safety, do not give out your personal data')

        if limition_chat[0][1] == True: # Проверка на silence - мут всех кроме админов
            user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            user_id_is_admin = user_admin['status']
            if user_id_is_admin == 'member':
                await message.delete()

        if limition_chat[0][0] == True: # Проверка на ссылку в сообщении
            user_admin = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            user_id_is_admin = user_admin['status']
            if user_id_is_admin == 'member':
                if 'http' in message.text or 't.me' in message.text or '.com' in message.text or '.ru' in message.text or '.net' in message.text:
                    await message.delete()



@dp.message_handler()
async def warning_text():
    get_all_users_who_on_warning = database.get_all_warning()
    if get_all_users_who_on_warning == []:
        pass
    else:
        for chat in get_all_users_who_on_warning:
            try:
                language_captcha = database.get_language_captcha(id_chat=chat[0])
                if language_captcha == []:

                    await bot.send_message(chat_id=chat[0], text="""Dear users, your safety is important to us, so we recommend you not to post your personal information, as well as any other personal information. Do not click on third-party links not sent by the chat administrator.
            """)
                    await bot.send_message(chat_id=chat[0], text='Thank you for your attention and have a great day!')

                elif language_captcha[0][0] == 'ru':

                    await bot.send_message(chat_id=chat[0], text="""Уважаемые пользователи, для нас важна ваша безопасность, поэтому мы рекомендуем вам не размещать свою личную информацию, а также любую другую личную информацию. Не переходите по сторонним ссылкам, не присланным администратором чата.
                                """)
                    await bot.send_message(chat_id=chat[0], text='Спасибо за внимание и хорошего дня!')
                elif language_captcha[0][0] == 'gb':

                    await bot.send_message(chat_id=chat[0], text="""Dear users, your safety is important to us, so we recommend you not to post your personal information, as well as any other personal information. Do not click on third-party links not sent by the chat administrator.
                                """)
                    await bot.send_message(chat_id=chat[0], text='Thank you for your attention and have a great day!')
            except Exception as ex:
                continue

    await asyncio.sleep(120)

@dp.message_handler()
async def check_time_captcha():
    all_users = database.check_all_users_captcha() # все пользователи, получившие каптчу (наст. время)
    for user in all_users:
        time_now = datetime.datetime.now()
        datetime_now = datetime.datetime(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second)
        datetime_end = datetime.datetime(user[6], user[5], user[4], user[10], user[11], user[12]) # время, когда у пользователя истекает возможность пройти каптчу
        datetime_captcha = int((datetime_end - datetime_now).days) # алгоритм, позволяющий посчитать, сколько осталось до конца каптчи, если число меньше нуля - каптча истекла => бан
        if datetime_captcha < 0:
            try:
            # Происходит бан пользователя
                await bot.delete_message(chat_id=user[2], message_id=user[-1])
                await bot.kick_chat_member(chat_id=user[2], user_id=user[1])
                database.delete_captcha_user(id_user=user[1], id_chat=user[2])
            except Exception as ex:
                continue
        else:
            # Игнорируем
            pass

async def scheduler():
    # Рассылка команды warning
    aioschedule.every().day.at("00:00").do(warning_text)
    aioschedule.every().day.at("06:00").do(warning_text)
    aioschedule.every().day.at("12:00").do(warning_text)
    aioschedule.every().day.at("18:00").do(warning_text)

    # Проверка на истечение времени каптчи (каждые 30 минут)
    aioschedule.every().day.at("21:46").do(check_time_captcha)

    aioschedule.every().day.at("00:30").do(check_time_captcha)
    aioschedule.every().day.at("01:00").do(check_time_captcha)
    aioschedule.every().day.at("00:30").do(check_time_captcha)
    aioschedule.every().day.at("02:00").do(check_time_captcha)
    aioschedule.every().day.at("02:30").do(check_time_captcha)
    aioschedule.every().day.at("03:00").do(check_time_captcha)
    aioschedule.every().day.at("03:30").do(check_time_captcha)
    aioschedule.every().day.at("04:00").do(check_time_captcha)
    aioschedule.every().day.at("04:30").do(check_time_captcha)
    aioschedule.every().day.at("05:00").do(check_time_captcha)
    aioschedule.every().day.at("05:30").do(check_time_captcha)
    aioschedule.every().day.at("06:00").do(check_time_captcha)
    aioschedule.every().day.at("00:00").do(check_time_captcha)
    aioschedule.every().day.at("06:00").do(check_time_captcha)
    aioschedule.every().day.at("06:30").do(check_time_captcha)
    aioschedule.every().day.at("07:00").do(check_time_captcha)
    aioschedule.every().day.at("07:30").do(check_time_captcha)
    aioschedule.every().day.at("08:00").do(check_time_captcha)
    aioschedule.every().day.at("08:30").do(check_time_captcha)
    aioschedule.every().day.at("09:00").do(check_time_captcha)
    aioschedule.every().day.at("09:30").do(check_time_captcha)
    aioschedule.every().day.at("10:00").do(check_time_captcha)
    aioschedule.every().day.at("10:30").do(check_time_captcha)
    aioschedule.every().day.at("11:00").do(check_time_captcha)
    aioschedule.every().day.at("11:30").do(check_time_captcha)
    aioschedule.every().day.at("12:00").do(check_time_captcha)
    aioschedule.every().day.at("12:30").do(check_time_captcha)
    aioschedule.every().day.at("13:00").do(check_time_captcha)
    aioschedule.every().day.at("13:30").do(check_time_captcha)
    aioschedule.every().day.at("14:00").do(check_time_captcha)
    aioschedule.every().day.at("14:30").do(check_time_captcha)
    aioschedule.every().day.at("15:00").do(check_time_captcha)
    aioschedule.every().day.at("15:30").do(check_time_captcha)
    aioschedule.every().day.at("16:00").do(check_time_captcha)
    aioschedule.every().day.at("16:30").do(check_time_captcha)
    aioschedule.every().day.at("17:00").do(check_time_captcha)
    aioschedule.every().day.at("17:30").do(check_time_captcha)
    aioschedule.every().day.at("18:00").do(check_time_captcha)
    aioschedule.every().day.at("18:30").do(check_time_captcha)
    aioschedule.every().day.at("19:00").do(check_time_captcha)
    aioschedule.every().day.at("19:30").do(check_time_captcha)
    aioschedule.every().day.at("20:00").do(check_time_captcha)
    aioschedule.every().day.at("20:30").do(check_time_captcha)
    aioschedule.every().day.at("21:00").do(check_time_captcha)
    aioschedule.every().day.at("21:30").do(check_time_captcha)
    aioschedule.every().day.at("22:00").do(check_time_captcha)
    aioschedule.every().day.at("22:30").do(check_time_captcha)
    aioschedule.every().day.at("23:00").do(check_time_captcha)
    aioschedule.every().day.at("23:30").do(check_time_captcha)
    aioschedule.every().day.at("00:01").do(check_time_captcha)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def on_startup(dp):
    asyncio.create_task(scheduler())


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)