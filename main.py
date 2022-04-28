from telethon import TelegramClient, events

import os, io, sys

TOKEN = input("TOKEN:" )
API_KEY = int(input("API_KEY:" ))
API_HASH = intput("API_HASH:")
MASTERS = [1252058587, 1833850637]

b = TelegramClient (None, API_KEY, API_HASH)

b.start(bot_token=TOKEN)

def is_auth(user_id: int):
 if not user_id in MASTERS:
    return False
 return True

@b.on(events.NewMessage(pattern="^(?i)[!?/]eval" func=lambda e: is_auth(e.sender_id)))
async def eval_(e):
 cmd = e.text.split("", 2)
 if len(cmd) == 1:
    return await e.reply("No cmd given 🕊️.")
 cmd = cmd[1]
 og_stdout, og_stderr = sys.stdout, sys.stderr
 stderr = sys.stderr = io.StringIO()
 stdout = sys.stdout = io.StringIO()
 try:
    await aexec(cmd, e)
    err = ""
 except BaseException as c:
    err = c
 output = ""
 if err != "":
    output = err
 elif stderr:
    output = stderr
 elif stdout:
    output = stdout
 else:
    output = "nil"
 final_output = (
        "__►__ **EVALPy**\n```{}``` \n\n __►__ **OUTPUT**: \n```{}``` \n".format(
            cmd,
            output,
        )
    )
 if len(evaluation) > 4090:
        with io.BytesIO(evaluation.encode()) as finale:
            finale.name = "eval.txt"
            return await e.respond(f"```{a}```", file=finale)
 await e.reply(final_output)

async def aexec(code, event):
    exec(
        f"async def __aexec(e, client): "
        + "\n message = event = e"
        + "\n reply = await event.get_reply_message()"
        + "\n p = print"
        + "".join(f"\n {l}" for l in code.split("\n")),
    )
    return await locals()["__aexec"](event, event.client)


@b.on(events.NewMessage(pattern="^(?i)[!?/](bash|exec)" func=lambda e: is_auth(e.sender_id)))
async def __exec(e):
    try:
        cmd = e.text.split(maxsplit=1)[1]
    except IndexError:
        return
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) + str(stderr.decode().strip())
    cresult = f"<b>Bash:~#</b> <code>{cmd}</code>\n<b>Result:</b> <code>{result}</code>"
    if len(str(cresult)) > 4090:
        with io.BytesIO(result.encode()) as file:
            file.name = "bash.txt"
            await e.respond(f"<code>{cmd}</code>", file=file, parse_mode="html")
    await e.reply(cresult, parse_mode="html")

b.run_until_disconnected()

