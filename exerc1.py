def getNumberOfVogals(Word):
    lettersInText = list(Word)
    vogals = ['a', 'e', 'i', 'o', 'u']
    count = 0
    
    for Text in lettersInText:
        if Text in vogals:
            count+=1
    print(count)
    
def getNumberOfConsoants(Word):
    lettersInText = list(set(Word))
    vogals = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    count = 0
    
    for letter in lettersInText:
         if letter not in vogals:
             result.append(letter)
             count+=1
    print(f'Consoantes: {result}\nTotal: {count}')
             
        
       
    

getNumberOfVogals('abacaxi')
getNumberOfConsoants('batata')



