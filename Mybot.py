import telebot
from googletrans import Translator
import mysql.connector
import mytoken

# from datetime import datetime
TOKEN = mytoken.TOKEN
myBot = telebot.TeleBot(TOKEN)
myDb = mysql.connector.connect(host='localhost',user='root',database='database_bot')
sql = myDb.cursor()
# waktusekarang = datetime.now()

class Mybot:
    def __init__(self):
        self.message

    @myBot.message_handler(commands=['start', 'help'])
    def start(message):
        teks = "😺\n" + "Halo @" + message.from_user.username + mytoken.menyapa + "💬\nAku dapat membantumu dengan perintah:\n\n" \
               + mytoken.mulai + mytoken.datasiswa + mytoken.gambar + mytoken.help + "\n\n------------------------ Creator: @rayfantio ------------------------"
        # Translator().translate(teks, dest='en')

        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['pic'])
    def pic(message):
        photo = open('img/kucing.jpg', 'br')
        myBot.send_photo(message.from_user.id, photo)

        myBot.reply_to(message, photo)

    @myBot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query = "select nipd,nama,kelas from tabel_siswa"
        sql.execute(query)
        data = sql.fetchall()
        jmldata = sql.rowcount
        kumpuldata = ''
        if(jmldata > 0):
            no = 0
            for x in data:
                no += 1
                kumpuldata = kumpuldata + str(x) + "\n"
                print(kumpuldata)
                kumpuldata = kumpuldata.replace("(","")
                kumpuldata = kumpuldata.replace(")","")
                kumpuldata = kumpuldata.replace("'","")
                kumpuldata = kumpuldata.replace(",", "|")
                print(kumpuldata)
        else:
            print("Data kosong")

        myBot.reply_to(message, str(kumpuldata))

print(myDb)
print("-- Bot sedang berjalan --")
myBot.polling(none_stop=True)
