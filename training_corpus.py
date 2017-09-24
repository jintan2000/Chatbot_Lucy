# This program is only training chatbot by some specific corpus.w
from chatterbot import ChatBot
#from chatterbot.response_selection import get_most_frequent_response
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Training a corpus data and testing",
    #response_selection_method=get_most_frequent_response
        logic_adapters=[
        "chatterbot.logic.BestMatch"
    ]

    )

''' Train the chatbot by corpus data'''

chatbot.set_trainer(ChatterBotCorpusTrainer)

#chatbot.train("chatterbot.corpus.english")
chatbot.train("chatterbot.corpus.chinese")

