from prompt_toolkit import prompt
from prompt_toolkit import HTML as html
from prompt_toolkit import print_formatted_text as pft
from prompt_toolkit.styles import Style

style = Style.from_dict({
     "head":"#ffffff",
    "startsign":"#44cef6",
    "notice":"#ff2d51",
    "right":"#ffffff bg:#ff4777",
    "paragraph":"#00bc12",
    "word":"#f36838"
})

def writeline():
    pft(html("<success>[AFE] Enter writing mode now.</success>"),style=style)
    while True:
        content = prompt(html("<startsign><b>>>> </b></startsign>"),style=style)
        file = open("paper","a")
        if content == "\e":
            break
        file.write(content+"\n")
        file.close()

def display():
    file = open("paper","r")
    content = []
    for lines in file.readlines():
        line = lines.strip()
        content.append(line)
        print(line)
    if len(content)==0:

        pft(html("<notice>[AFE] Nothing here now.</notice>"),style=style)
    file.close()

def clear():
    file = open("paper","w+")
    file.close()
    pft(html("<notice>[AFE] Cleared paper.</notice>"),style=style)

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

            
