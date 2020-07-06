// https://codingbat.com/java/Recursion-1

// Basic recursion problems. Recursion strategy: first test for one or two base cases that are so simple, the answer can be returned immediately. Otherwise, make a recursive a call for a smaller case (that is, a case which is a step towards the base case). Assume that the recursive call works correctly, and fix up what it returns to make the answer.

//  factorial       bunnyEars       fibonacci
//  bunnyEars2      triangle        sumDigits
//  count7          count8          powerN
//  countX          countHi         changeXY
//  changePi        noX             array6
//  array11         array220        allStar
//  pairStar        endX            countPairs
//  countAbc        count11         stringClean
//  countHi2        parenBit        nestParen
//  strCount        strCopies       strDist

public class recursion1 {


  // Given n of 1 or more, return the factorial of n, which is n * (n-1) * (n-2) ... 1. Compute the result recursively (without loops).
  // factorial(1) → 1
  // factorial(2) → 2
  // factorial(3) → 6
  public int factorial(int n) {
    return (n == 1) ? 1 : n * factorial(n-1);
  }


  // We have a number of bunnies and each bunny has two big floppy ears. We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).
  // bunnyEars(0) → 0
  // bunnyEars(1) → 2
  // bunnyEars(2) → 4
  public int bunnyEars(int bunnies) {
    // return 2*bunnies; // NOT ACCEPTABLE since it uses multiplication
    if (bunnies == 0)
      return 0;
    else
      return 2 + bunnyEars(bunnies-1);
  }


  // The fibonacci sequence is a famous bit of mathematics, and it happens to have a recursive definition. The first two values in the sequence are 0 and 1 (essentially 2 base cases). Each subsequent value is the sum of the previous two values, so the whole sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on. Define a recursive fibonacci(n) method that returns the nth fibonacci number, with n=0 representing the start of the sequence.
  // fibonacci(0) → 0
  // fibonacci(1) → 1
  // fibonacci(2) → 1
  public int fibonacci(int n) {
    if (n <= 1)
      return n;
    else
      return fibonacci(n-1) + fibonacci(n-2);
  }


  // We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say have 3 ears, because they each have a raised foot. Recursively return the number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).
  // bunnyEars2(0) → 0
  // bunnyEars2(1) → 2
  // bunnyEars2(2) → 5
  public int bunnyEars2(int bunnies) {
    if (bunnies == 0)
      return 0;
    else if ((bunnies % 2) == 0)
      return 3 + bunnyEars2(bunnies-1);
    else
      return 2 + bunnyEars2(bunnies-1);
  }


  // We have triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks, the next row has 3 blocks, and so on. Compute recursively (no loops or multiplication) the total number of blocks in such a triangle with the given number of rows.
  // triangle(0) → 0
  // triangle(1) → 1
  // triangle(2) → 3
  public int triangle(int rows) {
    if (rows == 0)
      return 0;
    else
      return rows + triangle(rows-1);
  }


  // Given a non-negative int n, return the sum of its digits recursively (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
  // sumDigits(126) → 9
  // sumDigits(49) → 13
  // sumDigits(12) → 3
  public int sumDigits(int n) {
    if (n == 0)
      return n;
    else
      return n % 10 + sumDigits(n/10);
  }


  // Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
  // count7(717) → 2
  // count7(7) → 1
  // count7(123) → 0
  public int count7(int n) {
    if (n == 0)
      return 0;
    int a = ((n % 10) == 7) ? 1 : 0;
    return a + count7(n / 10);
  }


  // Given a non-negative int n, compute recursively (no loops) the count of the occurrences of 8 as a digit, except that an 8 with another 8 immediately to its left counts double, so 8818 yields 4. Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
  // count8(8) → 1
  // count8(818) → 2
  // count8(8818) → 4
  public int count8(int n) {
    if (n == 0)
      return 0;
    int a;
    if ((n % 100) == 88)
      a = 2;
    else if ((n % 10) == 8)
      a = 1;
    else
      a = 0;
    return a + count8(n / 10);
  }


  // Given base and n that are both 1 or more, compute recursively (no loops) the value of base to the n power, so powerN(3, 2) is 9 (3 squared).
  // powerN(3, 1) → 3
  // powerN(3, 2) → 9
  // powerN(3, 3) → 27
  public int powerN(int base, int n) {
    if (n == 0)
      return 1;
    else
      return base * powerN(base, n - 1);
  }


  // Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.
  // countX("xxhixx") → 4
  // countX("xhixhix") → 3
  // countX("hi") → 0
  public int countX(String str) {
    if (str.length() == 0)
      return 0;
    else {
      int n = (str.indexOf('x') == 0) ? 1 : 0;
      return n + countX(str.substring(1));
    }
  }


  // Given a string, compute recursively (no loops) the number of times lowercase "hi" appears in the string.
  // countHi("xxhixx") → 1
  // countHi("xhixhix") → 2
  // countHi("hi") → 1
  public int countHi(String str) {
    if (str.length() <= 1)
      return 0;
    else {
      int n = (str.indexOf("hi") == 0) ? 1 : 0;
      return n + countHi(str.substring(1));
    }
  }


  // Given a string, compute recursively (no loops) a new string where all the lowercase 'x' chars have been changed to 'y' chars.
  // changeXY("codex") → "codey"
  // changeXY("xxhixx") → "yyhiyy"
  // changeXY("xhixhix") → "yhiyhiy"
  public String changeXY(String str) {
    if (str.length() == 0)
      return str;
    else {
      char a = (str.indexOf('x') == 0) ? 'y' : str.charAt(0);
      // CAUTION: string concatenation is not commutative
      return a + changeXY(str.substring(1));
    }
  }


  // Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by "3.14".
  // changePi("xpix") → "x3.14x"
  // changePi("pipi") → "3.143.14"
  // changePi("pip") → "3.14p"
  public String changePi(String str) {
    if (str.length() <= 1)
      return str;
    else {
      boolean pi_found = str.indexOf("pi") == 0;
      String str2;
      int delta;
      if (pi_found) {
        str2 = "3.14";
        delta = 2;
      }
      else {
        str2 = str.substring(0, 1);
        delta = 1;
      }
      // CAUTION: string concatenation is not commutative
      return str2 + changePi(str.substring(delta));
    }
  }


  // Given a string, compute recursively a new string where all the 'x' chars have been removed.
  // noX("xaxb") → "ab"
  // noX("abc") → "abc"
  // noX("xx") → ""
  public String noX(String str) {
    if (str.length() == 0)
      return str;
    else {
      String a = (str.indexOf('x') == 0) ? "" : str.substring(0, 1);
      return a + noX(str.substring(1));
    }
  }


  // Given an array of ints, compute recursively if the array contains a 6. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.
  // array6([1, 6, 4], 0) → true
  // array6([1, 4], 0) → false
  // array6([6], 0) → true
  public boolean array6(int[] nums, int index) {
    if (index == nums.length)
      return false;
    else if (nums[index] == 6)
      return true;  // short circuit behavior of OR gate
                    // this improves best-case and average-case run time
    else
      return array6(nums, index+1);
  }


  // Given an array of ints, compute recursively the number of times that the value 11 appears in the array. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.
  // array11([1, 2, 11], 0) → 1
  // array11([11, 11], 0) → 2
  // array11([1, 2, 3, 4], 0) → 0
  public int array11(int[] nums, int index) {
    if (index == nums.length)
      return 0;
    int a = (nums[index] == 11) ? 1 : 0;
    return a + array11(nums, index+1);
  }


  // Given an array of ints, compute recursively if the array contains somewhere a value followed in the array by that value times 10. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.
  // array220([1, 2, 20], 0) → true
  // array220([3, 30], 0) → true
  // array220([3], 0) → false
  public boolean array220(int[] nums, int index) {
    if (index >= nums.length - 1)
      return false;
    else if (nums[index] * 10 == nums[index+1])
      return true;  // short circuit behavior of OR gate
                    // this improves best-case and average-case run time
    else
      return array220(nums, index+1);
  }
  // Another solution challenged by Umair
  public boolean array220_(int[] nums, int index) {
    if (nums.length <= 1)
      return false;
    else if (nums[0] * 10 == nums[1])
      return true;
    else {
      nums = Arrays.copyOfRange(nums, 1, nums.length);
      return array220(nums, -999);
    }
  }
  // Umair's solution based on associative arrays
  public boolean array220__(int[] nums, int index) {
    return array220___(nums, index, new HashMap<Integer, Integer>());
  }
  boolean array220___(int[] nums, int index, Map<Integer, Integer> map) {
    if(index >= nums.length)
      return false;
    if(map.get(nums[index]) != null) {
      return true;
    }
    else {
      map.put(nums[index]*10, nums[index]);
      return array220___(nums, index+1, map);
    }
  }


  // Given a string, compute recursively a new string where all the adjacent chars are now separated by a "*".
  // allStar("hello") → "h*e*l*l*o"
  // allStar("abc") → "a*b*c"
  // allStar("ab") → "a*b"
  public String allStar(String str) {
    if (str.length() <= 1)
      return str;
    return str.charAt(0) + "*" + allStar(str.substring(1));
  }


  // Given a string, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
  // pairStar("hello") → "hel*lo"
  // pairStar("xxyy") → "x*xy*y"
  // pairStar("aaaa") → "a*a*a*a"
  public String pairStar(String str) {
    if (str.length() <= 1)
      return str;
    String a;
    if (str.charAt(0) == str.charAt(1))
      a = str.charAt(0) + "*";
    else
      a = str.substring(0, 1);
    return a + pairStar(str.substring(1));

  }


  // Given a string, compute recursively a new string where all the lowercase 'x' chars have been moved to the end of the string.
  // endX("xxre") → "rexx"
  // endX("xxhixx") → "hixxxx"
  // endX("xhixhix") → "hihixxx"
  public String endX(String str) {
    if (str.length() <= 1)
      return str;
    // NOTE: We are really making use of non-commutative nature of string concatenation here
    if (str.charAt(0) == 'x')
      return endX(str.substring(1)) + str.charAt(0);
    else
      return str.charAt(0) + endX(str.substring(1));
  }

  // We'll say that a "pair" in a string is two instances of a char separated by a char. So "AxA" the A's make a pair. Pair's can overlap, so "AxAxA" contains 3 pairs -- 2 for A and 1 for x. Recursively compute the number of pairs in the given string.
  // countPairs("axa") → 1
  // countPairs("axax") → 2
  // countPairs("axbx") → 1
  public int countPairs(String str) {
    if (str.length() <= 2)
      return 0;
    int a = (str.charAt(0) == str.charAt(2)) ? 1 : 0;
    return a + countPairs(str.substring(1));
  }


  // Count recursively the total number of "abc" and "aba" substrings that appear in the given string.
  // countAbc("abc") → 1
  // countAbc("abcxxabc") → 2
  // countAbc("abaxxaba") → 2
  public int countAbc(String str) {
    if (str.length() <= 2)
      return 0;
    int n1 = (str.indexOf("abc") == 0) ? 1 : 0;
    int n2 = (str.indexOf("aba") == 0) ? 1 : 0;
    return n1 + n2 + countAbc(str.substring(1));
  }


  // Given a string, compute recursively (no loops) the number of "11" substrings in the string. The "11" substrings should not overlap.
  // count11("11abc11") → 2
  // count11("abc11x11x11") → 3
  // count11("111") → 1
  public int count11(String str) {
    if (str.length() <= 1)
      return 0;
    int n1 = (str.indexOf("11") == 0) ? 1 : 0;
    int n2 = (str.indexOf("111") == 0) ? 1 : 0;
    int n3 = (str.indexOf("1111") == 0) ? 1 : 0; // weird but it passes the tests
    return n1 - n2 + n3 + count11(str.substring(1));
  }


  // Given a string, return recursively a "cleaned" string where adjacent chars that are the same have been reduced to a single char. So "yyzzza" yields "yza".
  // stringClean("yyzzza") → "yza"
  // stringClean("abbbcdd") → "abcd"
  // stringClean("Hello") → "Helo"
  public String stringClean(String str) {
    if (str.length() <= 1)
      return str;
    String a = (str.charAt(0) == str.charAt(1)) ? "" : str.substring(0, 1);
    return a + stringClean(str.substring(1));
  }


  // Given a string, compute recursively the number of times lowercase "hi" appears in the string, however do not count "hi" that have an 'x' immedately before them.
  // countHi2("ahixhi") → 1
  // countHi2("ahibhi") → 2
  // countHi2("xhixhi") → 0
  public int countHi2(String str) {
    if (str.length() <= 1)
      return 0;
    int n, delta;
    if (str.indexOf("xhi") == 0) {
      n = 0;
      delta = 3;
    }
    else if (str.indexOf("hi") == 0) {
      n = 1;
      delta = 2;
    }
    else {
      n = 0;
      delta = 1;
    }
    return n + countHi2(str.substring(delta));
  }


  // Given a string that contains a single pair of parenthesis, compute recursively a new string made of only of the parenthesis and their contents, so "xyz(abc)123" yields "(abc)".
  // parenBit("xyz(abc)123") → "(abc)"
  // parenBit("x(hello)") → "(hello)"
  // parenBit("(xy)1") → "(xy)"
  public String parenBit(String str) {
    return parenBit(str, false);
  }
  public String parenBit(String str, boolean hot) {
    if (str.length() == 0)
      return str;
    else if (!hot && str.charAt(0) == '(') {
      hot = true;
      return str.charAt(0) + parenBit(str.substring(1), hot);
    }
    else if (hot && str.charAt(0) == ')') {
      hot = false;
      return str.charAt(0) + parenBit(str.substring(1), hot);
    }
    else if (hot)
      return str.charAt(0) + parenBit(str.substring(1), hot);
    else
      return parenBit(str.substring(1), hot);
  }
  // Codingbat official solution:
  public String _parenBit(String str) {
    if (str.charAt(0) != '(') {
      return _parenBit(str.substring(1));
    }
    if (str.charAt(str.length()-1) != ')') {
      return _parenBit(str.substring(0, str.length()-1));
    }
    return str;
    // Solution notes: this is tricky. Is the first char a '('?
    // If not, recur, removing one char from the left of the string.
    // Eventually this gets us to '(' at the start of the string.
    // If the first char is '(', then recur similarly, removing one char from
    // the end of the string, until it is ')'.
    // Now the first and last chars are ( .. ) and you're done.
  }


  // Given a string, return true if it is a nesting of zero or more pairs of parenthesis, like "(())" or "((()))". Suggestion: check the first and last chars, and then recur on what's inside them.
  // nestParen("(())") → true
  // nestParen("((()))") → true
  // nestParen("(((x))") → false
  public boolean nestParen(String str) {
  if (str.length() == 0)
    return true;
  else if (!((str.charAt(0) == '(') && (str.charAt(str.length()-1) == ')')))
    return false;
  else
    return nestParen(str.substring(1, str.length()-1));
  }



  // Given a string and a non-empty substring sub, compute recursively the number of times that sub appears in the string, without the sub strings overlapping.
  // strCount("catcowcat", "cat") → 2
  // strCount("catcowcat", "cow") → 1
  // strCount("catcowcat", "dog") → 0
  public int strCount(String str, String sub) {
    if (str.isEmpty())
      return 0;
    else if (str.indexOf(sub) == 0)
      return 1 + strCount(str.substring(sub.length()), sub);
    else
      return strCount(str.substring(1), sub);
  }


  // Given a string and a non-empty substring sub, compute recursively if at least n copies of sub appear in the string somewhere, possibly with overlapping. N will be non-negative.
  // strCopies("catcowcat", "cat", 2) → true
  // strCopies("catcowcat", "cow", 2) → false
  // strCopies("catcowcat", "cow", 1) → true
  public boolean strCopies(String str, String sub, int n) {
    int count = 0;
    return strCopies(str, sub, n, count);
  }
  public boolean strCopies(String str, String sub, int n, int count) {
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
  public boolean strCopies_(String str, String sub, int n) {
    if (n == 0)
      return true;
    else if (str.isEmpty())
      return false;
    else if (str.indexOf(sub) == 0)
      return strCopies_(str.substring(1), sub, n-1);
    else
      return strCopies_(str.substring(1), sub, n);
  }
  // Codingbat official solution:
  public boolean _strCopies(String str, String sub, int n) {
    if (n == 0) return true;
    int len = sub.length();
    if (str.length() < len) return false;

    if (str.substring(0, len).equals(sub)) {
      // Found it, so subtract 1 from n in the recursion
      return _strCopies(str.substring(1), sub, n-1);
    } else {
      return _strCopies(str.substring(1), sub, n);
    }
  }


  // Given a string and a non-empty substring sub, compute recursively the largest substring which starts and ends with sub and return its length.
  // strDist("catcowcat", "cat") → 9
  // strDist("catcowcat", "cow") → 3
  // strDist("cccatcowcatxx", "cat") → 9
  public int strDist(String str, String sub) {
    if (str.isEmpty())
      return 0;
    else if (str.indexOf(sub) != 0)                               // if not found at head
      return strDist(str.substring(1), sub);                      // trim from head and recurse
    else if (str.lastIndexOf(sub) != str.length() - sub.length()) // if not found at tail
      return strDist(str.substring(0, str.length() - 1), sub);    // trim from tail and recurse
    else                                                          // if we reach here, we must have found the solution
      return str.length();                                        // TADA!
  }


}
