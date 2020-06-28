import java.util.Scanner;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";
        smallest = largest = s.substring(0, k);
        for (int i = 1; i < s.length() - k + 1; i++) {
            String tempSubString = s.substring(i, i+k);
            if (smallest.compareTo(tempSubString) > 0) {
                smallest = tempSubString;
            }
            if (largest.compareTo(tempSubString) < 0) {
                largest = tempSubString;
            }
        }
        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}