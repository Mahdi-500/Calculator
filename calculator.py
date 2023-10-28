from tkinter import *
import tkinter.messagebox as tm

main = Tk()
main.title('calculator')

e = Entry(main, borderwidth=5)
e.grid(row=0, column=0, ipadx=300, columnspan=4)

# defining functions


def number(n):

    # inserts the numbers and symbols in entry

    if n != '=':
        current = str(e.get()) + str(n)
        e.delete(0, END)
        e.insert(0, current)

    # begin calculating

    elif n == '=':
        
        calculate()

    if n == 'clear':
        e.delete(0, END)


def calculate():

    flag_2 = False

    # calculate both multiplication and division

    for i in range(0, len(e.get())):
        x = e.get()
        if x[i] == '+' or x[i] == '-' or x[i] == '*' or x[i] == '%':
            if x[i + 1] == '+' or x[i + 1] == '-' or x[i + 1] == '*' or x[i + 1] == '%':
                e.delete(0,END)
                tm.showwarning('two opertors', 'you can\'t put two operators next to each other')
                return
            
    # handles the index error

    try:
        for i in range(0, len(e.get())):
            x = e.get()  # it updates every time a change is made
            a = ''

            # find the start and end point for deleting and replacing

            if x[i] == '*' or x[i] == '%':
                start, end = find(x)
                flag_2 = True
                for j in range(start, end + 1):
                    a += x[j]

            # calculates the multiplication and division

            if a != '':
                result = multipla_divide(phrase=a)
                e.delete(start, end + 1)
                e.insert(start, result)

    except IndexError:
        pass

    a = ''
    b = ''
    end_2 = 0

    if flag_2:
        if flag:

            # saves te first number

            for i in range(0, len(x)):
                if x[i] != '+' and x[i] != '-':
                    a += x[i]
                else:
                    start_2 = i  # saves the location of first operator
                    break

            # saves the second number

            for i in range(start_2 + 1, len(x)):
                if x[i] != '+' and x[i] != '-':
                    b += x[i]
                elif x[i] == '+' or x[i] == '-':
                    end_2 = i  # saves the end of second number
                    break
            
            if end_2 == 0:
                end_2 = len(x) - 1

            # calculate the first two number based on saved operator

            if x[start_2] == '+':
                if '.' in a and '.' in b:
                    result = float(a) + float(b)
                elif '.' in a and '.' not in b:
                    result = float(a) + int(b)
                elif '.' not in a and '.' in b:
                    result = int(a) + float(b)
                else:
                    result = int(a) + int(b)

            else:
                if '.' in a and '.' in b:
                    result = float(a) - float(b)
                elif '.' in a and '.' not in b:
                    result = float(a) - int(b)
                elif '.' not in a and '.' in b:
                    result = int(a) - float(b)
                else:
                    result = int(a) - int(b)

            # calculates rest of the phrase

            if end_2 != len(x) - 1:
                b = ''
                for i in range(end_2, len(x)):

                    # saves the operator

                    if x[i] == '+':
                        sign = '+'
                    elif x[i] == '-':
                        sign = '-'

                    # saves the number whci is after saved operator

                    if x[i] != '+' and x[i] != '-':
                        b += x[i]
                    else:
                        b = ''

                    if i + 1 != len(x):  # handles the index string out of range error

                        # checks if number is saved completely or not

                        if x[i + 1] == '+' or x[i + 1] == '-':
                            if b != '':
                                if sign == '+':
                                    if '.' in b:
                                        result += float(b)
                                    else:
                                        result += int(b)
                                else:
                                    if '.' in b:
                                        result -= float(b)
                                    else:
                                        result -= int(b)
                    else:  # if i + 1 != len(x) it means i is on the last number
                        if sign == '+':
                            if '.' in b:
                                result += float(b)
                            else:
                                result += int(b)
                        else:
                            if '.' in b:
                                result -= float(b)
                            else:
                                result -= int(b)
    else:
        
        # saves the first number

        for i in range(0, len(x)):
            if x[i] != '+' and x[i] != '-':
                a += x[i]
            else:
                start_2 = i
                break

        # saves the second number

        for i in range(start_2 + 1, len(x)):
            if x[i] != '+' and x[i] != '-':
                b += x[i]
                
            else:
                end_2 = i
                break
        if end_2 == 0:
                end_2 = len(x) - 1
        
        # calculate the first two number based on saved operator

        if x[start_2] == '+':
            if '.' in a and '.' in b:
                result = float(a) + float(b)
            elif '.' in a and '.' not in b:
                result = float(a) + int(b)
            elif '.' not in a and '.' in b:
                result = int(a) + float(b)
            else:
                result = int(a) + int(b)

        else:
            if '.' in a and '.' in b:
                result = float(a) - float(b)
            elif '.' in a and '.' not in b:
                result = float(a) - int(b)
            elif '.' not in a and '.' in b:
                result = int(a) - float(b)
            else:
                result = int(a) - int(b)

        # calculates rest of the phrase

        if end_2 != len(x) - 1:
            b = ''
            for i in range(end_2, len(x)):

                # saves the operator

                if x[i] == '+':
                    sign = '+'
                elif x[i] == '-':
                    sign = '-'

                # saves the number whci is after saved operator

                if x[i] != '+' and x[i] != '-':
                    b += x[i]
                else:
                    b = ''

                if i + 1 != len(x):  # handles the index string out of range error

                    # checks if number is saved completely or not

                    if x[i + 1] == '+' or x[i + 1] == '-':
                        if b != '':
                            if sign == '+':
                                if '.' in b:
                                    result += float(b)
                                else:
                                    result += int(b)
                            else:
                                if '.' in b:
                                    result -= float(b)
                                else:
                                    result -= int(b)
                else:  # if i + 1 != len(x) it means i is on the last number
                    if sign == '+':
                        if '.' in b:
                            result += float(b)
                        else:
                            result += int(b)
                    else:
                        if '.' in b:
                            result -= float(b)
                        else:
                            result -= int(b)

    e.delete(0, END)
    e.insert(0, result)


def find(x) -> int:

    global start, end, flag
    flag = False

    if '*' in x and '%' in x:
        if '-' in x or '+' in x:
            flag = True

            if x.index('*') < x.index('%'):
                begin = x.index('*')
            if x.index('*') > x.index('%'):
                begin = x.index('%')

        elif '+' not in x and '-' not in x:
            flag = False
            start = 0
            end = len(x) - 1

    elif '*' in x or '%' in x:
        if '+' in x or '-' in x:
            flag = True

            if '*' in x and '%' not in x:
                begin = x.index('*')
            if '*' not in x and '%' in x:
                begin = x.index('%')

        elif '+' not in x and '-' not in x:
            flag = False
            start = 0
            end = len(x) - 1
            
    # finds the first number before * or % and last number after * or %
    
    if flag:
        start = end = 0
        for i in range(begin, 0, -1):
            if x[i] == '+' or x[i] == '-':
                start = i + 1
                break

        for i in range(begin, len(x)):
            if x[i] == '+' or x[i] == '-':
                end = i - 1
                break
        if end == 0:
            end = len(x) - 1
    
    return start, end


def multipla_divide(phrase) -> int or float:
    a = ''
    b = ''

    # save the first two numbers and sign; then calculate them based on the saved operator

    for i in range(0, len(phrase)):

        # saves the number before the sign

        if phrase[i] != '*' and phrase[i] != '%':
            a += phrase[i]
        else:
            start = i
            break

    # saves the number after the sign

    for i in range(start + 1, len(phrase)):
        if phrase[i] != '*' and phrase[i] != '%':
            b += phrase[i]
            end = i
        else:
            end = i
            break

    # calculate the first two numbers

    if phrase[start] == '*':
        result = int(a) * int(b)
    else:
        result = int(a) / int(b)

    # calculates the rest of phrase

    if len(phrase) - end != 1:
        b = ''
        for i in range(end, len(phrase)):

            # saves the operator

            if phrase[i] == '*':
                sign = '*'
            elif phrase[i] == '%':
                sign = '%'

            else:
                b += phrase[i]
            if phrase[i] == '*' or phrase[i] == '%':
                b = ''

            # calculates the rest of phrase

            if i != len(phrase) - 1:  # handles the index string out of range exepction
                if phrase[i + 1] == '*' or phrase[i + 1] == '%':
                    if b != '':
                        if sign == '*':
                            result *= int(b)
                        else:
                            result /= int(b)
            else:
                if sign == '*':
                    result *= int(b)
                else:
                    result /= int(b)

    return result


# defining and organizing the buttons
button_7 = Button(main, text='7', pady=10, bg='#B3B3B3',
                  command=lambda: number(7)).grid(row=1, column=0, ipadx=80)
button_8 = Button(main, text='8', pady=10, bg='#B3B3B3',
                  command=lambda: number(8)).grid(row=1, column=1, ipadx=80)
button_9 = Button(main, text='9', pady=10, bg='#B3B3B3',
                  command=lambda: number(9)).grid(row=1, column=2, ipadx=80)
button_devide = Button(main, text='%', font='bold', pady=8,
                       bg='black', fg='white', command=lambda: number('%')).grid(row=1, column=3, ipadx=76.4)

button_4 = Button(main, text='4', pady=10, bg='#B3B3B3',
                  command=lambda: number(4)).grid(row=2, column=0, ipadx=80)
button_5 = Button(main, text='5', pady=10, bg='#B3B3B3',
                  command=lambda: number(5)).grid(row=2, column=1, ipadx=80)
button_6 = Button(main, text='6', pady=10, bg='#B3B3B3',
                  command=lambda: number(6)).grid(row=2, column=2, ipadx=80)
button_x = Button(main, text='x', font='bold', pady=9,
                  bg='black', fg='white', command=lambda: number('*')).grid(row=2, column=3, ipadx=80.4)

button_1 = Button(main, text='1', pady=10, bg='#B3B3B3',
                  command=lambda: number(1)).grid(row=3, column=0, ipadx=80)
button_2 = Button(main, text='2', pady=10, bg='#B3B3B3',
                  command=lambda: number(2)).grid(row=3, column=1, ipadx=80)
button_3 = Button(main, text='3', pady=10, bg='#B3B3B3',
                  command=lambda: number(3)).grid(row=3, column=2, ipadx=80)
button_minus = Button(main, text='- ', font='bold', pady=9,
                      bg='black', fg='white', command=lambda: number('-')).grid(row=3, column=3, ipadx=79)

button_plus = Button(main, text='+', font='bold', pady=9,
                     bg='black', fg='white', command=lambda: number('+')).grid(row=4, column=3, ipadx=79)
button_0 = Button(main, text='0', pady=10, bg='#B3B3B3',
                  command=lambda: number(0)).grid(row=4, column=0, ipadx=80)
button_equal = Button(main, text='=', font='bold', pady=9,
                      bg='black', fg='white', command=lambda: number('=')).grid(row=4, column=2, ipadx=77)
button_clear = Button(main, text=' clear', pady=10, bg='#FFFFFF',
                      fg='#FF0000', command=lambda: number('clear')).grid(row=4, column=1, ipadx=69)


main.mainloop()