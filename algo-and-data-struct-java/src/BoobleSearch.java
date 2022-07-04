import java.awt.image.AreaAveragingScaleFilter;
import java.util.Arrays;

public class BoobleSearch {
    public static void main(String[] args) {
        int[] array = new int[]{1, 3, 4, 2, 6, 3, 7, 3, 8, 9, 0};

        // Quicksort
        Arrays.sort(array);
        int[] sortedArray = array;
        System.out.println(Arrays.toString(sortedArray));

        boolean isSorted;
        do {
            isSorted = true;
            for (int i = 1; i < array.length; i++) {
                if (array[i] < array[i - 1]) {
                    int tmp = array[i];
                    array[i] = array[i - 1];
                    array[i - 1] = tmp;
                    isSorted = false;
                }
            }
        } while (!isSorted);
        printArray(array);
    }

    private static void printArray(int[] arr) {
        System.out.print("[");
        for (int i = 0; i < arr.length; i++) {
            if (i > 0) {
                System.out.print(", ");
            }
            System.out.print(arr[i]);
        }
        System.out.print("]\n");
    }
}
