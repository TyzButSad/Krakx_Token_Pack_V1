import random
import time
import datetime

chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'

def localtime():
    time = datetime.datetime.now()
    return f'[{time.strftime("%H:%M:%S")}]'

def generator(number: int):
    num = 0
    for a in range(number):
        num += 1
        TOKEN = ''

        for a in range(24):
            TOKEN+=random.choice(chars)
        TOKEN+='.'

        for a in range(6):
            TOKEN+=random.choice(chars)
        TOKEN+='.'

        for a in range(27):
            TOKEN+=random.choice(chars)
        time.sleep(0.4)
        print(f'{TOKEN}')
        

def main():
    number = int(input('Entre Un Chiffre : '))
    print('='*75)
    generator(number)
    print('='*75)
    main()

if __name__ == '__main__':
    print('')
    print('')
    print('████████      █     █      ███████')
    print('   ██          █   █             █')
    print('   ██            █             █')
    print('   ██            █           █')
    print('   ██            █         █')
    print('   ██            █         ██████')
    print('')
    print('')
    print('Combien de token veux tu ?')
    main()


file = open('Token Codes.txt', 'a')
