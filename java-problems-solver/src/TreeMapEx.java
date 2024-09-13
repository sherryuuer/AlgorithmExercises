import java.util.Map;
import java.util.TreeMap;

public class TreeMapEx {

    public static void main(String[] args) {
        // 创建一个 TreeMap 对象
        TreeMap<String, Integer> treeMap = new TreeMap<>();

        // 插入键值对，会被排序的
        treeMap.put("Apple", 10);
        treeMap.put("Banana", 20);
        treeMap.put("Cherry", 30);
        treeMap.put("Date", 40);
        treeMap.put("Fig", 50);

        // 输出整个 TreeMap
        System.out.println("TreeMap: " + treeMap); // 输出: {Apple=10, Banana=20, Cherry=30, Date=40, Fig=50}

        // 获取指定键的值
        int value = treeMap.get("Cherry");
        System.out.println("Value for key 'Cherry': " + value); // 输出: 30

        // 移除指定键的键值对
        treeMap.remove("Date");
        System.out.println("TreeMap after removing 'Date': " + treeMap); // 输出: {Apple=10, Banana=20, Cherry=30, Fig=50}

        // 获取第一个键和最后一个键
        String firstKey = treeMap.firstKey();
        String lastKey = treeMap.lastKey();
        System.out.println("First key: " + firstKey); // 输出: Apple
        System.out.println("Last key: " + lastKey); // 输出: Fig

        // 获取指定键之前和之后的子映射
        System.out.println("HeadMap 'Cherry': " + treeMap.headMap("Cherry")); // 输出: {Apple=10, Banana=20}
        System.out.println("TailMap 'Cherry': " + treeMap.tailMap("Cherry")); // 输出: {Cherry=30, Fig=50}
        System.out.println("SubMap 'Banana' to 'Fig': " + treeMap.subMap("Banana", "Fig")); // 输出: {Banana=20,
                                                                                            // Cherry=30}

        // 遍历 TreeMap
        System.out.println("Iterating over TreeMap:");
        for (Map.Entry<String, Integer> entry : treeMap.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}

// 有序排列，对数时间复杂度，不允许null，他也是线程不安全的，基于红黑树（自平衡二叉树）
