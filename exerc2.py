from datetime import datetime, date
from array import array

def updateCompra(compra, ):
    print(updates)
    


observador = True
eventos = [
    {
        'nome_evento': 'rock in rio',
        'valor': 70.00,
        'descricao': 'Id nostrud ea aliquip quis pariatur ad consectetur sunt aliquip Lorem.'
    },
    {
        'nome_evento': 'lollapalooza',
        'valor': 100.00,
        'descricao': 'Incididunt culpa est reprehenderit nisi occaecat consequat.'
    },
    {
        'nome_evento': 'coachella',
        'valor': 150.00,
        'descricao': 'Proident occaecat reprehenderit labore est laborum pariatur sint.'
    }
]
infoComprador = []

while observador:
   comprarTicket = input('deseja comprar um ingresso? [S] ou [N]: ')
   
   if comprarTicket.upper() != 'S':
       break
   
   eventoValido = False
   eventoEncontrado = False
   
   while not eventoValido:
       eventoIngresso = input('Informe de qual evento deseja comprar o ingresso: ').lower()
       for evento in eventos:
           if evento['nome_evento'] == eventoIngresso:
                eventoEncontrado = True
                nomeComprador = input('Digite seu nome: ')
                quantIngressos = int(input('Quantas ingressos deseja comprar? '))
                dataCompra = date.today()
                
                infoComprador.append({
                    'nome_comprador': nomeComprador,
                    'evento': evento['nome_evento'],
                    'quant_ingressos': quantIngressos,
                    'data_compra': dataCompra.strftime("%d/%m/%Y"),
                    'valor_total': quantIngressos * evento['valor']
                })
                print(f'ingresso(s) para o evento {evento["nome_evento"]} comprado com sucesso!\n')
                eventoValido = True
                break
            
       if not eventoEncontrado:
            eventoIngresso = input('Evento informado é invalido. Digite [S] para digitar novo evento ou [N] para interromper a compra: ').lower()
               
            if eventoIngresso.upper() == 'N':
                eventoValido = True
                print('compra interrompida.\n')
                                
                
for index in range(len(infoComprador)):               
    print(f'\n---Comprador {index+1}---\nNome: {infoComprador[index]['nome_comprador']}\nEvento: {infoComprador[index]['evento']}\nQuant. ingressos: {infoComprador[index]['quant_ingressos']}\nData da compra: {infoComprador[index]['data_compra']}\nValor total: {infoComprador[index]['valor_total']}\n')
               
           
          
           
       
       
       
     
   
    

   
   
   
  
       
       

