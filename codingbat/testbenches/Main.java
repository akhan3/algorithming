public class Main {
    public static void main(String[] args) {
        System.out.println("This will be printed");
        // strCopies("catcowcat", "cat", 2);
        // strCopies("catcowcat", "cow", 2);
        // strCopies("catcowcat", "cow", 1);
        // strCopies("iiijjj", "i", 3);
        // strCopies("iiijjj", "i", 4);
        // strCopies("iiijjj", "ii", 2);
        // strCopies("iiijjj", "ii", 3);
        // strCopies("iiijjj", "x", 3);
        strCopies("iiijjj", "x", 0);
        // strCopies("iiiiij", "iii", 3);
        // strCopies("iiiiij", "iii", 4);
        // strCopies("ijiiiiij", "iiii", 2);
        // strCopies("ijiiiiij", "iiii", 3);
        // strCopies("dogcatdogcat", "dog", 2);


    }




    public static boolean strCopies(String str, String sub, int n) {
        int count = 0;
        boolean a = strCopies(str, sub, n, count);
        System.out.println("a = " + a);
        return a;
    }

    public static boolean strCopies(String str, String sub, int n, int count) {
        if (n == 0)
            return true;
        else if (str.isEmpty())
            return false;
        else if (str.indexOf(sub) == 0)
            if (++count >= n)
                return true;
            else
                return strCopies(str.substring(1), sub, n, count);
        else
            return strCopies(str.substring(1), sub, n, count);
    }

}

