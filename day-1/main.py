from modules.add import *
from modules.sub import *
from modules.mul import *
from modules.div import *
from modules.mod import *

def main():
    
    choice=-1

    while choice != '6':
        print('This is a calculator. Enter choices:')
        print('1) Add')
        print('2) Subtract')
        print('3) Multiply')
        print('4) Divide')
        print('5) Module')
        print('6) Exit')
        choice=input()
        
        if choice == '6':
            break;
        else:
            output=None
            input1=input('Enter first value: ')
            input2=input('Enter second value: ')
            match choice:
                case '1':
                    output=addition(input1,input2)
                case '2':
                    output=subtract(input1,input2)
                case '3':
                    output=multiply(input1,input2)
                case '4':
                    output=divide(input1,input2)
                case '5':
                    output=modulo(input1,input2)
                case _:
                    print('invalid argument!')
            
            if output!=None:
                print(f'Answer is: {output}')
                input("Press Enter to continue...")

if __name__ == '__main__':
    main()
else:
    quit()