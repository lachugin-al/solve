package day3conditionalstatements;

import java.util.*;

public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        if (N < 2) {
            if (N % 2 == 0) {
                System.out.print("Weird");
            } else {
                System.out.print("Not Weird");
            }
        } else if (N >=2 && N <= 5) {
            if (N % 2 == 0) {
                System.out.print("Not Weird");
            } else {
                System.out.print("Weird");
            }
        } else if (N >=6 && N <= 20) {
            if (N % 2 == 0) {
                System.out.print("Weird");
            } else {
                System.out.print("Not Weird");
            }
        } else {
            if (N % 2 == 0) {
                System.out.print("Not Weird");
            } else {
                System.out.print("Weird");
            }
        }

        scanner.close();
    }
}
