import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the plusMinus function below.
    static void plusMinus(int[] arr) {
        double positiveNumbers = 0;
        double negativeNumbers = 0;
        double zeroes = 0;
        double totalNumbers = arr.length;
        for (int i = 0; i < totalNumbers; i++) {
            if (arr[i] > 0) {
                positiveNumbers++;
            } else if (arr[i] < 0) {
                negativeNumbers++;
            } else {
                zeroes++;
            }
        }
        System.out.println(positiveNumbers / totalNumbers);
        System.out.println(negativeNumbers / totalNumbers);
        System.out.println(zeroes / totalNumbers);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }

        plusMinus(arr);

        scanner.close();
    }
}
