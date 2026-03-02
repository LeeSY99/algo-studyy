import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] drs = new int[]{0,1,0,-1};
        int[] dcs = new int[]{1,0,-1,0};
        int r = 0;
        int c = 0;

        for (int i = 0; i < n; i++) {
            char direction = sc.next().charAt(0);
            int distance = sc.nextInt();
            int dir = 0;
            if (direction == 'N') {
                dir = 1;
            }else if (direction == 'E'){
                dir = 0;
            }else if (direction == 'S'){
                dir = 3;
            }else{
                dir = 2;
            }
            r = r + drs[dir]*distance;
            c = c + dcs[dir]*distance;
            // Please write your code here.
        }
        System.out.printf("%d %d", c,r);

    }
}