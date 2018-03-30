import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        // Read Input
        Scanner scan = new Scanner(System.in);
        double mean = scan.nextDouble();
        int k = scan.nextInt();
        
        System.out.printf("%.3f", getPoissonProbability(mean, k));
    }
    
    /* Claculates the poisson probability */
    private static double getPoissonProbability(double lambda, int k) {
        return Math.pow(lambda, k) * Math.pow(Math.E, -1*lambda)/ factorial(k);
    }
    
    /* Calculates Factorial*/
    private static Long factorial(int n) {
        if (n < 0) return null;
        else if (n==1 || n==0) return 1l;
        else {
            long ans = 1l;
            ans = n*factorial(n-1);
            return ans;
        }
    }
}