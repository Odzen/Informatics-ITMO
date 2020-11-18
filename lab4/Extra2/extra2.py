import re 

email1="example@example"
email2="students.spam@yandex.ru"
email3="example@example.com"
email4="jsebastian.va@gmail.com"

email=input('Enter your email:')

regex = '^[a-z0-9]+[\ ._-]*[a-z0-9]+[@]\w+[.]\w{2,3}$' #correct?

regexDomine='[@]\w+[.]\w{2,3}$'

m=re.search(regex,email)

if(m):
	domine=re.search(regexDomine,email)
	print("Domine:" + domine[0])
else:
	print("Fail!")



