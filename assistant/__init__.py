# ElonMusk - UserBot
# Copyright (C) 2020 TeamElonmusk
#
# This file is a part of < https://github.com/Elonmusk-1/Elon-Musk-Bot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from pyElonmusk import *
from pyElonmusk.dB.database import Var
from pyElonmusk.functions.all import *
from telethon import Button, custom

from strings import get_languages, get_string

OWNER_NAME = elonmusk_bot.me.first_name
OWNER_ID = elonmusk_bot.me.id


async def setit(event, name, value):
    try:
        udB.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button
