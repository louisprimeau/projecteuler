
            
sumofsquares = 0
squareofsum = 0
for x in range(1,101):
    sumofsquares += x*x
    squareofsum += x
squareofsum = squareofsum * squareofsum

print(squareofsum - sumofsquares)
