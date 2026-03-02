import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int[] selected = new int[3];
        int ans = 0;
        for (int i = 0; i<n; i++){
            selected[0] = arr[i];
            for (int j = i+1; j<n; j++){
                selected[1] = arr[j];
                for (int k = j+1; k<n; k++){
                    selected[2] = arr[k];
                    int a = selected[0];
                    int b = selected[1];
                    int c = selected[2];
                    boolean carry = false;

                    while (a != 0 && b!=0 && c!=0){
                        if (a%10 + b%10 + c%10 >= 10) {
                            carry = true;
                            break;
                        } else{
                            a = a/10;
                            b = b/10;
                            c = c/10;
                        }
                    }
                    if (!carry){
                        ans = Math.max(ans, selected[0]+selected[1]+selected[2]);
                    }
                }
            }
        }

        if (ans == 0){
            System.out.println(-1);
        } else{
            System.out.println(ans);
        }
    
        // Please write your code here.
    }
}