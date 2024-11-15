token_input = input('Токен: ')
prefix_input = input('Префикс: ')

import discord
from discord.ext import commands
import asyncio
import random

bot = commands.Bot(command_prefix=prefix_input, self_bot=True, help_command=None)

texts = ['слышь сын шлюхи', 'маму твою ебал', 'мама в гробике отдыхает?', 'щас к тебе прийдёт твой же отчим и выебет тебя, сын шлюхи дохлой', 'гроб + твоя мама = реальность', 'сын фермы', 'найк про', 'пидор ты', 'вскройся уёбище', 'сын уёбищя', 'какая семья такой и ты', 'ракушка у тя', 'ракушка у твоего бати', 'щовель у тя', 'сельдерей у твоей дохлой мамы', 'гитара у твоей выебоной бабушки', 'пкж анус', 'очко жим жим', 'нет времени обеснять, суй ананас в жопу', 'папа здох от передоза?', 'помяукай у моего хуя', 'типо крутой?', 'мастер в гей клубе', 'гей', 'хохол', 'мама в спермахе', 'я тя щас как за залупку дёрну', 'чмо']

stop_flag = False

@bot.command()
async def start(ctx, member : discord.Member, skolco : int):
	await ctx.message.delete()
	
	for i in range(skolco):
		global stop_flag
		if stop_flag:
		    stop_flag = False
		    break
		
		ponrandom = random.choice(texts)
		await ctx.send(f'{member.mention} {ponrandom}')
		await asyncio.sleep(0.9)

@bot.command()
async def stop(ctx):
    await ctx.message.delete()
    
    global stop_flag
    stop_flag = True

@bot.command()
async def osk(ctx, member : discord.Member):
    await ctx.message.delete()
    
    ponrandom = random.choice(texts)
    await ctx.send(f'{member.mention} {ponrandom}')

@bot.command()
async def spam(ctx, skolco: int, *, text):
    await ctx.message.delete()
    
    for i in range(skolco):
        global stop_flag
        if stop_flag:
            stop_flag = False
            break
        
        await ctx.send(text)

@bot.command()
async def prikol1(ctx, skolco: int):
    await ctx.message.delete()
    
    for i in range(skolco):
        await ctx.send('Делаем свой проект (майнкрафт) будут вопросы как вступить пишите в лс')
        await asyncio.sleep(0.9)

@bot.command()
async def prikol2(ctx, skolco: int):
    await ctx.message.delete()
    
    for i in range(skolco):
        await ctx.send('https://cdn.discordapp.com/attachments/1044585702559596634/1287893018799771760/haha.gif')
        await asyncio.sleep(0.9)


bot.run(token_input)
