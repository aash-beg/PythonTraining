import webbrowser
from datetime import datetime
chat = True
while chat:
    #chat application
    msg = input("Enter your message : ")

    if msg == "hello":
        print("Hello User")
    elif msg == "date":
        print(datetime.now().date().strftime('%d-%b-%y'))
    elif msg == "time":
        print(datetime.now().time().strftime('%H:%M:%S %p'))
    #elif msg[0:4] == 'open':
        #webbrowser.open(msg[5:len(msg)] + '.com')
    elif msg.startswith('open'):
        web = msg.split()[-1]
        webbrowser.open(web + '.com')
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")