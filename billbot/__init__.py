#     billbot - a very random discord bot
#     Copyright (C) 2023  williamist
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as published
#     by the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

import discord
import os

from billbot import cmd_greytext, cmd_1984ify

intents = discord.Intents.none()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)


@tree.command(description="make a funny")
async def greytext(interaction: discord.Interaction, text: str):
    if len(text) > 2048:
        await interaction.response.send_message("womp womp (text recieved longer than 2048 characters)", ephemeral=True)
        return
    await interaction.response.send_message(file=discord.File(fp=cmd_greytext.do(text), filename='b1ll_w4s_h3r3.gif'))


@tree.command(name="1984ify", description="by george orwell")
async def _1984ify(interaction: discord.Interaction, img: discord.Attachment):
    # make sure img is actually an image lol
    if "image" not in img.content_type:
        await interaction.response.send_message("womp womp (images & gifs only please <3)", ephemeral=True)
        return
    await interaction.response.send_message(file=discord.File(fp=cmd_1984ify.do(await img.read()), filename='b1ll_w4s_h3r3.gif'))


@client.event
async def on_ready():
    print("Syncing slash commands, hold tight.")
    await tree.sync()
    print("Setting activity")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="your life rot away"))
    print("Done!")


def go():
    client.run(os.environ["BOT_TOKEN"], reconnect=False)


if __name__ == "__main__":
    go()
