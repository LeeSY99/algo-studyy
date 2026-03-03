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

        int[] sick_p = new int[S];
        int[] sick_t = new int[S];
        for (int i=0; i<S; i++) {
            sick_p[i] = sc.nextInt();
            sick_t[i] = sc.nextInt();
            
        }
        int answer = 0;
        for (int cheese=1; cheese<M+1; cheese++){
            boolean possible = true;

            for (int i=0; i<S && possible; i++){
                int p = sick_p[i];
                int t = sick_t[i];

                boolean eat = false;
                for (int j=0; j<D; j++){
                    if (record_p[j] == p && record_m[j] == cheese && record_t[j] < t){
                        eat = true;
                        break;
                    }
                }
                if (!eat) possible = false;
            }
            if (!possible) continue;
            boolean[] ate = new boolean[N+1];
            int cnt = 0;
            for (int j = 0; j<D; j++){
                if (record_m[j] == cheese && !ate[record_p[j]]){
                    ate[record_p[j]] = true;
                    cnt++;
                }
            }
            answer = Math.max(answer, cnt);
        }
        System.out.println(answer);
    }
}