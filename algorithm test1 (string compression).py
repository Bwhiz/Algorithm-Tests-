from itertools import groupby
emp=""
user=input("enter text:  ")
for k,g in groupby(user):
	emp+=(k+str(sum(1 for i in g)))
	
print(emp)

#example:
#enter text: aabba
#>> a2b2a1
#enter text: aaassbbbaaa
#>>a3s2b3a3
