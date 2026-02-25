import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        int[] arr = new int[10];
        arr[0] = a;
        arr[1] = b;

        for (int i = 2; i<10; i++){
            arr[i] = (arr[i-1]+arr[i-2]) % 10;
        }

        for (int num : arr){
            System.out.print(num + " ");
        }
    }
}