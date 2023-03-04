from BotTwitter import BotTwitter
from Tela import Tela


tela = Tela()
valores = tela.iniciar()
print(valores)

bot = BotTwitter()
bot.abrirSite('https://twitter.com/')

input('opa')
print(valores)