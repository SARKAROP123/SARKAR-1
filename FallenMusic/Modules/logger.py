# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from pyrogram import filters

import config
from FallenMusic import app
from FallenMusic import SUDOERS
from FallenMusic.utils.database import add_off, add_on
from FallenMusic.utils.decorators.language import language

# Commands
LOGGER_COMMAND = get_command("LOGGER_COMMAND")


@app.on_message(filters.command(LOGGER_COMMAND) & SUDOERS)
@language
async def logger(client, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await add_on(config.LOG)
        await message.reply_text(_["log_2"])
    elif state == "disable":
        await add_off(config.LOG)
        await message.reply_text(_["log_3"])
    else:
        await message.reply_text(usage)
