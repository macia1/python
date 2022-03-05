# 无参注解
def aop(method):
	def doAction(*method_args):
		print("start hook ", method)
		method(method_args)
	return doAction

@aop
def say(*args):
	print("Hi, This is Macia,", args, " is your mean? ")

# 带参注解
def annotation_with_args(**map):
	def doAction(method):
		for k in map:
			setattr(method, k, map[k])
		return method
	return doAction

@annotation_with_args(a='sport',b='sing')
def body():
	print("I want to ", getattr(body, 'a'))
	print("I want to ", getattr(body, 'b'))


if __name__ == '__main__':
	say([1,2,3])
	body()