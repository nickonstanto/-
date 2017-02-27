sum = 0

for num in range(0,1001):
	#kateutheian oi prwtoi 10 einai harshads sigoura
	if num <= 10 :
		print(num)
		continue

	#kanw ton arithmo string gia na perasw me epanalipsi ta stoixeia tou kai na
	#kai na glitwsw tis mathimatikes prakseis
	st = str(num)
	
	#pernaw me epanalipsi ta prifia tou
	for digit in st:
		#gia na athrisw prepei na to kanw to digit apo string se integer dld akeraio
		#ara xrisimopoiw to int(x)
		sum += int(digit)

	#an diairite teleia tote einai harshad arithmos
	if num % sum == 0:
		print(num)

	sum = 0