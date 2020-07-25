import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    // Complete the luckBalance function below.
    static int luckBalance() {
        String[] nk = scanner.nextLine().split(" ");
        int n = Integer.parseInt(nk[0]);
        int k = Integer.parseInt(nk[1]);
        int luckSum = 0;
        List<Integer> importantContestLuck = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            String[] contestsRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
            int luck = Integer.parseInt(contestsRowItems[0]);
            int importance = Integer.parseInt(contestsRowItems[1]);
            if (importance == 1) {
                importantContestLuck.add(luck);
            } else {
                luckSum += luck;
            }
        }
        Collections.sort(importantContestLuck, Collections.reverseOrder());
        for (int i = 0; i < importantContestLuck.size(); i++) {
            if (i < k) {
                luckSum += importantContestLuck.get(i);
            } else {
                luckSum -= importantContestLuck.get(i);
            }
        }
        return luckSum;
    }

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int result = luckBalance();

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
