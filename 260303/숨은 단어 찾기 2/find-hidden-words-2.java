import java.util.Scanner;
public class Main {
    public static int n,m;
    public static boolean in_range(int r, int c){
        return 0 <= r && r<n && 0<=c && c<m;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        String[] arr = new String[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.next();
        }
        // Please write your code here.
        int[] drs = new int[]{0,1,1,1,0,-1,-1,-1,};
        int[] dcs = new int[]{1,1,0,-1,-1,-1,0,1,};
        int answer = 0;
        for (int r=0; r<n; r++) {
            String str = arr[r];
            for (int c = 0; c<m; c++){
                if (str.charAt(c) == 'L'){
                    for (int k=0; k<8; k++){
                        int count = 1;
                        int cr = r;
                        int cc = c;
                        while (true){
                            int nr = cr + drs[k];
                            int nc = cc + dcs[k];
                            if (in_range(nr,nc) == false)
                                break;
                            if (arr[nr].charAt(nc) != 'E')
                                break;
                            count++;
                            cr = nr;
                            cc = nc;                            
                        }
                        if (count >=3)
                            answer++;
                    }
                }
            }
        }
        System.out.println(answer);
    }
    
}