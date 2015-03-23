import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    private static int UKS (int value[], int n, int k) {
		int Max[] = new int[k + 1], temp = -9999;
		Max[0] = 0;
		for (int i = 1; i <= k; i++) {
			Max[i] = Max[i - 1];
			for (int j = 0; j < n; j++) {
				if (i >= value[j]) {
					temp = Max[i - value[j]] + value[j];
				}
				if (temp > Max[i]) {
					Max[i] = temp;
				}
			}
		}
		return Max[k];
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int T;
		T = in.nextInt();
		while ((T--) > 0) {
			int n = in.nextInt(), k = in.nextInt();
			int value[] = new int[n];
			for (int i = 0; i < n; i++) {
				value[i] = in.nextInt();
			}
			System.out.println(UKS(value, n, k));
		}
		in.close();
	}
    
}