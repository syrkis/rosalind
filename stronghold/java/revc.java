import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String dna = sc.next();
        for (int i = dna.length() - 1; i >= 0 ; --i) {
            char c = dna.charAt(i);
            if (c == 'A') {
                System.out.print("T");
            } else if (c == 'C') {
                System.out.print("G");
            } else if (c == 'G') {
                System.out.print("C");
            } else {
                System.out.print("A");
            }
        }
    }
}

