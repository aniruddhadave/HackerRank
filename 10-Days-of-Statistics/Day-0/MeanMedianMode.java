import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
      
        Scanner scan = new Scanner(System.in); 
        int size = scan.nextInt();
        int[] a = new int[size];
        for (int i = 0; i<size; i++) {
            a[i] = scan.nextInt();
        }
        
        System.out.println(getMean(a));
        System.out.println(getMedian(a));
        System.out.println(getMode(a));
        
    }

        /* Calculate Mean */  
        public static double getMean(int[] a) {
            int sum = 0;
            for (int i = 0;i < a.length;i++) {
                sum += a[i];
            }
            return (double) sum/a.length;
        }
        /* Calculate Median */
        public static double getMedian(int[] a) {
            double median;
            int size = a.length;
            int[] copy = a.clone();
            Arrays.sort(copy);
            if (size % 2 == 0) {
                median  = (copy[size/2] +copy[size/2 - 1])/2.0d;
            } else {
                median  = copy[size/2];
            }
            return median;
        }
        
        /* Calculate Mode (In case of tie, return the number with a smaller value)*/
        public static int getMode(int[] a) {
            int  maxFreq = 1;
            int mode = Integer.MAX_VALUE;
            Map<Integer, Integer> modeMap = new HashMap<Integer, Integer>();
            for (int entry: a) {
                modeMap.merge(entry, 1, Integer::sum);
                int frequency = modeMap.get(entry);
                if (frequency > maxFreq || (frequency == maxFreq && entry < mode )) {
                    maxFreq = frequency;
                    mode = entry;
                }
            }
            return mode;
        }
}