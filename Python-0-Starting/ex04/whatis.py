import sys

if len(sys.argv) == 1:
	sys.exit(0)

try:
	assert len(sys.argv) <= 2, "more than one argument is provided"

	try:
		value = int(sys.argv[1])
	except ValueError:
		raise AssertionError("argument is not an integer")
	
	if value % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")
	
except AssertionError as err:
	print(f"AssertionError: {err}")
