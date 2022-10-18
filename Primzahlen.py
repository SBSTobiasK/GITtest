iteration = 1
saveprime = open("saveprime.txt", "w")
prime_candidate = input("Geben sie eine Zahl ein: ")
prime_candidate = int(prime_candidate)
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