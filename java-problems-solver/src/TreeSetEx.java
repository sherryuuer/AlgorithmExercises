import java.util.TreeSet;

public class TreeSetEx {

    public static void main(String[] args) {
        // 创建一个 TreeSet 对象
        TreeSet<String> treeSet = new TreeSet<>();

        // 插入元素
        treeSet.add("Apple");
        treeSet.add("Banana");
        treeSet.add("Cherry");
        treeSet.add("Date");
        treeSet.add("Fig");

        // 输出整个 TreeSet
        System.out.println("TreeSet: " + treeSet); // 输出: [Apple, Banana, Cherry, Date, Fig]

        // 获取最小和最大元素
        String first = treeSet.first();
        String last = treeSet.last();
        System.out.println("First element: " + first); // 输出: Apple
        System.out.println("Last element: " + last); // 输出: Fig

        // 获取子集
        System.out.println("HeadSet 'Cherry': " + treeSet.headSet("Cherry")); // 输出: [Apple, Banana]
        System.out.println("TailSet 'Cherry': " + treeSet.tailSet("Cherry")); // 输出: [Cherry, Date, Fig]
        System.out.println("SubSet 'Banana' to 'Fig': " + treeSet.subSet("Banana", "Fig")); // 输出: [Banana, Cherry,
                                                                                            // Date]

        // 遍历 TreeSet
        System.out.println("Iterating over TreeSet:");
        for (String element : treeSet) {
            System.out.println(element);
        }

        // 尝试插入重复元素
        boolean added = treeSet.add("Banana"); // 不会插入，返回 false
        System.out.println("Was 'Banana' added again? " + added); // 输出: false

        // 清空集合
        treeSet.clear();
        System.out.println("TreeSet after clearing: " + treeSet); // 输出: []
    }
}

// Tree都是有序的，Hash都是无序的
