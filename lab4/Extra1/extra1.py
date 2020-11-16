import re

with open('Hamlet.txt', 'r') as rf:
	with open('outpoud.txt', 'w') as wf:
		rf_content=rf.readlines()

		regex = '^[^,\n]*((,[^,\n]*){2,}$)'

		for line in rf_content:
			m=re.search(regex,line)

			if(m):
				print(line)
				wf.write(line)