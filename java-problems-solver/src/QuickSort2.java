import java.util.Arrays;

public class QuickSort2 {

    public static void main(String[] args) {
        int[] arr = { 9, 7, 5, 11, 12, 2, 14, 3, 10, 6 };
        System.out.println("Original Array: " + Arrays.toString(arr));

        quickSort2(arr, 0, arr.length - 1);

        System.out.println("Sorted Array: " + Arrays.toString(arr));
    }

    // 快速排序主方法
    public static void quickSort2(int[] arr, int low, int high) {
        if (low >= high) {
            return;
        }

        int pivot = arr[(low + high) / 2];
        int l = low;
        int r = high;

        while (l <= r) {
            while (arr[l] < pivot) {
                l++;
            }
            while (arr[r] > pivot) {
                r--;
            }

            if (l <= r) {
                int temp = arr[l];
                arr[l] = arr[r];
                arr[r] = temp;
                l++;
                r--;
            }
        }
        quickSort2(arr, low, r);
        quickSort2(arr, l, high);
    }
}
