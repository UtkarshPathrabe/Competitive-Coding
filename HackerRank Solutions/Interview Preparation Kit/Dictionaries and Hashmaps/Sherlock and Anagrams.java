import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the sherlockAndAnagrams function below.
    static int sherlockAndAnagrams(String s) {
        int count = 0;
        for (int subStringLength = 1; subStringLength <= s.length(); subStringLength++) {
            Map<String, Integer> subStringsFrequencyMap = new HashMap<>();
            for (int i = 0; i <= s.length() - subStringLength; i++) {
                String subString = s.substring(i, i + subStringLength);
                char[] tempArray = subString.toCharArray();
                Arrays.sort(tempArray);
                String sortedSubString = new String(tempArray);
                subStringsFrequencyMap.put(sortedSubString, subStringsFrequencyMap.getOrDefault(sortedSubString, 0) + 1);
            }
            for (String subString : subStringsFrequencyMap.keySet()) {
                count += (subStringsFrequencyMap.get(subString) * (subStringsFrequencyMap.get(subString) - 1)) / 2;
            }
        }
        return count;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int qItr = 0; qItr < q; qItr++) {
            String s = scanner.nextLine();

            int result = sherlockAndAnagrams(s);

            bufferedWriter.write(String.valueOf(result));
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
