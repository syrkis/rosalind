import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String dna = sc.next();

        int countArray[];
        countArray = new int[4];

        for(char c : dna.toCharArray()) {
            if (c == 'A') {
                countArray[0]++;
            } else if (c == 'C') {
                countArray[1]++;
            } else if (c == 'G') {
                countArray[2]++;
            } else {
                countArray[3]++;
            }
        }

        for ( int c : countArray) {
            System.out.printf(c + " ");
        }
        
    } 
}
