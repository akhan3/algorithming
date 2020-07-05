// How to compile and run
// javac Main.java && java -ea Main

public class Main {
    public static void main(String[] args) {
        System.out.println("This will be printed");

        assert strDist("catcowcat", "cat") == 9;
        assert strDist("catcowcat", "cow") == 3;
        assert strDist("cccatcowcatxx", "cat") == 9;
        assert strDist("abccatcowcatcatxyz", "cat") == 12;
        assert strDist("xyx", "x") == 3;
        assert strDist("xyx", "y") == 1;
        assert strDist("xyx", "z") == 0;
        assert strDist("z", "z") == 1;
        assert strDist("x", "z") == 0;
        assert strDist("", "z") == 0;
        assert strDist("hiHellohihihi", "hi") == 13;
        assert strDist("hiHellohihihi", "hih") == 5;
        assert strDist("hiHellohihihi", "o") == 1;
        assert strDist("hiHellohihihi", "ll") == 2;
    }

    // Given a string and a non-empty substring sub, compute recursively the largest substring which starts and ends with sub and return its length.
    public static int strDist(String str, String sub) {
        if (str.isEmpty())
          return 0;
        else if (str.indexOf(sub) != 0)
            return strDist(str.substring(1), sub);
        else if (str.lastIndexOf(sub) != str.length() - sub.length())
            return strDist(str.substring(0, str.length() - 1), sub);
        return str.length();
    }

}

