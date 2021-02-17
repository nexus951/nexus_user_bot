from userbot import *
from userbot.utils import *
from userbot.cmdhelp import CmdHelp
from userbot.uniborgConfig import Config
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "N̸E̸X̸U̸S̸B̸O̸T̸ User"

PM_IMG = Config.ALIVE_PIC

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

pm_caption = "__**🔥🔥𝐧𝐞𝐱𝐮𝐬 υѕєявσт ιѕ ση ƒιяє🔥🔥**__\n\n"

pm_caption += (
    f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**『[{DEFAULTUSER}](tg://user?id={kraken})』**\n\n"
)

pm_caption += "n̾e̾x̾u̾s̾ Vêr§ïðñ: `1.15.0` \n"

pm_caption += "ꉣꌦ꓄꒻ꄲꋊ ꒦ꏂꋪꇙ꒐ꄲꋊ:      `3.7.4` \n"

pm_caption += f"N̸E̸X̸U̸S̸฿Ø₮ VɆⱤ₴łØ₦:  __**D.0**__\n"

pm_caption += f"sᴜᴅᴏ            : `{sudou}`\n"

pm_caption += "ꇙ꒤ꉣꉣꄲꋪ꓄ ꍌꋪꄲ꒤ꉣ  : [ᴊᴏɪɴ](https://t.me/nexus_user_bot)\n"

pm_caption += "𝙲𝚛𝚎𝚊𝚝𝚘𝚛    : [Click Here](https://t.me/nexus_here)\n\n"

pm_caption += "    [✨REPO✨](https://github.com/nexus951/nexus_user_bot) 🔹 [📜License📜](https://github.com/nexus951/nexus_user_bot/blob/main/LICENSE)"



@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()

CmdHelp("alive").add_command(
  'alive', None, 'Check weather the bot is alive or not'
).add_command(
  'nexus', None, 'Check weather yhe bit is alive or not. In your custom Alive Pic and Alive Msg if in Heroku Vars'
).add()
