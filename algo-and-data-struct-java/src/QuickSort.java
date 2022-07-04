public class QuickSort {
    public static void main(String[] args) {
        int[] array = new int[]{2, 1, 3, 5, 34, 23, 66, 34, 24, 47, 75, 89, 99, 65};
        System.out.println(arrayToString(array));
        measureTime(() -> quickSort(array, 0, array.length - 1));

        // запускаем тест
        test();
    }

    private static void quickSort(int[] array, int from, int to) {
        if (from < to) {
            int divideIndex = partition(array, from, to);
            quickSort(array, from, divideIndex - 1);
            quickSort(array, divideIndex, to);
        }
    }

    // разбиваем массив на 2 части от центрального элемента(либо того который укажем как центральный)
    // пробегаем по правой и левой частям
    private static int partition(int[] array, int from, int to) {
        int leftIndex = from;
        int rightIndex = to;
        int centerIndex = array[from + (to - from) / 2];
        while (leftIndex <= rightIndex) {
            while (array[leftIndex] < centerIndex) {
                leftIndex++;
            }
            while (array[rightIndex] > centerIndex) {
                rightIndex--;
            }
            if (leftIndex <= rightIndex) {
                swap(array, rightIndex, leftIndex);
                leftIndex++;
                rightIndex--;
            }
        }
        return leftIndex;
    }

    // меняем местами элементы в массиве
    private static void swap(int[] array, int rightIndex, int leftIndex) {
        int tmp = array[rightIndex];
        array[rightIndex] = array[leftIndex];
        array[leftIndex] = tmp;
    }

    // выводим массив в консоль
    private static String arrayToString(int[] array) {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = 0; i < array.length; i++) {
            if (i > 0) {
                sb.append(", ");
            }
            sb.append(array[i]);
        }
        sb.append("]");
        return sb.toString();
    }

    private static void test() {
        int arraySize = 100000;
        int[] array1 = new int[arraySize];

        System.out.println("Заполняем массив случайными числами");

        for (int i = 0; i < arraySize; i++) {
            array1[i] = (int) Math.round(Math.random()*1000);
        }

        measureTime(() -> quickSort(array1, 0, arraySize-1));
    }

    private static void measureTime(Runnable task) {
        long startTime = System.currentTimeMillis();
        task.run();
        long elapsed = System.currentTimeMillis() - startTime;
        System.out.println("Затраченное время: " + elapsed + " мс");
    }

}
