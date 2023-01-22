from arsein import Messenger 
from colorama import Fore as f
from datetime import datetime
from os import system 
import pyfiglet 


timer = datetime.now()
system("clear")

text = pyfiglet.figlet_format("H S L", font='isometric1')+"\n"+timer.strftime(f"{f.BLUE}   [ {f.YELLOW}%H {f.BLUE}: {f.YELLOW}%M {f.BLUE}: {f.YELLOW}%S {f.BLUE}]")+"\n"+f"{f.RED}<>"*40

print(f.RED,text)

print("")

auth = str(input(f"{f.BLUE}Enter Auth {f.RED}>>>{f.YELLOW} "))

print("")

link = str(input(f"{f.BLUE}Enter The Link Gap {f.RED}>>>{f.YELLOW} "))

print("")

msg = str(input(f"{f.BLUE}Enter The Message Will Be Send To Gap {f.RED}>>>{f.YELLOW} "))

print("")

bot = Messenger(auth)

group_name=bot.joinGroup(link)['data']['group']['group_title']


group_member=bot.joinGroup(link)['data']['group']['count_members']

guid = bot.joinGroup(link)['data']['group']['group_guid']


print(f"{f.RED}Group name :{f.CYAN} {group_name}")

print("")

print(f"{f.RED}Group guid : {f.CYAN}{guid}")
print("")

print(f"{f.RED}Group members : {f.CYAN}{group_member}")

print("")

num = 0

while (1):
    num += 1
    guid = bot.joinGroup(link)['data']['group']['group_guid']
    print(f"{f.RED}Join")
    bot.sendMessage(guid,msg)
    print(f"{f.GREEN}Message Was Sended To Gap {f.YELLOW}{num}")
    bot.leaveGroup(guid)
    print(f"{f.BLUE}Left The Gap")
    
