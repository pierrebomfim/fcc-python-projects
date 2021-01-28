
def arithmetic_arranger(list, x = False):
    if len(list) > 5 : return ('Error: Too many problems.')
    
    new_list = []
    for item in list:
        if '*' in item or '/' in item:
            return ("Error: Operator must be '+' or '-'.")
        new_list.append(item.split())
    
    for i in new_list:
        if not i[0].isdigit() or not i[2].isdigit():
            return ('Error: Numbers must only contain digits.')
        if len(i[0]) > 5 or len(i[2]) > 5: 
            return ('Error: Numbers cannot be more than four digits.')
        
        if i[1] == '+':
            result = int(i[0]) + int(i[2])
            i.append(str(result))
        else:
            result = int(i[0]) - int(i[2])
            i.append(str(result))
        
    list_one = []
    list_two = []
    list_three = []
    list_four = []  

    for item in new_list:
        if len(item[0]) < len(item[2]):
            space = ' ' * (len(item[2]) - len(item[0]))
            list_one.append('  ' + space + item[0])
            list_two.append(item[1] + ' ' + item[2])
            list_three.append('-' * len(item[1] + ' ' + item[2]))
            if len(item[3]) == len(item[2]):
                list_four.append( '  ' + item[3])
            elif len(item[3]) > len(item[2]):
                list_four.append( ' ' + item[3])
            else:
                list_four.append( ' ' + item[3])
        else: 
            space = ' ' * (len(item[0]) - len(item[2]))
            list_one.append('  ' + item[0])
            list_two.append(item[1] + ' ' + space + item[2])
            list_three.append('-' * len(item[1] + ' ' + item[0]))
            trick = ' ' * (len(item[0]) - len(item[3]))
            list_four.append('  ' +  trick + item[3])
    if x:
        return ('    '.join(list_one) + '\n' + '    '.join(list_two) + '\n' + '    '.join(list_three) + '\n' + '    '.join(list_four))
    else:
        return ('    '.join(list_one) + '\n' + '    '.join(list_two) + '\n' + '    '.join(list_three))
 


print(arithmetic_arranger(["10901 - 10", "40 - 100", "40 - 405", "3 + 409"], x = False))
