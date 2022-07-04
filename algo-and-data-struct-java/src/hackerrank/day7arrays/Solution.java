package day7arrays;

import java.util.*;

public class Solution {
  private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n]; // create array int

        String[] arrItems = scanner.nextLine().split(" "); // input array string from console
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]); // parse string to int
            arr[i] = arrItem;   // add int to array int
        }

        // reverse elements in array
        int temp;
        for (int i = 0; i < n / 2; i++) {
            temp = arr[n - i - 1];
            arr[n - i - 1] = arr[i];
            arr[i] = temp;
        }

        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
        scanner.close();
    }
}
