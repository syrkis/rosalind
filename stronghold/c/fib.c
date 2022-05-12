#include <stdio.h>

int main() {
    int     count[5] = {0};
    char    dna[1000];

    scanf("%s", dna);    

    for (int i = 0; i < sizeof(dna) ; ++i) {
        if (dna[i] == 'A') {
            ++count[0];
        } else if (dna[i] == 'C') {
            ++count[1];
        } else if (dna[i] == 'G') {
            ++count[2];
        } else if (dna[i] == 'T') {
            ++count[3];
        } else {
            break;
        }
    }

    for (int i = 0; i < 4; ++i) {
        printf("%d ", count[i]);
    }

    return 0;
}
