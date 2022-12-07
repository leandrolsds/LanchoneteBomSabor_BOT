import requests
import json
import os
class TelegramBot:
	def __init__(self):
		token = '5838572417:AAE96O-oq4zivqP4_qJSP3ekH3oiauykJLo'
		self.url_base = f'https://api.telegram.org/bot{token}/'
	def Iniciar(self):
		update_id = None
		while True:
			atualizacao = self.obter_mensagens(update_id)
			mensagens = atualizacao['result']
			if mensagens:
				for mensagem in mensagens:
					update_id = mensagem['update_id']
					chat_id = mensagem['message']['from']['id']
					eh_primeira_mensagem = mensagem['message']['message_id'] == 1
					resposta = self.criar_resposta(mensagem,eh_primeira_mensagem)
					self.responder(resposta,chat_id)
	def obter_mensagens(self,update_id):
		link_requisicao = f'{self.url_base}getUpdates?timeout=100'
		if update_id:
			link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
		resultado = requests.get(link_requisicao)
		return json.loads(resultado.content)
	def criar_resposta(self,mensagem,eh_primeira_mensagem):
		mensagem = mensagem['message']['text']
		if eh_primeira_mensagem == True or mensagem.lower() == 'menu':
			return f'''Digite o número do "lanche" que gostaria de pedir.{os.linesep}1 - MISTO QUENTE{os.linesep}2 - X BURGUER{os.linesep}3 - X SALADA{os.linesep}4 - X SALADA DUPLO{os.linesep}5 - X EGG{os.linesep}6 - X BACON{os.linesep}7 - X TUDO{os.linesep}8 - X BACON EGG'''
		if mensagem == '1':
			return f'''MISTO QUENTE: presunto e queijo.{os.linesep}{os.linesep}Valor - R$6,00{os.linesep}Confirmar pedido(s / n)'''
		if mensagem == '2':
			return f'''X BURGUER: hamburguer e queijo.{os.linesep}{os.linesep}Valor - R$8,00 {os.linesep}Confirmar pedido(s / n)'''
		if mensagem == '3':
			return f'''X SALADA: hamburguer, queijo, salada e maionese. {os.linesep}{os.linesep}Valor - R$10,00 {os.linesep}Confirmar pedido(s / n)'''
		if mensagem == '4':
			return f'''X SALADA DUPLO: hamburguer, queijo, salada e maionese. {os.linesep}{os.linesep}Valor - R$15,00 {os.linesep}Confirmar pedido(s / n)'''
		if mensagem == '5':
			return f'''X EGG: hamburguer, queijo e ovo. {os.linesep}{os.linesep}Valor - R$10,00 {os.linesep}Confirmar pedido(s / n)'''
		if mensagem == '6':
			return f'''X BACON: hamburguer, queijo e bacon. {os.linesep}{os.linesep}Valor - R$14,00 {os.linesep}Confirmar pedido(s / n)'''
		if mensagem == '7':
			return f'''X TUDO: hamburguer, queijo, presunto, bacon, ovo, salada e maionese. {os.linesep}{os.linesep}Valor - R$18,00 {os.linesep}Confirmar pedido(s / n)'''
		if mensagem == '8':
			return f'''X BACON EGG: hamburguer, bacon e ovo. {os.linesep}{os.linesep}Valor - R$17,00 {os.linesep}Confirmar pedido(S / N)'''
		if mensagem.lower() in ('s','sim'):
			return f'''Pedido Confirmado!🤙 {os.linesep}{os.linesep}Obrigado pela preferencia!'''
		else:
			return f'''Olá, bem vindo a nossa Lanchonete.{os.linesep}Gostaria de acessar o menu?{os.linesep}Digite MENU'''
	def responder(self,resposta,chat_id):
		link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
		requests.get(link_de_envio)

bot = TelegramBot()	
bot.Iniciar()
