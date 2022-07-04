package day11arrays;

import java.util.*;

public class Solution {

  private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int[][] arr = new int[6][6];

        // row
        for (int i = 0; i < 6; i++) {
            String[] arrRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
            // column
            for (int j = 0; j < 6; j++) {
                int arrItem = Integer.parseInt(arrRowItems[j]);
                arr[i][j] = arrItem;
            }
        }
        System.out.println(maxHourglass(arr));
        scanner.close();
    }

    public static int maxHourglass(int[][] arr) {
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                int sum = sum(arr, i, j);
                max = Math.max(max, sum);
            }
        }
        return max;
    }

    // summing hourglass in 2D array
    public static int sum(int[][] arr, int a, int b) {
        int sum = arr[a + 0][b + 0] + arr[a + 0][b + 1] + arr[a + 0][b + 2]
                                    + arr[a + 1][b + 1]
                + arr[a + 2][b + 0] + arr[a + 2][b + 1] + arr[a + 2][b + 2];
        return sum;
    }
}

