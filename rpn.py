def abc(a):
    rpn = []
    priority = {0: [], 1: [], 2: [], 3: []}
    i = 0

    while 1:

        num = a[i]
        x = None

        while num.isdigit() or num is '.':
            #loop for searching int and float numbers
            if num =='.':
                x = str(x) + '.'
            elif num.isdigit() and '.' in str(x):
                x = str(x) + str(num)
            elif x:
                x = x*10 + int(num)
            else:
                x = int(num)

            if i < len(a)-1:
                i+=1
                num = a[i]
            else:
                break

        while num.isalpha():
            #loop for searching text
            if priority[3] and priority[3][0].isalpha():
                priority[3][0] = priority[3][0] + num
            else:
                priority[3].insert(0, num)

            if i < len(a)-1:
                i+=1
                num = a[i]
            else:
                break

        if str(x) == '0' or x:
            #add numbers in output str and add higher priority operator
            if '.' in str(x):
                rpn.append(float(x))
                x=None
            else:
                rpn.append(x)
                x=None

            if not priority[3]:
                if priority[0]:
                    rpn.append(priority[0][0])
                    del priority[0][0]
                    if priority[1]:
                        rpn.append(priority[1][0])
                        del priority[1][0]
                        if priority[2]:
                            rpn.append(priority[2][0])
                            del priority[2][0]
                elif priority[1] and num != '^':
                    rpn.append(priority[1][0])
                    del priority[1][0]
                    if priority[2] and not num in ['*', '/', '%', '`']:
                        rpn.append(priority[2][0])
                        del priority[2][0]
            else:
                if priority[3][0] == '^':
                    rpn.append(priority[3][0])
                    del priority[3][0]

        if num in ['+', '-', '*', '/', '%', '`', '^', '(']:
            #add operators in stack
            if not priority[3]:
                if num is '^':
                    priority[0].insert(0, num)
                elif num is '(':
                    priority[3].insert(0, num)
                elif num in ['*', '/', '%', '`']:
                    priority[1].insert(0, num)
                else:
                    priority[2].insert(0, num)
            else:
                priority[3].insert(0, num)

        if num == ')':
            work = True
            while work:
                if priority[3]:
                    if priority[3][0] == '(':
                        del priority[3][0]
                        if priority[3] and priority[3][0][0].isalpha():
                            rpn.append(priority[3][0])
                            del priority[3][0]
                            break
                    else:
                        rpn.append(priority[3][0])
                        del priority[3][0]
                else:
                    while 1:
                        if priority[0]:
                            rpn.append(priority[0][0])
                            del priority[0][0]
                        elif priority[1]:
                            rpn.append(priority[1][0])
                            del priority[1][0]
                        else:
                            break
                    work = False
        i+=1

        if i >= len(a):
            work = True
            while 1:
                if priority[0]:
                    rpn.append(priority[0][0])
                    del priority[0][0]
                elif priority[1]:
                    rpn.append(priority[1][0])
                    del priority[1][0]

                elif priority[2]:
                    if len(priority[2]) > 1 and priority[2][1] == '-':
                        rpn.append(priority[2][1])
                        del priority[2][1]
                    else:
                        rpn.append(priority[2][0])
                        del priority[2][0]
                else:
                    break
            break
    return rpn
