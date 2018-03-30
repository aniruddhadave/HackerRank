import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double a = scan.nextDouble();
        double b = scan.nextDouble();
        scan.close();
        
        double dailyCostA = 160 + 40 * (a + Math.pow(a, 2));
        double dailyCostB = 128 + 40 * (b + Math.pow(b, 2));
        
        System.out.printf("%.3f%n", dailyCostA);
        System.out.printf("%.3f%n", dailyCostB);
        
    }
}