import re
import os

def openfile(file_name):
    fr = open(file_name,'r', encoding = 'utf-8')
    s = fr.read ()
    fr.close()
    return s

def names (s):
    regex = '([А-Я]\. [А-Я][а-я]+(?: |\.|,))'
    array = re.findall (regex , s)
    print ('Задание №1:')
    for word in array:
        word = word.strip ('., ')
        print (word)

def allnames (s):
    regex = ('((?:(?:(?:[А-Я]\. )?[А-Я]\.)|(?:[А-Я][а-я]+)) [А-Я][а-я]+(?: |\.|,))')
    array = re.findall (regex , s)
    print ('\nЗадание №2:')
    for word in array:
        word = word.strip ('., ')
        print (word)
    return (array)

def folders (array, s):
    for word in array:
        regex = ('((?:(?:(?:[А-Я]\. )?[А-Я]\.)|(?:[А-Я][а-я]+)) ([А-Я][а-я]+)(?: |\.|,))')
        res = re.search (regex, word)
        if res != None:
            family = res.group (2)
        if not os.path.isdir(family):
            os.makedirs(family)
    

def main ():
    names(openfile('history_reading.txt'))
    a = allnames(openfile('history_reading.txt'))
    folders (a ,openfile('history_reading.txt'))

if __name__=='__main__':
    main()
