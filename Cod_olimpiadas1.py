def suma(a,b):
  x = a + b 
  return x

def resta(a,b):
  x = a - b
  return x

print("Dame el primer número")
a = int(input())
print ("Dame el segundo número:")
b = int(input())
print("La suma da ",suma(a,b), "y la resta da",resta(a,b))



def multiplicación(a,b):
  x = a * b
  return x

def división(a,b):
  x = a / b
  return x

print("Dame el primer número")
a = int(input())
print("Dame el segundo número")
b = int(input())
print("La multiplicación da ",multiplicación(a,b), "y la división da" ,división(a,b) )
