import java.util.Arrays;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int[] ability = new int[6];
        for(int i=0; i<6; i++){
            ability[i] = sc.nextInt();
        }

        Arrays.sort(ability);
        int max_sum = 0;
        int min_sum = Integer.MAX_VALUE;

        for (int i=0; i<3; i++){
            int a_sum = ability[i] + ability[5-i];
            max_sum = Math.max(max_sum, a_sum);
            min_sum = Math.min(min_sum, a_sum);
        }
        System.out.println(max_sum-min_sum);
    }
}