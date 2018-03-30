import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);
        int size = scan.nextInt();
        int[] x = new int[size];
        int[] frequency = new int[size];
        int dataSize = 0;
        
        for (int i=0; i< size; i++) {
            x[i] = scan.nextInt();
        }
        for (int i=0; i< size; i++) {
            frequency[i] = scan.nextInt();
            dataSize += frequency[i];
        }
        scan.close();
        
        /* Create Data */
        int[] data = new int[dataSize];
        int index = 0;
        for (int i=0; i<size; i++) {
            for (int j=0; j<frequency[i]; j++) {
                data[index] = x[i];
                index++;
            }
        }
        double quartile1 = getMedian(data, 0, dataSize/2 -1);
        double quartile3 = getMedian(data, (dataSize +1)/2, dataSize -1);
        System.out.format("%.1f",quartile3 - quartile1);

    
    }
    
    /* Calculates Median given an array and the range of indices */
    public static double getMedian(int[] a, int fromIndex, int toIndex) {
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