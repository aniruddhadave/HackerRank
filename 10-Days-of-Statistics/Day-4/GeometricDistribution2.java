import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        /* Read Input */
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        int denom = scan.nextInt();
        int inspection = scan.nextInt();
        
        double defectProbability = num / (denom * 1.0);
        double result = 0d;
        for (int i=1; i<= inspection; i++) {
                result += getGeometricDistribution(i, defectProbability);
        }
        System.out.printf("%.3f", result);
    }
    
    /* Calculates the Geometric Distribution given number of trials 
        required for a single succes and the probability of success */
    public static double getGeometricDistribution(int noOfTrials, double probabilityOfSuccess) {
        return Math.pow(1-probabilityOfSuccess, noOfTrials -1) * probabilityOfSuccess;
    }

}