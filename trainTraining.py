from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
                logic_adapters=['chatterbot.logic.BestMatch'],
                database_uri="mongodb://localhost:27017/chatbot"
                )
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.training")
