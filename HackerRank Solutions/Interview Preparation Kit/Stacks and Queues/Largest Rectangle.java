import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the largestRectangle function below.
    static long largestRectangle(int[] h) {
        long maxArea = 0L;
        for (int i = 0; i < h.length; i++) {
            int leftIndexWithValidHeight = i;
            for ( ; leftIndexWithValidHeight > 0; leftIndexWithValidHeight--) {
                if (h[leftIndexWithValidHeight-1] < h[i]) {
                    break;
                }
            }
            int rightIndexWithValidHeight = i;
            for ( ; rightIndexWithValidHeight < h.length - 1; rightIndexWithValidHeight++) {
                if (h[rightIndexWithValidHeight+1] < h[i]) {
                    break;
                }
            }
            long area = h[i] * (rightIndexWithValidHeight - leftIndexWithValidHeight + 1);
            if (area > maxArea) {
                maxArea = area;
            }
        }
        return maxArea;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] h = new int[n];

        String[] hItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int hItem = Integer.parseInt(hItems[i]);
            h[i] = hItem;
        }

        long result = largestRectangle(h);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
