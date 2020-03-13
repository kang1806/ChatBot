from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request

import pymongo

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
                logic_adapters=['chatterbot.logic.BestMatch'],
                database_uri="mongodb://localhost:27017/chatbot"
                )

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["chatbot"]
mycol = mydb["training"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/training")
def training():
    return render_template("training.html")

@app.route("/getTrain")
def get_user_train():
        userTrain = request.args.get('msg')
        print (userTrain)
        mydict = { "Msg": userTrain }
        x = mycol.insert_one(mydict)
        return str(userTrain)



@app.route("/getResponse")
def get_bot_response():
    userText = request.args.get('msg')
    print (userText)
    bot_response = english_bot.get_response(userText)
    print (bot_response.confidence)
    if bot_response.confidence > 0.0005:
        return str(bot_response)
    else:
        return str("I dont understand this")




if __name__ == "__main__":
    app.debug = True
    app.run()
