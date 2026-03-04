import java.util.*;
public class Main {
    public static int n;
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        String str = sc.next();
        System.out.println(check(str));
    }

    public static int check(String str){
        for (int lenth=1; lenth<n+1; lenth++) {
            boolean is = false;
            for(int i=0; i<n-lenth+1; i++) {
                for(int j=i+1; j<n-lenth+1; j++) {
                    if (str.substring(i,i+lenth).equals(str.substring(j,j+lenth)))
                        is = true;
                }
            }
            if (is==false) 
                return lenth;
        }
        return n;
    }
}