import java.util.Arrays;

public class ChoiceSearch {
    public static void main(String[] args) {
        int[] array = new int[]{1, 3, 4, 2, 6, 3, 7, 3, 8, 9, 0};

        for (int step = 0; step < array.length; step++) {
//            System.out.println(Arrays.toString(array));
            System.out.println(arrayToString(array));
            int index = min(array, step);
            int tmp = array[step];
            array[step] = array[index];
            array[index] = tmp;
        }


    }

    private static int min(int[] array, int start) {
        int minValue = array[start];
        int minIndex = start;
        for (int i = start; i < array.length; i++) {
            if (array[i] < minValue) {
                minValue = array[i];
                minIndex = i;
            }
        }
        return minIndex;
    }

    private static String arrayToString(int[] array) {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        sb.append(array[0]);
        for (int i = 1; i < array.length; i++) {
            sb.append(", ");
            sb.append(array[i]);
        }
        sb.append("]");
        return sb.toString();
    }
}
