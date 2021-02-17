import asyncio

from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="test ?(.*)"))
@bot.on(sudo_cmd(pattern="test ?(.*)", allow_sudo=True))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):

        await edit_or_reply(event, "`Testing N̸E̸X̸U̸S̸B̸O̸†`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing N̸E̸X̸U̸S̸B̸O̸†.`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing N̸E̸X̸U̸S̸B̸O̸†..`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing N̸E̸X̸U̸S̸B̸O̸†...`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing N̸E̸X̸U̸S̸B̸O̸†....`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing N̸E̸X̸U̸S̸B̸O̸†.....`")
        await asyncio.sleep(2)
        await edit_or_reply(event, "__Testing Successful__")
        await asyncio.sleep(2)
        await edit_or_reply(event, "`Generating Output`\nPlease wait")
        await asyncio.sleep(2)
        await edit_or_reply(event, "__Output Generated Successfully__")
        await asyncio.sleep(2)
        await edit_or_reply(event, "**SAVING OUTPUT TO NEXUSBOT LOCAL DATABASE**")
        await asyncio.sleep(3.5)
        await edit_or_reply(event, 
            "Your[N̸E̸X̸U̸S̸B̸O̸†](https:/t.me/nexus_user_bot) is working Fine...\n       Join @nexus_user_bot For Any Help......"
        )

CmdHelp("test").add_command(
  "test", None, "Test wether your bot is running or not."
).add()