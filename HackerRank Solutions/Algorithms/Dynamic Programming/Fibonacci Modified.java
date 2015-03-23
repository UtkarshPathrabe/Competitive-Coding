import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
		int A, B, N;
		BigInteger f1, f2, f3 = new BigInteger("0");
		A = in.nextInt();
		B = in.nextInt();
		N = in.nextInt();
		f1 = new BigInteger(Integer.toString(A));
		f2 = new BigInteger(Integer.toString(B));
		for (int i = 2; i < N; i++) {
			f3 = f1.add(f2.multiply(f2));
			f1 = f2;
			f2 = f3;
		}
		System.out.println(f3);
		in.close();
    }
}