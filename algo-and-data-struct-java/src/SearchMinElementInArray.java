public class SearchMinElementInArray {
    public static void main(String[] args) {
        int[] array = new int[]{1, 3, 4, 2, 6, 3, 7, 3, 8, 9, 0};
        int minValue = array[0];
        int minIndex = 0;

        for (int i = 1; i < array.length; i++) {
            if (array[i] < minValue) {
                minValue = array[i];
                minIndex = i;
            } else continue;
        }
        System.out.println("Minimal Value in array: " + minValue + "\n"
                            + "Index this Value: " + minIndex);
    }
}