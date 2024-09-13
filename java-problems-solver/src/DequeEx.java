import java.util.Deque;
import java.util.ArrayDeque;

public class DequeEx {

    public static void main(String[] args) {
        // 创建一个 ArrayDeque 实现的 Deque
        Deque<String> deque = new ArrayDeque<>();

        // 作为队列使用 (FIFO)
        deque.addLast("A"); // 插入元素到队尾
        deque.addLast("B");
        deque.addLast("C");

        // 输出队列的内容
        System.out.println("Deque as Queue (FIFO): " + deque); // 输出: [A, B, C]

        // 取出队列头部元素
        String firstElement = deque.removeFirst(); // 移除并返回队列的头部
        System.out.println("Removed first element: " + firstElement); // 输出: A
        System.out.println("Deque after removeFirst: " + deque); // 输出: [B, C]

        // 作为栈使用 (LIFO)
        deque.push("X"); // 插入元素到栈顶
        deque.push("Y");
        deque.push("Z");

        // 输出栈的内容
        System.out.println("Deque as Stack (LIFO): " + deque); // 输出: [Z, Y, X, B, C]

        // 查看栈顶元素
        String topElement = deque.peek(); // 查看栈顶的元素
        System.out.println("Top element: " + topElement); // 输出: Z

        // 弹出栈顶元素
        String poppedElement = deque.pop(); // 移除并返回栈顶的元素
        System.out.println("Popped element: " + poppedElement); // 输出: Z
        System.out.println("Deque after pop: " + deque); // 输出: [Y, X, B, C]

        // 其他操作
        String lastElement = deque.removeLast(); // 移除并返回队尾元素
        System.out.println("Removed last element: " + lastElement); // 输出: C
        System.out.println("Deque after removeLast: " + deque); // 输出: [Y, X, B]
    }
}

// 虽然 Stack 类是 Java 提供的，但它是同步的，性能并不总是最佳。
// 在现代 Java 中，推荐使用 Deque（双端队列）接口及其实现，如 ArrayDeque，它提供了更加灵活和高效的栈操作方法。
