import java.util.*;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int D = sc.nextInt();
        int S = sc.nextInt();
        boolean[] sick = new boolean[N+1];
        boolean[] rotten = new boolean[M+1];
        int[] record_p = new int[D];
        int[] record_m = new int[D];
        int[] record_t = new int[D];

        for (int i=0; i<D; i++) {
            int p = sc.nextInt();
            int m = sc.nextInt();
            int t = sc.nextInt();
            record_p[i] = p;
            record_m[i] = m;
            record_t[i] = t;
        }

        for (int i=0; i<S; i++) {
            int p = sc.nextInt();
            int t = sc.nextInt();
            sick[p] = true;

            for (int j=0; j<D; j++){
                int time = record_t[j];
                int cheese_num = record_m[j];
                int person_num = record_p[j];
                if (time < t && p == person_num){
                    rotten[cheese_num] = true;
                }
            }
        }
        for (int i=0; i<D; i++) {
            int cheese_num = record_m[i];
            int person_num = record_p[i];
            if (rotten[cheese_num] == true) {
                sick[person_num] = true;
            }
        }
        int answer = 0;
        for (int i=0; i<N+1; i++) {
            if (sick[i] == true){
                answer++;
            }
        }
        System.out.println(answer);
    }
}