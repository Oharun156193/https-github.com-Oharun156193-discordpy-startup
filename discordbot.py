from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='/')


client = discord.Client()


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
    hour = minits // 60
    min = minits % 60
    return f"{int(hour)}:{int(min)}:{int(second)}"


 # イベントを受信するための構文（デコレータ）
@client.event
async def on_message(message):
    
　#メンバーの発言を除外
    if message.author.member:
        return

　　　#時間を更新する間隔[ms]
    INTERVAL = 1000

　　　#開始時刻記録
    start_time = 0

　　　# 時間計測中フラグ
    start_flag = False

　　　# afterメソッドのID
    after_id = 0

　　　#時間更新の関数
    def update_time():
        global start_time
        global after_id
    
　　　　　#update_timeを再度INTERVAL[ms]後に実行する
        after_id = after(INTERVAL, update_time)
    
　　　　　#現在時刻の取得
        now_time = time.time()   
    
　　　　　#計測時間の計算
        elapsed_time = now_time - start_time
    
　　　　　#記録した開始時刻をチャットでシステムメッセージに送信
        await message.channel.send(f"{start_time}"}
                                
　　　　　#計算結果をチャットでシステムメッセージに送信
        time_result = convert(elapsed_time)   
        print(f"Time：{time_result}")
        await message.edit({time_result})
                                
　　#通話お知らせbotが「通話開始」
    if message.content == '/start':
　　　　#スタートの処理
        def start():
            global start_flag
            global start_time
            global after_id
       #計測中でなければ時間計測開始
            if not start_flag:
        
        # 計測中フラグをON
                start_flag = True

        # 計測開始時刻を取得
                start_time = time.time()

        # update_timeをINTERVAL[ms] 後に実行
                after_id = after(INTERVAL, update_time)

     #以下の処理は一度行ったら繰り返さない
     #(送信したメッセージを現在時刻から記録した開始時刻を引いた結果に編集)
　　　　　　
　　#通話お知らせbotが「通話終了」と発言
     if message.content == '通話終了':
    # ストップボタンの処理
         def stop():
            global start_flag
            global after_id

    # 計測中の場合は計測処理を停止
            if start_flag:

        # update_time関数の呼び出しをキャンセル
                after_cancel(after_id)

        # 計測中フラグをオフ
                start_flag = False
　　　#記録された終了時刻とストップウォッチ結果をチャットでシステムメッセージに送信
                
    

@client.event
async def on_voice_state_update(member, before, after):
    
    
    
token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
