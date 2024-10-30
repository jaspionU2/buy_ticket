from datetime import datetime, date
from array import array
from app import *
from re import split
import json

class ApllyDescount:
    
    def __init__(self, price, quantIngresso):
        self.descount = False
        self.typeCoupon = ''
        self.price = price
        self.totPrice = price * quantIngresso
        self.quantIngresso = quantIngresso
    
    def checkDescount(self):
        if self.quantIngresso >= 10:
            self.descount = True
            self.typeCoupon = "10%"
            return self.totPrice - ((self.totPrice * 2 / 10))
        
        elif self.quantIngresso >= 5:
            self.descount = True
            self.typeCoupon = "5%"
            return self.totPrice - ((self.totPrice / 10))
        
        return self.totPrice, False
    
    def descountApllied(self):
        return self.descount
            
def shoppingList(listBuys = []):
    if listBuys:
        print('Nenhuma compra foi feita ainda.')
        
    print('Resumo de compras:\n')
    for buyer in listBuys:            
        print(f'Nome do comprador: {buyer['nome_comprador']}\n')    
        for buy in buyer['compras']:
            print('---Compras--- ')               
            print(f"Evento: {buy['evento']}")
            print(f"Quant. ingressos: {buy['quant_ingressos']}")
            print(f"Data da compra: {buy['data_compra']}")
            print(f"Valor total: R$ {buy['valor_total']:.2f}\n")      

def showEvents(listEvent = []):
    print('---Lista De Eventos---\n')
    for event in listEvent:
        print(f'Evento: {event['nome_evento']}')
        print(f'Valor do Evento: {event['valor']}')
        print(f'Desc.: {event['descricao']}')
        print(f'quant. ingressos: {event['quantIngressos']}')

def ticketsAvailable (listEvent = [], numTickets = None, nameEvent = ''):
   numTickets = int(input('Quantas ingressos deseja comprar? '))
   
   for event in listEvent:
       if event['nome_evento'] == nameEvent:
           if event['quantIngressos'] >= numTickets and numTickets > 0:
               event['quantIngressos'] -= numTickets
               return numTickets
           else:
               return -1
   return -1

def validationName(message = ''):
    
   nameBuyer = input(str(message))
    
   while len(nameBuyer) < 3 or nameBuyer.isnumeric():
       print('ERRO: O nome digita é invalido. Tente novamente.')
       nameBuyer = input(str(message))
    
   return nameBuyer

def buyTicket(listEvent = [], orders = [], nameEvent = '', nameBuyer = '', numTickets = None):
    eventoValido = False
    eventoEncontrado = False
    for event in listEvent: 
        if event['nome_evento'] == nameEvent:
            eventoEncontrado = True
            nomeComprador = validationName('Digite seu nome: ')     
            quantIngressos = ticketsAvailable(listEvent, numTickets, nameEvent)
                
            while quantIngressos == -1:
                print('ERRO: A quantidade de ingressos informada, não esta disponivel para o evento.Informe uma quantidade valida.\n')
                quantIngressos = ticketsAvailable(listEvent, numTickets, nameEvent)
            
            cuponDescount = ApllyDescount(event['valor'], quantIngressos)
            price = cuponDescount.checkDescount()
            
            if cuponDescount.descountApllied():
                print(f'Desconto de {cuponDescount.typeCoupon} foi aplicado sobre o valor de {cuponDescount.totPrice}')
            else:
                print() 
                   
            dataCompra = date.today()
            
            with open("mockBuyers.json", 'w') as buyers:
                buyers.write(json.dumps({
                    "nome_comprador": nomeComprador,
                    "compras": [{
                    "evento": event["nome_evento"],
                    "quant_ingressos": quantIngressos,
                    "data_compra": dataCompra.strftime("%d/%m/%Y"),
                    "valor_total": price
                    }]
                }, indent=4))
            
            # buyer_exist = None
            # for order in orders:
            #     if order['nome_comprador'] == nomeComprador:
            #         buyer_exist = order
                    
            # if buyer_exist:
            #     buyer_exist['compras'].append(
            #             {
            #             'evento': event['nome_evento'],
            #             'quant_ingressos': quantIngressos,
            #             'data_compra': dataCompra.strftime("%d/%m/%Y"),
            #             'valor_total': price
            #             }
            #             )
            # else:        
            #     orders.append({
            #         'nome_comprador': nomeComprador,
            #         'compras': [{
            #         'evento': event['nome_evento'],
            #         'quant_ingressos': quantIngressos,
            #         'data_compra': dataCompra.strftime("%d/%m/%Y"),
            #         'valor_total': price
            #         }]
            #     })
            print(f'ingresso(s) para o evento {event["nome_evento"]} comprado com sucesso!\n')
            eventoValido = True
            break
        
    if not eventoEncontrado:
         eventoIngresso = input('Evento informado é invalido. Digite [S] para digitar novo evento ou [N] para interromper a compra: ').lower()
               
         if eventoIngresso.upper() == 'N':
            eventoValido = True
            print('compra interrompida.\n')
            return eventoValido
        
    return eventoValido


observador = True
eventos = [
    {
        'nome_evento': 'rock in rio',
        'valor': 70.00,
        'descricao': 'Id nostrud ea aliquip quis pariatur ad consectetur sunt aliquip Lorem.',
        'quantIngressos': 100
    },
    {
        'nome_evento': 'lollapalooza',
        'valor': 100.00,
        'descricao': 'Incididunt culpa est reprehenderit nisi occaecat consequat.',
        'quantIngressos': 50
    },
    {
        'nome_evento': 'coachella',
        'valor': 150.00,
        'descricao': 'Proident occaecat reprehenderit labore est laborum pariatur sint.',
        'quantIngressos': 15
    }
]
listEvents = None

infoBuyer = None

with open("mockBuyers.json") as buyers:
    infoComprador = json.load(buyers)

with open("mockEvents.json") as events:
    listEvents = json.load(events)

while observador:
   try:
    switchController = int(input('[1] - Comprar ingresso\n[2] - Imprimir lista de eventos\n[3] - Mostrar compras\n[4] - Encerrar compra\nDigite uma opção: '))
        
    match switchController:
            case 1:   
                eventoValido = False
        
                while not eventoValido:
                    eventoIngresso = input('Informe de qual evento deseja comprar o ingresso: ').lower()
                    eventoValido = buyTicket(listEvents, infoBuyer, eventoIngresso)
            
                    comprarTicket = input('deseja comprar um ingresso? [S] ou [N]: ')
        
                    if comprarTicket.upper() != 'S':
                       break
                    
            case 2:
                showEvents(listEvents) 
            
            case 3:
               shoppingList(infoBuyer)
            
            case 4:
                observador = False
                print('Progama encerrado')
            
            case _:
                print("Opção inválida! Tente novamente.")  
                     
   except ValueError:   
       print("Erro: por favor, insira uma opção válida.")