import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        int size = scan.nextInt();
        int[] x = new int[size];
        for (int i=0;i<size; i++) {
            x[i] = scan.nextInt();
        }
        double mean = getMean(x);
        double squaredDistance = 0;
        for (int i =0; i<size; i++) {
            squaredDistance += (x[i] -mean)*(x[i] -mean);
        }
        System.out.println(Math.sqrt(squaredDistance/size));
    }
    
    /* Calculates Mean */  
    public static double getMean(int[] a) {
        // int sum = IntStream.of(a).sum();
        int sum = 0;
        for (int i = 0;i < a.length;i++) {
            sum += a[i];
        }
        return (double) sum/a.length;
    }

}