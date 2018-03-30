import java.io.*;
import java.util.*;
import java.util.stream.*;
public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double percentageDefective = scan.nextInt()/100d;
        double currentBatchSize = scan.nextInt();
        double noMorethan2 = 0d;
        for (int i=0; i<= 2; i++) {
            noMorethan2 += binomialProbability(10, i, percentageDefective);
        }
        System.out.format("%.3f%n", noMorethan2);

        double atleast2 = 1 - noMorethan2 + binomialProbability(10, 2, percentageDefective);
        System.out.format("%.3f%n", atleast2);
        
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
    
    /* Calculates the number of combinations */
    private static Long combinations(int n, int r) {
        if (n < 0 || r < 0 || n < r) return null;
        return factorial(n) / (factorial(n-r) * factorial(r));
    }
    
    /* Calcaulates the Binomial Probability */
    private static Double binomialProbability(int n, int r, double p) {
        if (n < 0 || r < 0 || n < r || p > 1 || p <0) return null;
        return combinations(n, r) * Math.pow(p, r) * Math.pow(1-p, n-r);
    }
}