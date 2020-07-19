import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the commonChild function below.
    static int commonChild(String s1, String s2) {
        int l1 = s1.length();
        int l2 = s2.length();
        int[][] LCS = new int[2][l2+1];
        for (int i = 1; i <= l1; i++) {
            for (int j = 1; j <= l2; j++) {
                if (s1.charAt(i-1) == s2.charAt(j-1)) {
                    LCS[i%2][j] = LCS[(i-1)%2][j-1] + 1;
                } else {
                    LCS[i%2][j] = Math.max(LCS[(i-1)%2][j], LCS[i%2][j-1]);
                }
            }
        }
        return LCS[l1%2][l2];
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s1 = scanner.nextLine();

        String s2 = scanner.nextLine();

        int result = commonChild(s1, s2);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
