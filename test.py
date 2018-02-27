l = [ {'phone':1324567890}, {'phone':1234567890}]

for x in l:
	if x['phone'] == 1234567890:
		print l.index(x)