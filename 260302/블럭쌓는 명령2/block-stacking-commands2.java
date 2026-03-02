import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int block[] = new int[N+1];

        for (int i = 0; i < K; i++) {
            int A = sc.nextInt();
            int B = sc.nextInt();
            for (int j = A; j < B+1; j++){
                block[j]++;
            }
        }

        int ans = 0;
        for (int i = 0; i<N+1; i++) {
            ans = Math.max(ans, block[i]);
        }
        System.out.println(ans);
        // Please write your code here.
    }
}