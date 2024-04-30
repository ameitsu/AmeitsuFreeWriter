from prompt_toolkit import prompt
from prompt_toolkit import HTML as html
from prompt_toolkit import print_formatted_text as pft
from prompt_toolkit.styles import Style
import functions as f
from prompt_toolkit.cursor_shapes import CursorShape, ModalCursorShapeConfig
 

key = True
style = Style.from_dict({
    "head":"#ffffff",
    "startsign":"#44cef6",
    "notice":"#ff2d51",
    "right":"#ffffff bg:#ff4777",
    "paragraph":"#00bc12",
    "word":"#f36838"
})
pft(html("<b><head>Ameitsu FreeWriter alpha-0</head></b>"),style=style)
while key:
   
    text = prompt(html("<startsign><b># </b></startsign>"),style=style,cursor=CursorShape.BLOCK)
    res = list(text.split())

    if res[0] == "write":
      f.writeline()
    if res[0] == "display":
       f.display()
    if res[0]=="clear":
       f.clear()
'''
    if res[0]=="Stop" or "S":
        break
        '''