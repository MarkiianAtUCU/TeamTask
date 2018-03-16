from main import *
import os

menu = """
1) - Add Client
2) - Add Mail
3) - Send All
4) - Mail Number
5) - Clients info
6) - Quit
"""
clients = []
mails = MailBox()


def create_client(lst):
    name = input("[Client name] > ")

    age = input("[Client age] >")
    while not age.isdigit() and not (1 < int(age) < 110):
        print("[Error] Enter integer")
        age = input("[Client age] > ")
    age = int(age)

    sex = input("[Client sex] (male, female)> ")
    while sex not in ["male", "female"]:
        print("Sex must be male or femele")
        sex = input("[Client sex] (male, female)> ")
    email = input("[Client email] > ")
    other = input("[Client short info] >")
    lst.append(Client(name, age, sex, email, other))


def create_mail(clients, box):
    text = input("[Email text] > ")
    for i in range(len(clients)):
        print(str(i+1)+") "+clients[i].less_info())
    n = input("[Client number] >")
    while n not in map(lambda x: str(x), list(range(1, len(clients)+1))):
        print("Wrong client number")
        n = input("[Client number] >")

    t = input("[Mail type] (1-Birthday 2-Work_mail, 3-Sail)> ")
    while t not in ["1", "2", "3"]:
        print("Wrong mail type")
        t = input("[Mail type] (1,2,3)> ")
    box.add_mail_info(MailInfo(clients[int(n)-1], t, text))

while True:
    os.system("cls")
    print(menu)
    command = input("[o] > ")
    if command in ["1", "2", "3", "4", "5", "6"]:
        if command == "1":
            create_client(clients)
        elif command == "2":
            create_mail(clients, mails)
        elif command == "3":
            try:
                try:
                    login=input("[login] > ")
                    password=input("[password] > ")
                    mails.send_all(login, password)
                except smtplib.SMTPAuthenticationError:
                    print("Wrong emeil or password")
            except smtplib.SMTPRecipientsRefused:
                print("Wrong email")
            else:
                print("Sending done!")
        elif command == "4":
            print("Number of mails", len(mails.inf))
        elif command == "5":
            for i in clients:
                print(i)
                print("=================")
        elif command == "6":
            break
    else:
        print("Wrong Input")
    input()
print("Good-bye!")
