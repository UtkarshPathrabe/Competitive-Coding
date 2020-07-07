import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class Solution {

    // Complete the migratoryBirds function below.
    static int migratoryBirds(List<Integer> arr) {
        int[] frequencyArray = new int[5];
        for (Integer i : arr) {
            frequencyArray[i-1] += 1;
        }
        int maxFrequency = frequencyArray[0];
        int maxFrequencyBird = 1;
        for (int i = 1; i < frequencyArray.length; i++) {
            if (frequencyArray[i] > maxFrequency) {
                maxFrequency = frequencyArray[i];
                maxFrequencyBird = i+1;
            }
        }
        return maxFrequencyBird;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int arrCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        int result = migratoryBirds(arr);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
