import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        String s = sc.next();

        String newText = s.substring(0,1) + 'a' + s.substring(2,s.length()-2) + 'a' + s.substring(s.length()-1);
        System.out.println(newText);
    }
}