import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        int size = scan.nextInt();
        int[] x = new int[size];
        int[] weights = new int[size];
        for (int i=0; i<size; i++) {
            x[i] = scan.nextInt();
        }
        
        for (int i=0; i<size; i++) {
            weights[i] = scan.nextInt();
        }
        scan.close();
        
        System.out.format("%.1f",getWeightedMean(x, weights));
        
    }
    /* Calculates Weighted Mean */
    public static double getWeightedMean(int[] a, int[] w) {
        double weightedSum = 0d;
        int size = a.length;
        double totalWeight = 0d;
        for (int i = 0; i<a.length; i++) {
            weightedSum += a[i] * w[i];
            totalWeight += w[i];
        }
        // double totalWeight = IntStream.of(w).sum();
        return (weightedSum/totalWeight);
    }
}