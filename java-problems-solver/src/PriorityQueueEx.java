import java.util.PriorityQueue;

public class PriorityQueueEx {
    public static void main(String[] args) {
        PriorityQueue<Element> queue = new PriorityQueue<>();

        // 虽然将不同的类放在不同的文件是好的做法
        // 因为我想将Element类放在同一个问题中，所以我定义了一个内部静态的类
        queue.add(new PriorityQueueEx.Element("A", 3));
        queue.add(new PriorityQueueEx.Element("B", 2));
        queue.add(new PriorityQueueEx.Element("C", 1));

        while (!queue.isEmpty()) {
            System.out.println(queue.poll());
        }
    }

    static class Element implements Comparable<Element> {
        String letter;
        int priority;

        public Element(String letter, int priority) {
            this.letter = letter;
            this.priority = priority;
        }

        @Override
        public int compareTo(Element other) {
            return Integer.compare(this.priority, other.priority);
        }

        @Override
        public String toString() {
            return "Element{letter=" + letter + ", priority=" + priority + "}";
        }
    }
}
