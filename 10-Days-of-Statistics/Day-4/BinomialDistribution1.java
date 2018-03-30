import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double ratio_num = scan.nextDouble();
        double ratio_denom = scan.nextDouble();
        double a = 1.09;
        double prob = a /(1+a);
        int no_of_children = 6;
        double probability_boy = ratio_num / (ratio_num + ratio_denom) ;
        
        /* Calaculate the require proability*/
        double probability_atleast_3boys = 0d;
        for (int i = 3; i <= no_of_children; i++) {
            probability_atleast_3boys += binomialProbability(no_of_children, i, prob);
        }
        System.out.format("%.3f", probability_atleast_3boys);
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