# from time import clock
# from functools import lru_cache

# @lru_cache(maxsize=None)
# def factorial(n):
# 	total = 1
# 	while n > 0:
# 		total *= n
# 		n -= 1
# 	return total

# start_time = clock()

# factorial(100000)

# first_call = clock()

# factorial(100000)

# second_call = clock()

# print("First call to factorial:", first_call-start_time)

# print("Second call to factorial:", second_call-first_call)


# def bold(func):
# 	def wrapper(name):
# 		return "<b>{}</b>".format(func(name))
# 	return wrapper

# def italic(func):
# 	def wrapper(name):
# 		return "<i>{}</i>".format(func(name))
# 	return wrapper


# @bold
# @italic
# def greet(name):
#    return "Hello, {}!".format(name)

# print(greet("Maria"))


f = open('file')
try:
	# código que usa o arquivo
finally:
	f.close()