data = [16590, 17049, 17568, 19604, 16172, 17877]
prob = [1, 1, 1, 0.75, 0.5, 0]
out = 0 

for i in range(len(data)):
    out += data[i] * prob[i]

print(out * 2)
