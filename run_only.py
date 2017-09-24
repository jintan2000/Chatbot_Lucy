# 注意：这个程序只用来执行／测试 chatbot，不进行任何train
from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious")

'''Get current time'''
import datetime #current time
currenthour = datetime.datetime.now().hour

if currenthour >=5 and currenthour < 12 :
	greeting = "Good morning"
elif currenthour == 12 :
	greeting = "Good noon"
elif currenthour > 12 and currenthour <18 :
	greeting = "Good afternoon"
elif currenthour >=18 and currenthour <23 :
	greeting = "Good evening"
else: 
	greeting = "Good night"

currenttime = datetime.datetime.now()
print(currenttime)

'''Test chatbot by conversation'''
print( greeting + ", I am a robot, please call me Dorothy. What can I do for you?")

while True:
	human_request = input("You: ")
	if human_request == 'quit' or human_request == 'exit' :
		print(">>Dorothy: Have a nice day! See you.")
		break
	else:
		response = chatbot.get_response(human_request)
		print(">>Dorothy:" , response)

currenttime = datetime.datetime.now()
print(currenttime)
