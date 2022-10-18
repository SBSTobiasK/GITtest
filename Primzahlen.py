iteration = 1
saveprime = open("saveprime.txt", "a")
primesaved = open("saveprime.txt", "r")
while True:
  try:
    currentprime = int(primesaved.readlines()[-1])
    break
  except IndexError:
    currentprime = 0
    break
prime_candidate = input("Geben sie eine Zahl ein: ")
prime_candidate = int(prime_candidate)
if prime_candidate > currentprime:
  iteration = currentprime
  while iteration < prime_candidate:
    iteration = iteration + 1
    loop = 2
    while loop < iteration/2:
      loop = loop + 1
      if iteration % loop == 0:
        break
    if loop > iteration/2:
      print(iteration)
      saveprime.write(str(iteration))
      saveprime.write("\n")
  saveprime.close()

primesaved = open("saveprime.txt", "r")
for element in primesaved.readlines():
  if int(element) <= prime_candidate:
    print(element, end="")
primesaved.close()
