import java.util.ArrayList;
import java.util.List;

public class DFSEx {
    public static void main(String[] args) {
        // 构造一个简单的二叉树
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);
        root.left.left.left = new TreeNode(8); // Leaf
        root.left.left.right = new TreeNode(9); // Leaf

        // 获取并打印所有叶子节点
        List<TreeNode> leaves = getLeafNodes(root);
        for (TreeNode leaf : leaves) {
            System.out.println("Leaf Node: " + leaf.value);
        }
    }

    public static List<TreeNode> getLeafNodes(TreeNode root) {
        List<TreeNode> leaves = new ArrayList<>();
        dfs(root, leaves);
        return leaves;
    }

    private static void dfs(TreeNode node, List<TreeNode> leaves) {
        if (node == null) {
            return;
        }

        // 如果是叶子节点（没有左右子节点）
        if (node.left == null && node.right == null) {
            leaves.add(node);
        }

        // 递归访问左子树
        if (node.left != null) {
            dfs(node.left, leaves);
        }

        // 递归访问右子树
        if (node.right != null) {
            dfs(node.right, leaves);
        }
    }

    static class TreeNode {
        int value;
        TreeNode left;
        TreeNode right;

        public TreeNode(int value) {
            this.value = value;
            this.left = null;
            this.right = null;
        }
    }
}
