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

    // Complete the countTriplets function below.
    static long countTriplets(List<Long> arr, long r) {
        Map<Long, Long> mapOfDuplets = new HashMap<>();
        Map<Long, Long> mapOfTriplets = new HashMap<>();
        long count = 0;
        for (long i : arr) {
            if (mapOfTriplets.containsKey(i)) {
                count += mapOfTriplets.get(i);
            }
            if (mapOfDuplets.containsKey(i)) {
                if (mapOfTriplets.containsKey(i*r)) {
                    mapOfTriplets.put(i*r, mapOfTriplets.get(i*r) + mapOfDuplets.get(i));
                } else {
                    mapOfTriplets.put(i*r, mapOfDuplets.get(i));
                }
            }
            if (mapOfDuplets.containsKey(i*r)) {
                mapOfDuplets.put(i*r, mapOfDuplets.get(i*r) + 1);
            } else {
                mapOfDuplets.put(i*r, 1L);
            }
        }
        return count;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nr = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(nr[0]);

        long r = Long.parseLong(nr[1]);

        List<Long> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Long::parseLong)
            .collect(toList());

        long ans = countTriplets(arr, r);

        bufferedWriter.write(String.valueOf(ans));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
