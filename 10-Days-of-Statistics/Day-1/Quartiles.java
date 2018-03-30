import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);
        int size = scan.nextInt();
        int[] x = new int[size];
        for (int i=0; i<size; i++) {
            x[i] = scan.nextInt();
        }
        System.out.println(getMedian(x, 0, x.length/2 -1));
        System.out.println(getMedian(x, 0, x.length -1));
        System.out.println(getMedian(x, (x.length + 1)/2, x.length -1));


    }
    /* Calculates Median given an array and the range of indices */
    public static int getMedian(int[] a, int fromIndex, int toIndex) {
        int median;
        int size = a.length;
        int[] copy = a.clone();
        Arrays.sort(copy);
        if ((toIndex - fromIndex) % 2 != 0) {
            int val1 = copy[(fromIndex + toIndex)/2];
            int val2 = copy[(fromIndex + toIndex)/2 + 1];
            median  = (val1 + val2)/2;
        } else {
            median  = copy[(fromIndex + toIndex)/2];
        }
        return median;
    }
}