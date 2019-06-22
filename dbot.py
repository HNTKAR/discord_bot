#-*- coding:utf-8 -*-
import discord
import asyncio
import datetime

datec=["月","火","水","木","金","土","日"]
schedulelist=["曜日時間割"
,"火曜日時間割"
,"水曜日時間割"
,"木曜日時間割"
,"金曜日時間割"
,"404 Not Found"
,"404 Not Found"]
newinfo="コマンドの日本語化\n特定の言葉に反応するように改良"

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
    return sny,snm,snd,snh,snn,sns,dtx

def is_me(m):
    return m.author == client.user

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    msgdata=message.content

    if msgdata.find('!時刻')!=-1:
        await asyncio.sleep(1)
        tcode=timecode()
        dtx=tcode[6]
        await client.send_message(message.channel,tcode[0]+"年"+tcode[1]+"月"+tcode[2]+"日"+"("+datec[dtx]+")")
        await client.send_message(message.channel,tcode[3]+"時"+tcode[4]+"分"+tcode[5]+"秒")
    elif msgdata.find('!授業時間')!=-1:
        await asyncio.sleep(1)
        await client.send_message(message.channel,"1・2校時目:\t9:10~10:40\n3・4校時目:\t10:50~12:20\n5・6校時目:\t13:05~14:35\n7・8校時目:\t14:45~16:15")
    elif msgdata.find('!時間割')!=-1:
        await asyncio.sleep(1)
        sny,snm,snd,snh,snn,sns,dtx=timecode()
        if len(msgdata)>8:
            await client.send_message(message.channel,"int型の場合x日後の時間割を表示\n数値は1桁(指定しないと0)\n\nchar型の場合x曜日の時間割を表示\n文字はSun,Mon,Tue,Wed,Thu,Fri,Satの7パターン")
        else:
            if msgdata[5:]=="Mon":
                dtx=0
            elif msgdata[5:]=="Tue":
                dtx=1
            elif msgdata[5:]=="Wed":
                dtx=2
            elif msgdata[5:]=="Thu":
                dtx=3
            elif msgdata[5:]=="Fri":
                dtx=4
            elif msgdata[5:]=="Sat":
                dtx=5
            elif msgdata[5:]=="Sun":
                dtx=6
            elif len(msgdata)==4:
                dtx=dtx
            elif len(msgdata)==6:
                ddtx=int(msgdata[5])
                dtx=(dtx+ddtx)%7
            await client.send_message(message.channel,schedulelist[dtx])

    elif msgdata.find('なんなん')!=-1:
        await asyncio.sleep(1)
        await client.send_message(message.channel,"( `o´ )ぎんなん")


    elif msgdata.find('xxx')!=-1:
        await asyncio.sleep(1)
        await client.send_message(message.channel,"xxx!!")
        with open('/home/pi/Desktop/mypython/fuck.jpg', 'rb') as f:
            await client.send_file(message.channel, f)
            
    elif msgdata.find('!fileserver')!=-1:
        urls=msgdata[12:]
        urls="/home/pi/Desktop/mypython/"+urls
        await asyncio.sleep(1)
        with open(urls, "rb") as f:
            await client.send_file(message.channel, f)

    elif message.content.startswith('!program'):
        await asyncio.sleep(1)
        await client.send_message(message.channel,"For you!!")
        with open('/home/pi/Desktop/mypython/program.py', 'rb') as f:
            await client.send_file(message.channel, f)
            
    elif msgdata.find("ハム太郎")!=-1:
        await asyncio.sleep(1)
        await client.send_message(message.channel,"全くもってその通りなのだ！！！！！！")
            

    elif msgdata.find('xx部')!=-1:
        await asyncio.sleep(1)
        await client.send_message(message.channel,"song")
        
        
    elif msgdata.find('!help')!=-1:
        await asyncio.sleep(1)
        await client.send_message(message.channel,"[!help]:ヘルプ(このコマンド)\n\n[!時刻]:現在時刻を表示\n\n[!授業時間]:授業の開始時間と終了時間を表示\n\n[!時間割 [x]]:x日後 or x曜日の時間割を表示\n\(xに関する詳細は[!時間割help]を参照)\n\n[!BOTclear [x]]:xコメント前までのBOTのコメントを削除\n(デフォルトでは100コメント前まで遡る)\n\n[!clear [x]]:xコメント前までの全てのコメントを削除\n(デフォルトでは100コメント前まで遡る)\n\n\n※[!program]:プログラムの表示")

    elif msgdata.find('!BOTclear')!=-1:
        await asyncio.sleep(1)
        try:
            delint=int(msgdata[10:])
        except:
            delint=100
        deleted = await client.purge_from(message.channel, limit=delint, check=is_me)
        await client.send_message(message.channel, ' {}個のBOTのコメントを削除しました。'.format(len(deleted)))

    elif msgdata.find('!clear')!=-1:
        await asyncio.sleep(1)
        try:
            delint=int(msgdata[7:])
        except:
            delint=100
        deleted = await client.purge_from(message.channel, limit=delint, check=None)#is_me)
        await client.send_message(message.channel, ' {}個のコメントを削除しました。'.format(len(deleted)))

client.run('kye')