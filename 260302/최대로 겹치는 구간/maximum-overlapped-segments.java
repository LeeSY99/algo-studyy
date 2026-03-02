import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] x1 = new int[n];
        int[] x2 = new int[n];
        for (int i = 0; i < n; i++) {
            x1[i] = sc.nextInt();
            x2[i] = sc.nextInt();
        }
        int[] lines = new int[201];
        for (int i = 0; i<n; i++){
            int a = x1[i]+100;
            int b = x2[i]+100;
            for (int j = a; j<b; j++){
                lines[j]++;
            }
        }
        int ans = 0;
        for (int i: lines){
            ans = Math.max(ans, i);
        }
        System.out.println(ans);
        
        // Please write your code here.
    }
}