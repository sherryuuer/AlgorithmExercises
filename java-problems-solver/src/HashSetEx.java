import java.util.HashSet;

public class HashSetEx {
    public static void main(String[] args) {
        // 创建一个 HashSet 来存储整数
        HashSet<Integer> set = new HashSet<>();

        // 添加元素到 HashSet
        set.add(10);
        set.add(20);
        set.add(30);
        set.add(40);
        set.add(20); // 添加重复元素，HashSet 不会保存

        // 打印 HashSet 的内容
        System.out.println("HashSet 内容: " + set);

        // 检查 HashSet 中是否包含某个元素
        boolean contains30 = set.contains(30);
        System.out.println("是否包含30: " + contains30);

        // 删除 HashSet 中的某个元素
        set.remove(10);
        System.out.println("删除元素后: " + set);

        // 遍历 HashSet
        System.out.println("遍历 HashSet:");
        for (int i : set) {
            System.out.println(i);
        }

        // 获取 HashSet 的大小
        System.out.println("HashSet 大小: " + set.size());

        // 清空 HashSet
        set.clear();
        System.out.println("清空后 HashSet 大小: " + set.size());
    }
}
