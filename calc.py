from math import *
from tkinter import *

def curve(f): 
    root = Tk() 

    canv = Canvas(root, width = 1000, height = 1000, bg = "white") 
    canv.create_line(500,1000,500,0,width=2,arrow=LAST) 
    canv.create_line(0,500,1000,500,width=2,arrow=LAST) 

    First_x = -500 
    for i in range(16000): 
        if (i % 800 == 0): 
            k = First_x + (1 / 16) * i 
            canv.create_line(k + 500, -3 + 500, k + 500, 3 + 500, width = 0.5, fill = 'black') 
            canv.create_text(k + 515, -10 + 500, text = str(k), fill="purple", font=("Helvectica", "10")) 
            if (k != 0): 
                canv.create_line(-3 + 500, k + 500, 3 + 500, k + 500, width = 0.5, fill = 'black') 
                canv.create_text(20 + 500, k + 500, text = str(k), fill="purple", font=("Helvectica", "10")) 
        try: 
            x = First_x + (1 / 16) * i
            if x >= 0:
                new_f = f.replace('x', str(x))
            else:
                new_f = f.replace('x', '(' + str(x) + ')')
            y = -count(new_f) + 500
            x += 500
            canv.create_oval(x, y, x + 1, y + 1, fill = 'black') 
        except: 
            pass 
    canv.pack() 
    root.mainloop()

def functions():
    i = 0
    while i < len(array):
        if array[i] in {'exp', 'ln', 'sin', 'cos', 'sqrt'} and array[i + 1] == '(' and array[i + 3] == ')':
            if array[i] == 'exp':
                array[i] = exp(array[i + 2])
            elif array[i] == 'ln':
                array[i]= log(array[i + 2])
            elif array[i] == 'sin':
                array[i] = sin(array[i + 2])
            elif array[i] == 'cos':
                array[i] =  cos(array[i + 2])
            elif array[i] == 'sqrt':
                array[i] =  sqrt(array[i + 2])
            array.pop(i + 3)
            b.pop(i + 3)
            array.pop(i + 2)
            b.pop(i + 2)
            array.pop(i + 1)
            b.pop(i + 1)
            i = -1
        i += 1
                
def free_brackets(i):
    if ind[i] - 1 > 0 and array[ind[i] - 2] == '(' and array[ind[i]] == ')':
        if ind[i] - 2 == 0 or array[ind[i] - 3] not in {'exp', 'ln', 'sin', 'cos', 'sqrt'}:
            array.pop(ind[i])
            b.pop(ind[i])
            array.pop(ind[i] - 2)
            b.pop(ind[i] - 2)    

def count(s):
    global array
    global b
    global ind
    array = []
    i = 0
    now = ""
    while i < len(s):
        if s[i] in {'+', '-', '*', '/', '(', ')', '^'}:
            array.append(s[i])
            i += 1
        elif '0' <= s[i] <= '9':
            while i < len(s) and ('0' <= s[i] <= '9' or s[i] == '.'):
                now += s[i]
                i += 1
            array.append(now)
            now = ""
            j = len(array) - 1
            if j >= 2 and array[j - 2] == '(' and array[j - 1] == '-':
                array.append(array[j])
                array[j - 1], array[j] = '0', '-'
            elif j == 1 and array[j - 1] == '-':
                array.append(array[j])
                array[j - 1], array[j] = '0', '-'
        elif 'a' <= s[i] <= 'z':
            while i < len(s) and 'a' <= s[i] <= 'z':
                now += s[i]
                i += 1
            array.append(now)
            now = ""
        else:
            i += 1
    if now != "":
        array.append(now)
    
    #count bracket balance
    flag = True
    balance = 0
    b = [0 for i in range(len(array))]
    for i in range(len(array)):
        if array[i] == '(':
            balance += 1
        elif array[i] == ')':
            balance -= 1
            if balance < 0:
                print('Check the bracket balance!')
                flag = False
        elif array[i] in {'+', '-', '*', '/', '^'}:
            b[i] = balance
        elif array[i][0].isdigit():
            array[i] = float(array[i])
        elif array[i] == 'pi':
            array[i] = pi
    if balance != 0:
        print('Check the bracket balance!')
        flag = False
    for i in range(len(array) - 1):
        if array[i] in {'+', '-', '*', '/', '^'} and array[i + 1] in {'+', '-', '*', '/', '^'}:
            print('Wrong operation: ', array[i], array[i + 1], sep = "")
            flag = False
        
    
    
    
    #counting    
    if flag:
        while len(array) != 1 and flag:
            flag1 = True
            functions()
            ind = []
            a = max(b)
            if a != 0:
                for i in range(len(b)):
                    if b[i] == a:
                        ind.append(i)
            else:
                for i in range(len(array)):
                    if array[i] in {'+', '-', '*', '/', '^'}:
                        ind.append(i)
            i = 0
            while i < len(ind) and flag:
                if array[ind[i]] == '^':
                    array[ind[i] - 1] = array[ind[i] - 1] ** array[ind[i] + 1]
                    array.pop(ind[i] + 1)
                    b.pop(ind[i] + 1)
                    array.pop(ind[i])
                    b.pop(ind[i])
                    free_brackets(i)
                    flag1 = False
                    break
                i += 1
            functions()
            i = 0
            while i < len(ind) and flag and flag1:
                if array[ind[i]] == '*' or array[ind[i]] == '/':
                    if array[ind[i]] == '*':
                        array[ind[i] - 1] = array[ind[i] - 1] * array[ind[i] + 1]
                        array.pop(ind[i] + 1)
                        b.pop(ind[i] + 1)
                        array.pop(ind[i])
                        b.pop(ind[i])
                        free_brackets(i)
                    else:
                        if array[ind[i] + 1] == 0:
                            print('Division by zero!')
                            flag = False
                            break
                        else:
                            array[ind[i] - 1] = array[ind[i] - 1] / array[ind[i] + 1]
                            array.pop(ind[i] + 1)
                            b.pop(ind[i] + 1)
                            array.pop(ind[i])
                            b.pop(ind[i])
                            free_brackets(i)
                    flag1 = False
                    break
                i += 1
            functions()
            i = 0
            while i < len(ind) and flag and flag1:
                if array[ind[i]] == '+' or array[ind[i]] == '-':
                    if array[ind[i]] == '+':
                        array[ind[i] - 1] = array[ind[i] - 1] + array[ind[i] + 1]
                    else:
                        array[ind[i] - 1] = array[ind[i] - 1] - array[ind[i] + 1]
                    array.pop(ind[i] + 1)
                    b.pop(ind[i] + 1)
                    array.pop(ind[i])
                    b.pop(ind[i])
                    free_brackets(i)
                    break
                i += 1
    if flag:
        return array[0]
    else:
        return False
        

s = input()
a1 = s.split()
if a1[0] == 'curve':
    curve(' '.join(a1[1:]))
else:
    a = count(s)
    if a != False:
        if int(a) == a:
            print(int(a))
        else:
            print(a)    
