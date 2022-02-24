# result sheet
# import random

# variable initializing
NOS = 3
subject = ["English", "Maths", "Social"] #, "Compu", "O.Maths","Nepali","Health"]

#-----------------------------------------------------------------
def data_input(n, sub):
	# student name input
	name = []
	for i in range(n):
		print("Enter name of student-", i+1 , ": ", end="")
		nm = input()
		name.append(nm)
	marks = []
	marks.append(sub.copy()) # marks.append(sub)
	marks[0].insert(0,"Name") # [["Name","English", "Maths", "Social"],]
	
	# mark input for all student in all subject
	for i in range(1,n+1):
		mark = []
		for j in range(len(sub)):
			#-----------------------------------
			print("Enter mark for ", name[i-1], "  in subject ", sub[j],": ",end="")
			mark.append(int(input()))
			#------------------------------------
			# mark.append(random.randint(25,100))
		marks.append(mark)
		marks[i].insert(0, name[i-1])
	return marks # [["Name","English", "Maths", "Social"],["ram", 1,2,3],["sam",2,3,4],["kris",3,4,5]]

def add_total(n, res):
	res[0].insert(len(res[0]),"Total") # [["Name","English", "Maths", "Social", "Total"],["ram", 1,2,3],["sam",2,3,4],["kris",3,4,5]]
	for i in range(1,n+1):
		res[i].insert(len(res[i]),sum(res[i][1:])) 
	# print(res)
	return res

def sort_result(res):
	# selection sort -------------sorting process
	tmp = []
	for i in range(1,len(res)):
		for j in range(1,i):
			# swap
			if res[i][len(res[i])-1] > res[j][len(res[j])-1]:
				tmp = res[i].copy()
				res[i] = res[j].copy()
				res[j] = tmp
	return res

def  display_process(result):
	# display process
	print("S.N.", end="\t")
	for i,res in enumerate(result):
		for r in res:
			print(r, end="\t")
		print()
		print(i+1, end="\t")

def file_write(result):
	# file open
	# loop:
	 	# write
	# file close

result = data_input(NOS, subject)
result = add_total(NOS,result)
result = sort_result(result)
display_process(result)
file_write(result)