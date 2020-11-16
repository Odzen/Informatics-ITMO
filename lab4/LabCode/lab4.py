import re
import string

Test1= "Довольно распространённая ошибка ошибка - это лишний повтор повтор слова слова. Смешно, не не правда ли? Не нужно портить хор хоровод."
Test2="Объктно-ориентиированное программиирование     программиирование это методология программирования, основанная основанная на представлении программы в виде совокупности совокупности объектов."
Test3="Регулярные выражения выражения это формальный язык поиска и осуществления осуществления манипуляций с подстроками в тексте, основанный основанный на использовании метасимволов."
Test4="Python это высокоуровневый язык язык программирования общего назначения, ориентированный на повышение повышение производительности разработчика и читаемости читаемости кода."
Test5="Информатика это наука наука о методах и процессах сбора, хранения, обработки обработки, передачи, анализа и оценки информации информации с применением компьютерных технологий, обеспечивающих обеспечивающих возможность её использования для принятия решений."


def replaceReg(string):
    re_output=re.sub(r'\b(\w+)\s*( \1\b)+', r'\1', string)
    return re_output

def withoutPunct(stringWithPunct):
    for c in string.punctuation:
        stringWithPunct= stringWithPunct.replace(c,"")
    return stringWithPunct

def replaceNormal(string):
    count=0
    new=[]
    split=string.split()
    actual=""
    next=""
    nextWithoutPunt=""
    temp=0
    for word in split:
        if(count+1<len(split)):
            actual=word
            nextWord=split[count+1]
            temp=len(nextWord)
        else:
            actual=word
            nextWord=""

        if(nextWord[temp - 1:]=='.' or nextWord[temp - 1:]==','):
            nextWithoutPunt=nextWord[:temp - 1]
        if(actual==nextWord):
            new.append("")
        elif(actual==nextWithoutPunt):
            new.append('')
        else:
            new.append(actual)
        
        count+=1
    return ' '.join(new)

re_output1 = replaceReg(Test1)
re_output2 = replaceReg(Test2)
re_output3 = replaceReg(Test3)
re_output4 = replaceReg(Test4)
re_output5 = replaceReg(Test5)

output1=replaceNormal(Test1)
output2=replaceNormal(Test2)
output3=replaceNormal(Test3)
output4=replaceNormal(Test4)
output5=replaceNormal(Test5)


print("REgex1:"+ re_output1)
print("Normal1: "+ output1+'\n')

print("REgex2:"+ re_output2)
print("Normal2: "+ output2+'\n')

print("REgex3:"+ re_output3)
print("Normal3: "+ output3+'\n')

print("REgex4:"+ re_output4)
print("Normal4: "+ output4+'\n')

print("REgex5:"+ re_output5)
print("Normal5: "+ output5+'\n')




