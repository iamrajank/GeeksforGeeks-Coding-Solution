//{ Driver Code Starts

// } Driver Code Ends
//Back-end complete function Template for Java
import java.util.*;

public class Main {
    public static void main(String args[]) {
        // Your Code Here
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int m=n*10;
        while(m>0){
            System.out.print(m+" " );
            m=m-n;
        }
    }
}

//{ Driver Code Starts.
// } Driver Code Ends