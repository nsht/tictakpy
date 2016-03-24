import os #To run cls command

#Initialise Board
newBoard = {'tl':' ','tm':' ','tr':' ','ml':' ','mm':' ','mr':' ','ll':' ','lm':' ','lr':' '}

#Inirialiase condition and pieces
condition = ' '
pieces = ['x','o','X','O']




def guide():
    print('tl' + '|'+ 'tm' + '|' + 'tr')
    print('-----')
    print('ml' + '|'+ 'mm' + '|' + 'mr')
    print('-----')
    print('ll' + '|'+ 'lm' + '|' + 'lr')

def makemove1():
    move=input('Player X type a move')
    newBoard[move] = 'x'

def makemove2():
    move=input('Player O type a move')
    newBoard[move] = 'o'




#Print The Board
def printBoard():
    print(newBoard['tl'] + '|'+ newBoard['tm'] + '|' + newBoard['tr'])
    print('-----')
    print(newBoard['ml'] + '|'+ newBoard['mm'] + '|' + newBoard['mr'])
    print('-----')
    print(newBoard['ll'] + '|'+ newBoard['lm'] + '|' + newBoard['lr'])

#Clear the screen in Windows CMD
def cls():
    os.system('cls')

#Compute Winning Condition

def Compute():
    global condition
    if newBoard['tl'] == newBoard['tm'] == newBoard['tr'] in pieces:
        print(newBoard['tl'] +  ' won')
        condition = 'win'
    elif newBoard['ml'] == newBoard['mm'] == newBoard['mr'] in pieces:
        print(newBoard['ml'] +  ' won')
        condition = 'win'
    elif newBoard['ll'] == newBoard['lm'] == newBoard['lr'] in pieces:
        print(newBmoard['ll'] +  ' won')
        condition = 'win'
    elif newBoard['tl'] == newBoard['ml'] == newBoard['ll'] in pieces:
        print(newBoard['tl'] +  ' won')
        condition = 'win'
    elif newBoard['ml'] == newBoard['mm'] == newBoard['lm'] in pieces:
        print(newBoard['ml'] +  ' won')
        condition = 'win'
    elif newBoard['tr'] == newBoard['mr'] == newBoard['lr'] in pieces:
        print(newBoard['tr'] +  ' won')
        condition = 'win'
    elif newBoard['tl'] == newBoard['mm'] == newBoard['lr'] in pieces:
        print(newBoard['tl'] +  ' won')
        condition = 'win'
    elif newBoard['tr'] == newBoard['mm'] == newBoard['lr'] in pieces:
        print(newBoard['tr'] +  ' won')
        condition = 'win'
    else:
        print('Next Move')


guide()

while condition != 'win':

    if condition == 'win':
            printBoard()
            break
    #Player 1 move
    makemove1()
    Compute()
    
    if condition == 'win':
            printBoard()
            break
    cls()
    printBoard()
    #Player 2 move
    makemove2()
    cls()
    printBoard()
    Compute()
    
wait = input("type any key to exit")    
    
