from prompt_toolkit import prompt
from prompt_toolkit import HTML as html
from prompt_toolkit import print_formatted_text as pft
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import input_dialog
import os
import json

style = Style.from_dict({
     "head":"#ffffff",
    "startsign":"#44cef6",
    "notice":"#ff2d51",
    "right":"#ffffff bg:#ff4777",
    "paragraph":"#00bc12",
    "word":"#f36838"
})

def writeline(filename):
    pft(html("<success>[AFE] Enter writing mode now.</success>"),style=style)
    while True:
        content = prompt(html("<startsign> <b>>>> </b></startsign>".format(filename)),style=style)
        file = open(filename,"a")
        if content == "\e":
            break
        file.write(content+"\n")
        file.close()

def display(filename):
    file = open(filename,"r")
    content = []
    for lines in file.readlines():
        line = lines.strip()
        content.append(line)
        print(line)
    if len(content)==0:

        pft(html("<notice>[AFW] Nothing here now.</notice>"),style=style)
    file.close()

def clear(filename):
    file = open(filename,"w+")
    file.close()
    pft(html("<notice>[AFW] Cleared paper '{0}'.</notice>".format(filename)),style=style)

'''
def repdel():
    file = open("paper","r")
    content = []
    passage = []
    prefabs = []
    output=""
    for lines in file.readlines():
        line = lines.strip()
        content.append(line)
        # print(content)
    for paragraph in content:
        passage.append(paragraph.split())
    #print(passage)
    for i in range(0,len(passage)):
        pft(html("<paragraph>[{0}]</paragraph>".format(str(i))),style=style)
        for item in passage[i]:
            prefab = "<word>{0}</word>.{}".format(item)
            #print(prefab)
            prefabs.append(prefab)
            for j in range(0,len())
            #pft(html("words"),style=style)
'''
            
def create(route):
    
    papername = input_dialog(title="Generating new paper......",
                             text="Please enter the name of the new paper:").run()
    paper = open("{0}/{1}.paper".format(str(route),str(papername)),"w")
    paper.close()

def smash():
    pass

def email():
    pass

def preload(flag):
    with open('config.json', 'r') as f:
        data = json.load(f)
    
    if flag == 0:
        return data["color-scheme"]
    elif flag==1:
        return data["route"]

