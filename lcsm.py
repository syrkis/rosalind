from sys import stdin
data = ["".join(line.split()[1:]) for line in stdin.read().split('>')[1:]]

def ngram(seq, n):
    ngrams = []
    for i in range(len(seq) - (n - 1)):
        ngrams.append(seq[i:i+n])
    return ngrams

def inall(seqs, gram, n):
    for seq in seqs:
        ngrams = ngram(seq, n)
        if gram not in ngrams:
            return False
    return True

def runner():
    for i in range(min([len(seq) for seq in data])):
        n = min([len(seq) for seq in data]) - i
        for seq in data:
            ngrams = ngram(seq, n)
            for gram in ngrams:
                if inall(data, gram, n):
                    return gram

print(runner())
