import java.util.Arrays;

public class QuickSort {

    public static void main(String[] args) {
        int[] arr = { 9, 7, 5, 11, 12, 2, 14, 3, 10, 6 };
        System.out.println("Original Array: " + Arrays.toString(arr));

        quickSort(arr, 0, arr.length - 1);

        System.out.println("Sorted Array: " + Arrays.toString(arr));
    }

    // 快速排序主方法
    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            // 找到分区点
            int pi = partition(arr, low, high);

            // 递归排序左子数组
            quickSort(arr, low, pi - 1);

            // 递归排序右子数组
            quickSort(arr, pi + 1, high);
        }
    }

    // 分区方法：将数组分为两个部分
    public static int partition(int[] arr, int low, int high) {
        // 选择最后一个元素作为枢轴
        int pivot = arr[high];
        int i = (low - 1); // 小于枢轴的元素索引

        for (int j = low; j < high; j++) {
            // 如果当前元素小于或等于枢轴
            if (arr[j] <= pivot) {
                i++;

                // 交换 arr[i] 和 arr[j]
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        System.out.println(i + 1);
        System.out.println(Arrays.toString(arr));

        // 交换 arr[i + 1] 和枢轴元素（arr[high]）
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        return i + 1; // 返回分区点的索引
    }
}
