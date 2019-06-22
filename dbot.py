import discord
import asyncio
import datetime
import datetime

client = discord.Client()
def timecode():
    now = datetime.datetime.now() # 現在の日時を取得
    dtx=now.weekday()
    sny=str(now.year)
    snm=str(now.month)
    snd=str(now.day)
    snh=str(now.hour)
    snn=str(now.minute)
    sns=str(now.second)
    if dtx==0:
        dtt="月"
    elif dtx==1:
        dtt="火"
    elif dtx==2:
        dtt="水"
    elif dtx==3:
        dtt="木"
    elif dtx==4:
        dtt="金"
    elif dtx==5:
        dtt="土"
    elif dtx==6:
        dtt="日"
    return sny,snm,snd,snh,snn,sns,dtt,dtx

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!date'):
        await asyncio.sleep(1)
        tcode=timecode()
        await client.send_message(message.channel,tcode[0]+"年"+tcode[1]+"月"+tcode[2]+"日"+"("+tcode[6]+")")
        await client.send_message(message.channel,tcode[3]+"時"+tcode[4]+"分"+tcode[5]+"秒")

    elif message.content.startswith('!schedule'):
        await asyncio.sleep(1)
        sny,snm,snd,snh,snn,sns,dtt,dtx=timecode()
        tcode=sny,snm,snd,snh,snn,sns,dtt
        msgdata=message.content
        if msgdata[10:]=="Mon":
            dtx=0
        elif msgdata[10:]=="Tue":
            dtx=1
        elif msgdata[10:]=="Wed":
            dtx=2
        elif msgdata[10:]=="Thu":
            dtx=3
        elif msgdata[10:]=="Fri":
            dtx=4
        elif msgdata[10:]=="Sat":
            dtx=5
        elif msgdata[10:]=="Sun":
            dtx=6
        elif len(msgdata)==9:
            dtx=dtx
        elif (len(msgdata)==11)&(int(msgdata[10])<7):
            ddtx=int(msgdata[10])
            dtx=(dtx+ddtx)%7
            
        if dtx==0:
            await client.send_message(message.channel,"月曜時間割")
        elif dtx==1:
            await client.send_message(message.channel,"火曜時間割")
        elif dtx==2:
            await client.send_message(message.channel,"水曜時間割")
        elif dtx==3:
            await client.send_message(message.channel,"木曜時間割")
        elif dtx==4:
            await client.send_message(message.channel,"金曜時間割")
        else:
            await client.send_message(message.channel,"404 Not Found")

    elif message.content.startswith('!help'):
        await asyncio.sleep(1)
        await client.send_message(message.channel,"コマンドの前には!をつけてください。\n\nhelp:ヘルプ(このコマンド)\ndate:現在時刻を表示\nschedule[x]:x日後 or x曜日の時間割を表示\n(xに関する詳細はsparaを参照)")
    elif message.content.startswith('!spara'):
        await asyncio.sleep(1)
        await client.send_message(message.channel,"int型の場合x日後の時間割を表示\n数値は0~6まで(指定しないと0)\n\nchar型の場合x曜日の時間割を表示\n文字はSun,Mon,Tue,Wed,Thu,Fri,Satの7パターン")


client.run('kye')
