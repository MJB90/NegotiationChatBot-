from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from dataExtractor import extract_info

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():

    userText = request.args.get('msg')

    # payment = extract_info.run_extract_info(str(userText))
    #
    # msg = "you have a due of :" + str(payment) + " rupees"
    # return msg
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
