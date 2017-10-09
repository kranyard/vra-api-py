
if isinstance(value, dict):
	print "dict"
	for k, v in value.items():
		print "  ",k,"::=",v
elif isinstance(value, list):
	print "list"
	for v in value:
		print v
else:
	print value

