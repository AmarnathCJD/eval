from Elsa.events import Sbot

@Ebot(pattern="^/eval ?(.*)")
async def ev(event):
 code = event.text.split(None, 1)[1]
 if not code:
    return
 
 
@Ebot(pattern="^/ping$")
async def p(event):
 await event.edit("Pong!")

