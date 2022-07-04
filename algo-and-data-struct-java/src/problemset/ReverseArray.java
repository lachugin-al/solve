package problemset;

import java.util.Arrays;

public class ReverseArray {
    public static void main(String[] args) {
        String[] arr = {"a", "f", "w"};
        reverseArray(arr);
    }

    private static void reverseArray(String[] arr) {
        int n = arr.length;
        String temp;
        for (int i = 0; i < n / 2; i++) {
            temp = arr[i];
            arr[i] = arr[n - i - 1];
            arr[n - i - 1] = temp;
        }
        System.out.println(Arrays.toString(arr));
    }
}
