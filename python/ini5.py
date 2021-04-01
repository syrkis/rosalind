with open('rosalind_ini5.txt', 'r') as f:
    data = f.readlines()

data = data[1::2]
for d in data:
    print(d.strip())
