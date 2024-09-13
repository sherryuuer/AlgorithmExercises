import java.util.Arrays;

public class BinSort {
    public static void main(String[] args) {
        int[] data = { 2, 6, 3, 1, 4, 5 };
        int[] bins = binSort(data);
        System.out.println(Arrays.toString(bins));

    }

    static int[] binSort(int[] data) {
        int max = Arrays.stream(data).max().orElse(0);
        int n = data.length;
        int[] bins = new int[max + 1];

        for (int i = 0; i < n; i++) {
            bins[data[i]] = data[i];
        }

        return bins;

    }
}

// 会得到排序好的列表
