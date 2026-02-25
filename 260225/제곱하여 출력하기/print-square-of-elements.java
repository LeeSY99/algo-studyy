import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];

        for (int i = 0; i<n; i++){
            nums[i] = sc.nextInt();
        }
        // System.out.print(nums);
        for (int i = 0; i<n; i++){
            System.out.print(nums[i] * nums[i] + " ");
        }
    }
}