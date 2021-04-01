with open('../data/rosalind_bins.txt', 'r') as f:
    n = int(f.readline().strip())
    m = int(f.readline().strip())
    A = list(map(int, f.readline().strip().split()))
    I = list(map(int, f.readline().strip().split()))

def bins(L, t, mi, ma):
    m = (mi + ma) // 2
    if mi  == ma - 1:
        if L[m] == t:
            return m + 1
        else:
            return -1

    elif L[m] <= t:
        return bins(L, t, m, ma)

    else:
        return bins(L, t, mi, m)
     

def main():
    with open('tmp.out', 'w') as f:
        for i in I:
            f.write(f"{bins(A, i, 0, n)} ")

if __name__ == '__main__':
    main()
