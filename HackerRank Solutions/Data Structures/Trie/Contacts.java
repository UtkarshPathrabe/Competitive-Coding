import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    static int[] contacts(String[][] queries, int numberOfFindQueries) {
        Map<String, Integer> contactMap = new HashMap<>();
        int[] result = new int[numberOfFindQueries];
        int resultIndex = 0;
        for (String[] query : queries) {
            if (query[0].equalsIgnoreCase("add")) {
                for (int i = 1; i <= query[1].length(); i++) {
                    contactMap.put(query[1].substring(0, i), contactMap.getOrDefault(query[1].substring(0, i), 0) + 1);
                }
            } else {
                result[resultIndex++] = contactMap.getOrDefault(query[1], 0);
            }
        }
        return result;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int queriesRows = Integer.parseInt(scanner.nextLine().trim());

        String[][] queries = new String[queriesRows][2];
        int numberOfFindQueries = 0;

        for (int queriesRowItr = 0; queriesRowItr < queriesRows; queriesRowItr++) {
            String[] queriesRowItems = scanner.nextLine().split(" ");
            if (queriesRowItems[0].equalsIgnoreCase("find")) {
                numberOfFindQueries++;
            }
            for (int queriesColumnItr = 0; queriesColumnItr < 2; queriesColumnItr++) {
                String queriesItem = queriesRowItems[queriesColumnItr];
                queries[queriesRowItr][queriesColumnItr] = queriesItem;
            }
        }

        int[] result = contacts(queries, numberOfFindQueries);

        for (int resultItr = 0; resultItr < result.length; resultItr++) {
            bufferedWriter.write(String.valueOf(result[resultItr]));

            if (resultItr != result.length - 1) {
                bufferedWriter.write("\n");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();
    }
}
