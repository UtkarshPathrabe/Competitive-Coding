import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the maxSubsetSum function below.
    static int maxSubsetSum(int[] arr) {
        int[] subsetSum = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            if (i == 0) {
                subsetSum[i] = arr[0];
            } else if (i == 1) {
                subsetSum[i] = Math.max(arr[1], arr[0]);
            } else {
                subsetSum[i] = Math.max(Math.max(arr[i], subsetSum[i-1]), subsetSum[i-2] + arr[i]);
            }
        }
        return subsetSum[subsetSum.length - 1];
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }

        int res = maxSubsetSum(arr);

        bufferedWriter.write(String.valueOf(res));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
