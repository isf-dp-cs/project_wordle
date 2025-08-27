# BASIC TRY, EXCEPT
letter = 'a'
try:
	letter = letter + 3
except: 
	print("letter is not a number")


# RAISE EXCEPTIONS 
try:
	print(x)
except: 
	raise Exception("Impossible!")


# BUILT-IN EXCEPTIONS
try:
	print(x)
except: 
	raise ValueError("x does not exist")

