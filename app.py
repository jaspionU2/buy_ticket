from random import *;

characterLower = "abcdefghijklmnopqrstuvwxyz";
characterUpper = characterLower.upper();
numbers = "1234567890";

def getRandomCharUpper() -> str:
    return characterUpper[randint(0, len(characterUpper) - 1)];

def getRandomCharLower() -> str:
    return characterLower[randint(0, len(characterLower) -1)];

def getRandomCharNumber() -> str:
    return numbers[randint(0, len(numbers) - 1)];

def createPassWord():
    existCharacterLow = False
    existCharacterUpper = False
    senha = []
    
    for _ in range(8):
        Random().seed()
        randomizeSwitch = Random().randint(1, 3)
        match randomizeSwitch:
            case 1:
                senha.append(getRandomCharLower())
                existCharacterUpper = True
            case 2:
                senha.append(getRandomCharUpper())
                existCharacterLow = True
            case 3:
                senha.append(getRandomCharNumber())
            case _:
                print(randomizeSwitch)
                break
                
    if not existCharacterUpper and not existCharacterLow:
           print(f'senha formatada: {type(existCharacterLow)}, {type(existCharacterUpper)}')
           createPassWord()
           
    return '-'.join(senha)
  
  
print(createPassWord())