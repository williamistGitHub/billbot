import discord
import os

from billbot import cmd_greytext

intents = discord.Intents.none()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)


@tree.command(description="make a funny")
async def greytext(interaction: discord.Interaction, text: str):
    if len(text) > 2048:
        await interaction.response.send_message("womp womp (text recieved longer than 2048 characters)", ephemeral=True)
        return
    await interaction.response.send_message(file=discord.File(fp=cmd_greytext.do(text), filename='b1ll_w4s_h3r3.gif'))


@client.event
async def on_ready():
    print("Syncing slash commands, hold tight.")
    await tree.sync()
    print("Setting activity")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="your life rot away"))
    print("Done!")

client.run(os.environ["BOT_TOKEN"], reconnect=False)
