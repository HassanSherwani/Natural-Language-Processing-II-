from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def setup():
    chatbot = ChatBot('Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    trainer='chatterbot.trainers.ListTrainer')
    trainer = ListTrainer(chatbot)
    for file in os.listdir('data/'):
        convData = open(r'data/' + file,encoding='latin-1').readlines()
        #chatbot.set_trainer(ListTrainer)
        #chatbot.train(convData)
        trainer.train(convData)
        #print("Training completed")


setup()
