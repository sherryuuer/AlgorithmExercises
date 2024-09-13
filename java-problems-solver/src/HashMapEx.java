import java.util.HashMap;
import java.util.Map;

public class HashMapEx {

    public static void main(String[] args) {
        // 创建一个 HashMap 对象
        HashMap<String, Integer> hashMap = new HashMap<>();

        // 插入键值对
        hashMap.put("Apple", 10);
        hashMap.put("Banana", 20);
        hashMap.put("Cherry", 30);
        hashMap.put("Date", 40);
        hashMap.put("Fig", 50);

        // 输出整个 HashMap
        System.out.println("HashMap: " + hashMap); // 输出: {Apple=10, Banana=20, Cherry=30, Date=40, Fig=50}

        // 获取指定键的值
        int value = hashMap.get("Cherry");
        System.out.println("Value for key 'Cherry': " + value); // 输出: 30

        // 移除指定键的键值对
        hashMap.remove("Date");
        System.out.println("HashMap after removing 'Date': " + hashMap); // 输出: {Apple=10, Banana=20, Cherry=30, Fig=50}

        // 检查是否包含指定键和指定值
        boolean hasKey = hashMap.containsKey("Banana");
        boolean hasValue = hashMap.containsValue(50);
        System.out.println("Contains key 'Banana': " + hasKey); // 输出: true
        System.out.println("Contains value 50: " + hasValue); // 输出: true

        // 获取键集合、值集合和条目集合
        System.out.println("Key Set: " + hashMap.keySet()); // 输出: [Apple, Banana, Cherry, Fig]
        System.out.println("Values: " + hashMap.values()); // 输出: [10, 20, 30, 50]
        System.out.println("Entry Set: " + hashMap.entrySet()); // 输出: [Apple=10, Banana=20, Cherry=30, Fig=50]

        // 遍历 HashMap
        System.out.println("Iterating over HashMap:");
        for (Map.Entry<String, Integer> entry : hashMap.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}

// 快速查找，无序，线程不安全，基于哈希表
