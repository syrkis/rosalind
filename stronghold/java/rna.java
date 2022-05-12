import java.util.Scanner;

class main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);        
        String dna = sc.next();
        
        for ( char c : dna.toCharArray()) {
            if (c == 'T') {
                System.out.printf('U' + "");
            } else {
                System.out.printf(c + "");
            }
        }
    }   
}
