"""Check if userbot awake or not . 



"""

#make by @nexus_here don't kang this plugin

# if you kang then keep credits

#cReDiTs - ROLDEX⚡⚡

import os

import time

import asyncio

from telethon import events

from telethon.tl.types import ChannelParticipantsAdmins

from userbot import ALIVE_NAME, StartTime, CMD_HELP

from userbot.utils import admin_cmd

from telethon import version

from math import ceil

import json

import random

import re

from telethon import events, errors, custom

import io

from platform import python_version, uname



ALIVE_PIC = Config.ALIVE_PIC

if ALIVE_PIC is None:

  ALIVE_PIC = "https://telegra.ph/file/0e36b02061064b7229e3b.jpg"





DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "N̸E̸X̸U̸S̸B̸O̸T̸ USER"



global ghanti

        

#make by 	NEXUS             

#@command(outgoing=True, pattern="^.awake$")

@borg.on(admin_cmd(pattern=r"awake"))

async def amireallyalive(awake):

   """ For .awake command, check if the bot is running.  """

   tag = borg.uid

   ALIVE_MESSAGE= " ⚡⚡ NEXUS USER BOT 🔥  IS ON 🔥 FIRE 🔥 \n\n"

   ALIVE_MESSAGE += "🔥🔥 SYSTEM STATUS🔥🔥\n"

   ALIVE_MESSAGE += "🔥🔥TELETHON VERSION🔥🔥 : 6.0.9\n"

   ALIVE_MESSAGE += "🔥🔥 NEXUS VERSION🔥🔥 :   1.0.9\n"

   ALIVE_MESSAGE += f"🔥🔥 SYSTEM🔥🔥 : DATABASE OK\n"

   ALIVE_MESSAGE += f"🔥 MY BOSS 🔥: {DEFAULTUSER}\n"

   ALIVE_MESSAGE += "🔥🔥MADE BY🔥🔥 : [NEXUS](t.me/nexus_here) \n\n"

   ALIVE_MESSAGE += "⚡⚡Deploy N̸E̸X̸U̸S̸B̸O̸T̸⚡⚡ : [REPO](https://github.com/nexus951/nexus_user_bot)\n"   

   await awake.delete() 

   await borg.send_file(awake.chat_id, ALIVE_PIC,caption=ALIVE_MESSAGE)


#make by NEXUS
