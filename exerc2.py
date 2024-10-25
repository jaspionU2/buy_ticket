from datetime import datetime, date
from array import array
from app import *

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
    
   nameBuyer =input(str(message))
    
   while len(nameBuyer) < 3 or nameBuyer.isnumeric:
       print('ERRO: O nome digita é invalido. Tente novamente.')
       nameBuyer =input(str(message))
    
   return nameBuyer
  
def apllyDescount():    
      

def buyTicket(listEvent = not None, orders = [], nameEvent = '', nameBuyer = '', numTickets = None): 
    eventoValido = False
    eventoEncontrado = False
    for event in listEvent:
           if event['nome_evento'] == nameEvent:
                eventoEncontrado = True
                nomeComprador = validationName('Digite seu nome: ')     
                quantIngressos = ticketsAvailable(listEvent, numTickets, nameEvent)
                
                while quantIngressos == -1:
                    print('ERRO: A quantidade de ingressos informada, não esta disponivel para o evento. Informe uma quantidade valida.\n')
                    quantIngressos = ticketsAvailable(listEvent, numTickets, nameEvent)
                    
                
                dataCompra = date.today()
                
                buyer_exist = None
                for order in orders:
                    if order['nome_comprador'] == nomeComprador:
                        buyer_exist = order
                        
                if buyer_exist:
                    buyer_exist['compras'].append(
                            {
                            'evento': event['nome_evento'],
                            'quant_ingressos': quantIngressos,
                            'data_compra': dataCompra.strftime("%d/%m/%Y"),
                            'valor_total': quantIngressos * event['valor']
                            }
                         )
                else:        
                    orders.append({
                        'nome_comprador': nomeComprador,
                        'compras': [{
                        'evento': event['nome_evento'],
                        'quant_ingressos': quantIngressos,
                        'data_compra': dataCompra.strftime("%d/%m/%Y"),
                        'valor_total': quantIngressos * event['valor']}
                        ],
                    })
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
infoComprador = []

while observador:
   try:
    switchController = int(input('[1] - Comprar ingresso\n[2] - Imprimir lista de eventos\n[3] - Mostrar compras\n[4] - Encerrar compra\nDigite uma opção: '))
        
    match switchController:
            case 1:   
                eventoValido = False
        
                while not eventoValido:
                    eventoIngresso = input('Informe de qual evento deseja comprar o ingresso: ').lower()
                    eventoValido = buyTicket(eventos, infoComprador, eventoIngresso)
            
                    comprarTicket = input('deseja comprar um ingresso? [S] ou [N]: ')
        
                    if comprarTicket.upper() != 'S':
                       break
                    
            case 2:
                showEvents(eventos) 
            
            case 3:
                print('Resumo de compras:\n')
                for comprador in infoComprador:            
                    print(f'Nome do comprador: {comprador['nome_comprador']}\n')    
                    for compra in comprador['compras']:
                        print('---Compras--- ')               
                        print(f"Evento: {compra['evento']}")
                        print(f"Quant. ingressos: {compra['quant_ingressos']}")
                        print(f"Data da compra: {compra['data_compra']}")
                        print(f"Valor total: R$ {compra['valor_total']:.2f}\n")
            
            case 4:
                observador = False
                print('Progama encerrado')
            
            case _:
                print("Opção inválida! Tente novamente.")  
                     
   except ValueError:   
       print("Erro: por favor, insira uma opção válida.")