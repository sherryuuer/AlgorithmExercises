public class UnicodeToUTF8 {
    public static void main(String[] args) {
        int[] bytes = encode(0x3042);
        for (int _byte : bytes) {
            System.out.println(Integer.toBinaryString(_byte)); // １０進数を２進数に変換して表示
        }
    }

    private static int[] encode(int codePoint) {
        int[] utf8Bytes = { 224, 128, 128 };
        int cp = codePoint;
        int i;
        for (i = utf8Bytes.length - 1; i >= 0; i--) {
            utf8Bytes[i] = utf8Bytes[i] + (cp % 64);
            cp = cp / 64;
        }
        return utf8Bytes;
    }
}
