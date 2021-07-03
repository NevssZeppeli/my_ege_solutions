def f1(x):
   return x

def f2(x):
   return x * 2

def f3(x):
    return x + 3

def master(hammer):
   line = input()
   words = line.split()
   numbers = [int(word) for word in words]
   for number in numbers:
      print(hammer(number))

		
master(f1)
master(f2)
