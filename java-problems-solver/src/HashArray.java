import java.util.Arrays;

public class HashArray {
    public static void main(String[] args) {
        int[] arr = new int[5];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = -1;
        }
        System.out.println(Arrays.toString(arr));
        add(arr, 3);
        add(arr, 18);
        add(arr, 11);
        System.err.println(Arrays.toString(arr));
    }

    public static boolean add(int[] arr, int value) {
        int i = calcHash1(arr, value);
        if (i < arr.length && arr[i] == -1) {
            arr[i] = value;
            return true;
        } else {
            i = calcHash2(arr, value);
            if (i < arr.length && arr[i] == -1) {
                arr[i] = value;
                return true;
            }
        }
        return false;

    }

    public static int calcHash1(int[] arr, int value) {
        return (value % arr.length) + 1;
    }

    public static int calcHash2(int[] arr, int value) {
        return ((value + 3) % arr.length) + 1;
    }
}
