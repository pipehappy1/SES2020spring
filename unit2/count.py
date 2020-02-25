def count_char(fn,):
	import os.path
	if os.path.isfile(fn):
		with open (fn,'r') as fh:
			total=0
			fh=fh.read()
			total=len(fh.split())
			return total

a=count_char('/Users/zhouying/Desktop/readme.md')
print(a)