from prompt_toolkit import prompt
from prompt_toolkit import HTML as html
from prompt_toolkit import print_formatted_text as pft
from prompt_toolkit.styles import Style
import functions as f
from prompt_toolkit.cursor_shapes import CursorShape, ModalCursorShapeConfig
import os

key = True
style = Style.from_dict({
    "head":"#ffffff",
    "startsign":"#44cef6",
    "notice":"#ff2d51",
    "right":"#ffffff bg:#ff4777",
    "paragraph":"#00bc12",
    "word":"#f36838"
})

default = "./folder"
if not os.path.exists(default):
    os.makedirs(default)

pft(html("<b><head>Ameitsu FreeWriter alpha-0</head></b>"),style=style)

file = prompt(html("<startsign><b>Open file >>> </b></startsign>"),style=style)

while key:
   
    text = prompt(html("<startsign><b># </b></startsign>"),style=style,cursor=CursorShape.BLOCK)
    res = list(text.split())

    if res[0] == "write":
      f.writeline(str(file))
    if res[0] == "display":
       f.display()
    if res[0]=="clear":
       f.clear()
    if res[0]=="change":
        if len(res) != 2:
           pft(html("<b><notice>[AFW] Invalid command.</notice></b>"),style=style)
        else: 
            try:
                os.makedirs(res[1])
                default = res[1]
            except:
               pft(html("<b><notice>[AFW] Invalid route.</notice></b>"),style=style)

    if res[0]=="create" or res[0]=="new":
        f.create(default)
'''
    if res[0]=="Stop" or "S":
        break
        '''