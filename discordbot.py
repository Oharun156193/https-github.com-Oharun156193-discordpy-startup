from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

    
import time


def convert(sec):
    minits = sec // 60
    second = sec % 60
    milli_sec = (second - int(second)) * 1000
    hour = minits // 60
    min = minits % 60
    return f"{int(hour)}:{int(min)}:{int(second)}:{int(milli_sec)}"


@client.event
async def on_message(message):
    # メッセージ送信者がmemberだった場合は無視する
    if message.author.member:
        return
    # 「/start」と発言したら「にゃーん」が返る処理
    if message.content == '/start':
        start_signal = input('Push "ENTER" to Start')
        start_time = time.time()
        await message.channel.send(start_time)
    #通話終了と発言したら終わった時間を表示する
    if message.content == '通話終了':
    stop_signal = input('Push "ENTER" to Stop')
    stop_time = time.time()
    result = stop_time - start_time
    print(f"Stop Time：{result:.3f} sec")
    

@client.event
async def on_voice_state_update(member, before, after):
    
    
    
token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
