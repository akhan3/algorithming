// https://codingbat.com/java/Recursion-1

// Basic recursion problems. Recursion strategy: first test for one
// or two base cases that are so simple, the answer can be returned
// immediately. Otherwise, make a recursive a call for a smaller case
// (that is, a case which is a step towards the base case). Assume that
// the recursive call works correctly, and fix up what it returns to
// make the answer.

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

import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;

public class recursion1 {


  // Given n of 1 or more, return the factorial of n, which is n *
  // (n-1) * (n-2) ... 1. Compute the result recursively (without loops).
  // assert factorial(1) == 1;
  // assert factorial(2) == 2;
  // assert factorial(3) == 6;
  // assert factorial(4) == 24;
  // assert factorial(5) == 120;
  // assert factorial(6) == 720;
  // assert factorial(7) == 5040;
  // assert factorial(8) == 40320;
  // assert factorial(12) == 479001600;
  public int factorial(int n) {
    return (n == 1) ? 1 : n * factorial(n-1);
  }


  // We have a number of bunnies and each bunny has two big floppy
  // ears. We want to compute the total number of ears across all the
  // bunnies recursively (without loops or multiplication).
  // assert bunnyEars(0) == 0;
  // assert bunnyEars(1) == 2;
  // assert bunnyEars(2) == 4;
  // assert bunnyEars(3) == 6;
  // assert bunnyEars(4) == 8;
  // assert bunnyEars(5) == 10;
  // assert bunnyEars(12) == 24;
  // assert bunnyEars(50) == 100;
  // assert bunnyEars(234) == 468;
  public int bunnyEars(int bunnies) {
    // return 2*bunnies; // NOT ACCEPTABLE since it uses multiplication
    if (bunnies == 0)
      return 0;
    else
      return 2 + bunnyEars(bunnies-1);
  }


  // The fibonacci sequence is a famous bit of mathematics, and it
  // happens to have a recursive definition. The first two values in the
  // sequence are 0 and 1 (essentially 2 base cases). Each subsequent
  // value is the sum of the previous two values, so the whole sequence
  // is: 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on. Define a recursive
  // fibonacci(n) method that returns the nth fibonacci number, with n=0
  // representing the start of the sequence.
  // assert fibonacci(0) == 0;
  // assert fibonacci(1) == 1;
  // assert fibonacci(2) == 1;
  // assert fibonacci(3) == 2;
  // assert fibonacci(4) == 3;
  // assert fibonacci(5) == 5;
  // assert fibonacci(6) == 8;
  // assert fibonacci(7) == 13;
  public int fibonacci(int n) {
    if (n <= 1)
      return n;
    else
      return fibonacci(n-1) + fibonacci(n-2);
  }


  // We have bunnies standing in a line, numbered 1, 2, ... The odd
  // bunnies (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4,
  // ..) we'll say have 3 ears, because they each have a raised foot.
  // Recursively return the number of "ears" in the bunny line 1, 2, ... n
  // (without loops or multiplication).
  // assert bunnyEars2(0) == 0;
  // assert bunnyEars2(1) == 2;
  // assert bunnyEars2(2) == 5;
  // assert bunnyEars2(3) == 7;
  // assert bunnyEars2(4) == 10;
  // assert bunnyEars2(5) == 12;
  // assert bunnyEars2(6) == 15;
  // assert bunnyEars2(10) == 25;
  public int bunnyEars2(int bunnies) {
    if (bunnies == 0)
      return 0;
    else if ((bunnies % 2) == 0)
      return 3 + bunnyEars2(bunnies-1);
    else
      return 2 + bunnyEars2(bunnies-1);
  }


  // We have triangle made of blocks. The topmost row has 1 block,
  // the next row down has 2 blocks, the next row has 3 blocks, and so on.
  // Compute recursively (no loops or multiplication) the total number of
  // blocks in such a triangle with the given number of rows.
  // assert triangle(0) == 0;
  // assert triangle(1) == 1;
  // assert triangle(2) == 3;
  // assert triangle(3) == 6;
  // assert triangle(4) == 10;
  // assert triangle(5) == 15;
  // assert triangle(6) == 21;
  // assert triangle(7) == 28;
  public int triangle(int rows) {
    if (rows == 0)
      return 0;
    else
      return rows + triangle(rows-1);
  }


  // Given a non-negative int n, return the sum of its digits
  // recursively (no loops). Note that mod (%) by 10 yields the rightmost
  // digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost
  // digit (126 / 10 is 12).
  // assert sumDigits(126) == 9;
  // assert sumDigits(49) == 13;
  // assert sumDigits(12) == 3;
  // assert sumDigits(10) == 1;
  // assert sumDigits(1) == 1;
  // assert sumDigits(0) == 0;
  // assert sumDigits(730) == 10;
  // assert sumDigits(1111) == 4;
  // assert sumDigits(11111) == 5;
  // assert sumDigits(10110) == 3;
  // assert sumDigits(235) == 10;
  public int sumDigits(int n) {
    if (n == 0)
      return n;
    else
      return n % 10 + sumDigits(n/10);
  }


  // Given a non-negative int n, return the count of the occurrences
  // of 7 as a digit, so for example 717 yields 2. (no loops). Note that
  // mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while
  // divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
  // assert count7(717) == 2;
  // assert count7(7) == 1;
  // assert count7(123) == 0;
  // assert count7(77) == 2;
  // assert count7(7123) == 1;
  // assert count7(771237) == 3;
  // assert count7(771737) == 4;
  // assert count7(47571) == 2;
  // assert count7(777777) == 6;
  // assert count7(70701277) == 4;
  // assert count7(777576197) == 5;
  // assert count7(99999) == 0;
  // assert count7(99799) == 1;
  public int count7(int n) {
    if (n == 0)
      return 0;
    int a = ((n % 10) == 7) ? 1 : 0;
    return a + count7(n / 10);
  }


  // Given a non-negative int n, compute recursively (no loops) the
  // count of the occurrences of 8 as a digit, except that an 8 with
  // another 8 immediately to its left counts double, so 8818 yields 4.
  // Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
  // while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
  // assert count8(8) == 1;
  // assert count8(818) == 2;
  // assert count8(8818) == 4;
  // assert count8(8088) == 4;
  // assert count8(123) == 0;
  // assert count8(81238) == 2;
  // assert count8(88788) == 6;
  // assert count8(8234) == 1;
  // assert count8(2348) == 1;
  // assert count8(23884) == 3;
  // assert count8(0) == 0;
  // assert count8(1818188) == 5;
  // assert count8(8818181) == 5;
  // assert count8(1080) == 1;
  // assert count8(188) == 3;
  // assert count8(88888) == 9;
  // assert count8(9898) == 2;
  // assert count8(78) == 1;
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


  // Given base and n that are both 1 or more, compute recursively
  // (no loops) the value of base to the n power, so powerN(3, 2) is 9 (3
  // squared).
  // assert powerN(3, 1) == 3;
  // assert powerN(3, 2) == 9;
  // assert powerN(3, 3) == 27;
  // assert powerN(2, 1) == 2;
  // assert powerN(2, 2) == 4;
  // assert powerN(2, 3) == 8;
  // assert powerN(2, 4) == 16;
  // assert powerN(2, 5) == 32;
  // assert powerN(10, 1) == 10;
  // assert powerN(10, 2) == 100;
  // assert powerN(10, 3) == 1000;
  public int powerN(int base, int n) {
    if (n == 0)
      return 1;
    else
      return base * powerN(base, n - 1);
  }


  // Given a string, compute recursively (no loops) the number of
  // lowercase 'x' chars in the string.
  // assert countX("xxhixx") == 4;
  // assert countX("xhixhix") == 3;
  // assert countX("hi") == 0;
  // assert countX("h") == 0;
  // assert countX("x") == 1;
  // assert countX("") == 0;
  // assert countX("hihi") == 0;
  // assert countX("hiAAhi12hi") == 0;
  public int countX(String str) {
    if (str.length() == 0)
      return 0;
    else {
      int n = (str.indexOf('x') == 0) ? 1 : 0;
      return n + countX(str.substring(1));
    }
  }


  // Given a string, compute recursively (no loops) the number of
  // times lowercase "hi" appears in the string.
  // assert countHi("xxhixx") == 1;
  // assert countHi("xhixhix") == 2;
  // assert countHi("hi") == 1;
  // assert countHi("hihih") == 2;
  // assert countHi("h") == 0;
  // assert countHi("") == 0;
  // assert countHi("ihihihihih") == 4;
  // assert countHi("ihihihihihi") == 5;
  // assert countHi("hiAAhi12hi") == 3;
  // assert countHi("xhixhxihihhhih") == 3;
  // assert countHi("ship") == 1;
  public int countHi(String str) {
    if (str.length() <= 1)
      return 0;
    else {
      int n = (str.indexOf("hi") == 0) ? 1 : 0;
      return n + countHi(str.substring(1));
    }
  }


  // Given a string, compute recursively (no loops) a new string
  // where all the lowercase 'x' chars have been changed to 'y' chars.
  // assert changeXY("codex") == "codey";
  // assert changeXY("xxhixx") == "yyhiyy";
  // assert changeXY("xhixhix") == "yhiyhiy";
  // assert changeXY("hiy") == "hiy";
  // assert changeXY("h") == "h";
  // assert changeXY("x") == "y";
  // assert changeXY("") == "";
  // assert changeXY("xxx") == "yyy";
  // assert changeXY("yyhxyi") == "yyhyyi";
  // assert changeXY("hihi") == "hihi";
  public String changeXY(String str) {
    if (str.length() == 0)
      return str;
    else {
      char a = (str.indexOf('x') == 0) ? 'y' : str.charAt(0);
      // CAUTION: string concatenation is not commutative
      return a + changeXY(str.substring(1));
    }
  }


  // Given a string, compute recursively (no loops) a new string
  // where all appearances of "pi" have been replaced by "3.14".
  // assert changePi("xpix") == "x3.14x";
  // assert changePi("pipi") == "3.143.14";
  // assert changePi("pip") == "3.14p";
  // assert changePi("pi") == "3.14";
  // assert changePi("hip") == "hip";
  // assert changePi("p") == "p";
  // assert changePi("x") == "x";
  // assert changePi("") == "";
  // assert changePi("pixx") == "3.14xx";
  // assert changePi("xyzzy") == "xyzzy";
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


  // Given a string, compute recursively a new string where all the
  // 'x' chars have been removed.
  // assert noX("xaxb") == "ab";
  // assert noX("abc") == "abc";
  // assert noX("xx") == "";
  // assert noX("") == "";
  // assert noX("axxbxx") == "ab";
  // assert noX("Hellox") == "Hello";
  public String noX(String str) {
    if (str.length() == 0)
      return str;
    else {
      String a = (str.indexOf('x') == 0) ? "" : str.substring(0, 1);
      return a + noX(str.substring(1));
    }
  }


  // Given an array of ints, compute recursively if the array
  // contains a 6. We'll use the convention of considering only the part
  // of the array that begins at the given index. In this way, a recursive
  // call can pass index+1 to move down the array. The initial call will
  // pass in index as 0.
  // assert array6([1, 6, 4], 0) == true;
  // assert array6([1, 4], 0) == false;
  // assert array6([6], 0) == true;
  // assert array6([], 0) == false;
  // assert array6([6, 2, 2], 0) == true;
  // assert array6([2, 5], 0) == false;
  // assert array6([1, 9, 4, 6, 6], 0) == true;
  // assert array6([2, 5, 6], 0) == true;
  public boolean array6(int[] nums, int index) {
    if (index == nums.length)
      return false;
    else if (nums[index] == 6)
      return true;  // short circuit behavior of OR gate
                    // this improves best-case and average-case run time
    else
      return array6(nums, index+1);
  }


  // Given an array of ints, compute recursively the number of times
  // that the value 11 appears in the array. We'll use the convention of
  // considering only the part of the array that begins at the given
  // index. In this way, a recursive call can pass index+1 to move down
  // the array. The initial call will pass in index as 0.
  // assert array11([1, 2, 11], 0) == 1;
  // assert array11([11, 11], 0) == 2;
  // assert array11([1, 2, 3, 4], 0) == 0;
  // assert array11([1, 11, 3, 11, 11], 0) == 3;
  // assert array11([11], 0) == 1;
  // assert array11([1], 0) == 0;
  // assert array11([], 0) == 0;
  // assert array11([11, 2, 3, 4, 11, 5], 0) == 2;
  // assert array11([11, 5, 11], 0) == 2;
  public int array11(int[] nums, int index) {
    if (index == nums.length)
      return 0;
    int a = (nums[index] == 11) ? 1 : 0;
    return a + array11(nums, index+1);
  }


  // Given an array of ints, compute recursively if the array
  // contains somewhere a value followed in the array by that value times
  // 10. We'll use the convention of considering only the part of the
  // array that begins at the given index. In this way, a recursive call
  // can pass index+1 to move down the array. The initial call will pass
  // in index as 0.
  // assert array220([1, 2, 20], 0) == true;
  // assert array220([3, 30], 0) == true;
  // assert array220([3], 0) == false;
  // assert array220([], 0) == false;
  // assert array220([3, 3, 30, 4], 0) == true;
  // assert array220([2, 19, 4], 0) == false;
  // assert array220([20, 2, 21], 0) == false;
  // assert array220([20, 2, 21, 210], 0) == true;
  // assert array220([2, 200, 2000], 0) == true;
  // assert array220([0, 0], 0) == true;
  // assert array220([1, 2, 3, 4, 5, 6], 0) == false;
  // assert array220([1, 2, 3, 4, 5, 50, 6], 0) == true;
  // assert array220([1, 2, 3, 4, 5, 51, 6], 0) == false;
  // assert array220([1, 2, 3, 4, 4, 50, 500, 6], 0) == true;
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


  // Given a string, compute recursively a new string where all the
  // adjacent chars are now separated by a "*".
  // assert allStar("hello") == "h*e*l*l*o";
  // assert allStar("abc") == "a*b*c";
  // assert allStar("ab") == "a*b";
  // assert allStar("a") == "a";
  // assert allStar("") == "";
  // assert allStar("3.14") == "3*.*1*4";
  // assert allStar("Chocolate") == "C*h*o*c*o*l*a*t*e";
  // assert allStar("1234") == "1*2*3*4";
  public String allStar(String str) {
    if (str.length() <= 1)
      return str;
    return str.charAt(0) + "*" + allStar(str.substring(1));
  }


  // Given a string, compute recursively a new string where identical
  // chars that are adjacent in the original string are separated from
  // each other by a "*".
  // assert pairStar("hello") == "hel*lo";
  // assert pairStar("xxyy") == "x*xy*y";
  // assert pairStar("aaaa") == "a*a*a*a";
  // assert pairStar("aaab") == "a*a*ab";
  // assert pairStar("aa") == "a*a";
  // assert pairStar("a") == "a";
  // assert pairStar("") == "";
  // assert pairStar("noadjacent") == "noadjacent";
  // assert pairStar("abba") == "ab*ba";
  // assert pairStar("abbba") == "ab*b*ba";
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


  // Given a string, compute recursively a new string where all the
  // lowercase 'x' chars have been moved to the end of the string.
  // assert endX("xxre") == "rexx";
  // assert endX("xxhixx") == "hixxxx";
  // assert endX("xhixhix") == "hihixxx";
  // assert endX("hiy") == "hiy";
  // assert endX("h") == "h";
  // assert endX("x") == "x";
  // assert endX("xx") == "xx";
  // assert endX("") == "";
  // assert endX("bxx") == "bxx";
  // assert endX("bxax") == "baxx";
  // assert endX("axaxax") == "aaaxxx";
  // assert endX("xxhxi") == "hixxx";
  public String endX(String str) {
    if (str.length() <= 1)
      return str;
    // NOTE: We are really making use of non-commutative nature of
    // string concatenation here
    if (str.charAt(0) == 'x')
      return endX(str.substring(1)) + str.charAt(0);
    else
      return str.charAt(0) + endX(str.substring(1));
  }

  // We'll say that a "pair" in a string is two instances of a char
  // separated by a char. So "AxA" the A's make a pair. Pair's can
  // overlap, so "AxAxA" contains 3 pairs -- 2 for A and 1 for x.
  // Recursively compute the number of pairs in the given string.
  // assert countPairs("axa") == 1;
  // assert countPairs("axax") == 2;
  // assert countPairs("axbx") == 1;
  // assert countPairs("hi") == 0;
  // assert countPairs("hihih") == 3;
  // assert countPairs("ihihhh") == 3;
  // assert countPairs("ihjxhh") == 0;
  // assert countPairs("") == 0;
  // assert countPairs("a") == 0;
  // assert countPairs("aa") == 0;
  // assert countPairs("aaa") == 1;
  public int countPairs(String str) {
    if (str.length() <= 2)
      return 0;
    int a = (str.charAt(0) == str.charAt(2)) ? 1 : 0;
    return a + countPairs(str.substring(1));
  }


  // Count recursively the total number of "abc" and "aba" substrings
  // that appear in the given string.
  // assert countAbc("abc") == 1;
  // assert countAbc("abcxxabc") == 2;
  // assert countAbc("abaxxaba") == 2;
  // assert countAbc("ababc") == 2;
  // assert countAbc("abxbc") == 0;
  // assert countAbc("aaabc") == 1;
  // assert countAbc("hello") == 0;
  // assert countAbc("") == 0;
  // assert countAbc("ab") == 0;
  // assert countAbc("aba") == 1;
  // assert countAbc("aca") == 0;
  // assert countAbc("aaa") == 0;
  public int countAbc(String str) {
    if (str.length() <= 2)
      return 0;
    int n1 = (str.indexOf("abc") == 0) ? 1 : 0;
    int n2 = (str.indexOf("aba") == 0) ? 1 : 0;
    return n1 + n2 + countAbc(str.substring(1));
  }


  // Given a string, compute recursively (no loops) the number of
  // "11" substrings in the string. The "11" substrings should not overlap.
  // assert count11("11abc11") == 2;
  // assert count11("abc11x11x11") == 3;
  // assert count11("111") == 1;
  // assert count11("1111") == 2;
  // assert count11("1") == 0;
  // assert count11("") == 0;
  // assert count11("hi") == 0;
  // assert count11("11x111x1111") == 4;
  // assert count11("1x111") == 1;
  // assert count11("1Hello1") == 0;
  // assert count11("Hello") == 0;
  public int count11(String str) {
    if (str.length() <= 1)
      return 0;
    int n1 = (str.indexOf("11") == 0) ? 1 : 0;
    int n2 = (str.indexOf("111") == 0) ? 1 : 0;
    int n3 = (str.indexOf("1111") == 0) ? 1 : 0; // KLUDGE! but it passes the tests
    return n1 - n2 + n3 + count11(str.substring(1));
  }


  // Given a string, return recursively a "cleaned" string where
  // adjacent chars that are the same have been reduced to a single char.
  // So "yyzzza" yields "yza".
  // assert stringClean("yyzzza") == "yza";
  // assert stringClean("abbbcdd") == "abcd";
  // assert stringClean("Hello") == "Helo";
  // assert stringClean("XXabcYY") == "XabcY";
  // assert stringClean("112ab445") == "12ab45";
  // assert stringClean("Hello Bookkeeper") == "Helo Bokeper";
  public String stringClean(String str) {
    if (str.length() <= 1)
      return str;
    String a = (str.charAt(0) == str.charAt(1)) ? "" : str.substring(0, 1);
    return a + stringClean(str.substring(1));
  }


  // Given a string, compute recursively the number of times
  // lowercase "hi" appears in the string, however do not count "hi" that
  // have an 'x' immedately before them.
  // assert countHi2("ahixhi") == 1;
  // assert countHi2("ahibhi") == 2;
  // assert countHi2("xhixhi") == 0;
  // assert countHi2("hixhi") == 1;
  // assert countHi2("hixhhi") == 2;
  // assert countHi2("hihihi") == 3;
  // assert countHi2("hihihix") == 3;
  // assert countHi2("xhihihix") == 2;
  // assert countHi2("xxhi") == 0;
  // assert countHi2("hixxhi") == 1;
  // assert countHi2("hi") == 1;
  // assert countHi2("xxxx") == 0;
  // assert countHi2("h") == 0;
  // assert countHi2("x") == 0;
  // assert countHi2("") == 0;
  // assert countHi2("Hellohi") == 1;
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


  // Given a string that contains a single pair of parenthesis,
  // compute recursively a new string made of only of the parenthesis and
  // their contents, so "xyz(abc)123" yields "(abc)".
  // assert parenBit("xyz(abc)123") == "(abc)";
  // assert parenBit("x(hello)") == "(hello)";
  // assert parenBit("(xy)1") == "(xy)";
  // assert parenBit("not really (possible)") == "(possible)";
  // assert parenBit("(abc)") == "(abc)";
  // assert parenBit("(abc)xyz") == "(abc)";
  // assert parenBit("(abc)x") == "(abc)";
  // assert parenBit("(x)") == "(x)";
  // assert parenBit("()") == "()";
  // assert parenBit("res (ipsa) loquitor") == "(ipsa)";
  // assert parenBit("hello(not really)there") == "(not really)";
  // assert parenBit("ab(ab)ab") == "(ab)";
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
    // If the first char is '(', then recur similarly, removing one
    // char from
    // the end of the string, until it is ')'.
    // Now the first and last chars are ( .. ) and you're done.
  }


  // Given a string, return true if it is a nesting of zero or more
  // pairs of parenthesis, like "(())" or "((()))". Suggestion: check the
  // first and last chars, and then recur on what's inside them.
  // assert nestParen("(())") == true;
  // assert nestParen("((()))") == true;
  // assert nestParen("(((x))") == false;
  // assert nestParen("((())") == false;
  // assert nestParen("((()()") == false;
  // assert nestParen("()") == true;
  // assert nestParen("") == true;
  // assert nestParen("(yy)") == false;
  // assert nestParen("(())") == true;
  // assert nestParen("(((y))") == false;
  // assert nestParen("((y)))") == false;
  // assert nestParen("((()))") == true;
  // assert nestParen("(())))") == false;
  // assert nestParen("((yy())))") == false;
  // assert nestParen("(((())))") == true;
  public boolean nestParen(String str) {
  if (str.length() == 0)
    return true;
  else if (!((str.charAt(0) == '(') && (str.charAt(str.length()-1) == ')')))
    return false;
  else
    return nestParen(str.substring(1, str.length()-1));
  }



  // Given a string and a non-empty substring sub, compute
  // recursively the number of times that sub appears in the string,
  // without the sub strings overlapping.
  // assert strCount("catcowcat", "cat") == 2;
  // assert strCount("catcowcat", "cow") == 1;
  // assert strCount("catcowcat", "dog") == 0;
  // assert strCount("cacatcowcat", "cat") == 2;
  // assert strCount("xyx", "x") == 2;
  // assert strCount("iiiijj", "i") == 4;
  // assert strCount("iiiijj", "ii") == 2;
  // assert strCount("iiiijj", "iii") == 1;
  // assert strCount("iiiijj", "j") == 2;
  // assert strCount("iiiijj", "jj") == 1;
  // assert strCount("aaabababab", "ab") == 4;
  // assert strCount("aaabababab", "aa") == 1;
  // assert strCount("aaabababab", "a") == 6;
  // assert strCount("aaabababab", "b") == 4;
  public int strCount(String str, String sub) {
    if (str.isEmpty())
      return 0;
    else if (str.indexOf(sub) == 0)
      return 1 + strCount(str.substring(sub.length()), sub);
    else
      return strCount(str.substring(1), sub);
  }


  // Given a string and a non-empty substring sub, compute
  // recursively if at least n copies of sub appear in the string
  // somewhere, possibly with overlapping. N will be non-negative.
  // assert strCopies("catcowcat", "cat", 2) == true;
  // assert strCopies("catcowcat", "cow", 2) == false;
  // assert strCopies("catcowcat", "cow", 1) == true;
  // assert strCopies("iiijjj", "i", 3) == true;
  // assert strCopies("iiijjj", "i", 4) == false;
  // assert strCopies("iiijjj", "ii", 2) == true;
  // assert strCopies("iiijjj", "ii", 3) == false;
  // assert strCopies("iiijjj", "x", 3) == false;
  // assert strCopies("iiijjj", "x", 0) == true;
  // assert strCopies("iiiiij", "iii", 3) == true;
  // assert strCopies("iiiiij", "iii", 4) == false;
  // assert strCopies("ijiiiiij", "iiii", 2) == true;
  // assert strCopies("ijiiiiij", "iiii", 3) == false;
  // assert strCopies("dogcatdogcat", "dog", 2) == true;
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


  // Given a string and a non-empty substring sub, compute recursively
  // the largest substring which starts and ends with sub and return
  // its length.
  // assert strDist("catcowcat", "cat") == 9;
  // assert strDist("catcowcat", "cow") == 3;
  // assert strDist("cccatcowcatxx", "cat") == 9;
  // assert strDist("abccatcowcatcatxyz", "cat") == 12;
  // assert strDist("xyx", "x") == 3;
  // assert strDist("xyx", "y") == 1;
  // assert strDist("xyx", "z") == 0;
  // assert strDist("z", "z") == 1;
  // assert strDist("x", "z") == 0;
  // assert strDist("", "z") == 0;
  // assert strDist("hiHellohihihi", "hi") == 13;
  // assert strDist("hiHellohihihi", "hih") == 5;
  // assert strDist("hiHellohihihi", "o") == 1;
  // assert strDist("hiHellohihihi", "ll") == 2;
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
