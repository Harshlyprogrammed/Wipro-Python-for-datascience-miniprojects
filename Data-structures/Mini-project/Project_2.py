scores = [86,40,90,98,68,99,78,89]

winner = max(scores)
runnerup =0

for i in scores:
    if runnerup<=i<winner:
        runnerup=i
print(runnerup)