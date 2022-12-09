nbr = int(input('Entrez un nombre : '))

def facto():
    fact = 1
    for i in range(1, nbr+1):
      fact = fact * i
    print (nbr,'! = ',fact)

facto()