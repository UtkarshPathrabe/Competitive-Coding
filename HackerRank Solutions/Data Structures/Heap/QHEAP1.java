import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Set<Integer> added = new HashSet<>();
        int numberOfQueries = scanner.nextInt();
        scanner.nextLine();
        int[] array = new int[numberOfQueries + 1];
        int count = 0;
        while (numberOfQueries-- > 0) {
            String result = scanner.nextLine();
            Scanner resultScanner = new Scanner(result);
            Integer item;
            switch (Integer.parseInt(resultScanner.next())) {
                case 1:
                    item = Integer.parseInt(resultScanner.next());
                    if (!added.contains(item)) {
                        added.add(item);
                        array[count+1] = item;
                        count++;
                        rising(array, count);
                    }
                    break;
                case 2:
                    item = Integer.parseInt(resultScanner.next());
                    for (int i = 1; i <= count; i++) {
                        if (array[i] == item) {
                            swap(array, i, count);
                            added.remove(item);
                            count--;
                            sinking(array, i, count);
                            break;
                        }
                    }
                    break;
                case 3:
                    System.out.println(array[1]);
                    break;
            }
        }

    }

    static void rising(int[] array, int index) {
        while (index > 1) {
            if (array[index] < array[index / 2]) {
                swap(array, index, index / 2);
                index = index / 2;
            } else {
                break;
            }
        }
    }

    static void sinking(int[] array, int index, int max) {
        while (2*index <= max) {
            int smallestChild = getSmallestIndex(array, index, max);
            if (array[smallestChild] < array[index]) {
                swap(array, smallestChild, index);
                index = smallestChild;
            } else {
                break;
            }
        }
    }

    static void swap(int[] array, int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    static int getSmallestIndex(int[] array, int index, int max) {
        if (2*index == max || array[2*index] < array[2*index+1]) {
            return 2*index;
        } else {
            return 2*index + 1;
        }
    }

}