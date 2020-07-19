import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the isValid function below.
    static String isValid(String s) {
        Map<Character, Integer> characterFrequency = new HashMap<Character, Integer>();
        for (char c : s.toCharArray()) {
            characterFrequency.put(c, characterFrequency.getOrDefault(c, 0) + 1);
        }
        Map<Integer, Integer> frequencyOfCharacterFrequency = new HashMap<Integer, Integer>();
        for (int i : characterFrequency.values()) {
            frequencyOfCharacterFrequency.put(i, frequencyOfCharacterFrequency.getOrDefault(i, 0) + 1);
        }
        if ((frequencyOfCharacterFrequency.size() == 0) || (frequencyOfCharacterFrequency.size() == 1)) {
            return "YES";
        } else if (frequencyOfCharacterFrequency.size() > 2) {
            return "NO";
        } else {
            if (frequencyOfCharacterFrequency.values().contains(1)) {
                if (frequencyOfCharacterFrequency.get(Collections.min(frequencyOfCharacterFrequency.keySet())) == 1 || (Collections.max(frequencyOfCharacterFrequency.keySet()) - Collections.min(frequencyOfCharacterFrequency.keySet()) == 1)) {
                    return "YES";
                } else {
                    return "NO";
                }
            } else {
                return "NO";
            }
        }
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = scanner.nextLine();

        String result = isValid(s);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
