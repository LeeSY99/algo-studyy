import java.util.*;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] a = new int[n];
        for (int i=0; i<n; i++){
            a[i] = sc.nextInt();
        }

        int ans = 10000;
        for (int i = 1; i<10001; i++) {
            boolean possible = true;
            int count = 1;
            int sum = 0;
            for (int j=0; j<n; j++){
                if(a[j] > i){
                    possible = false;
                    break;
                }
                if (sum+a[j] > i){
                    sum = 0;
                    count++;
                }
                sum += a[j];
            }
            if(possible && count <=m){
                ans = Math.min(ans, i);
            }
        }
        System.out.println(ans);
    }
}