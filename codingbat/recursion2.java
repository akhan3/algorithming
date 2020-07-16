// https://codingbat.com/java/Recursion-2

// Harder recursion problems. Currently, these are all recursive
// backtracking problems with arrays.

// groupSum         groupSum6       groupNoAdj
// groupSum5        groupSumClump   splitArray
// splitOdd10       split53

import java.util.Deque;
import java.util.ArrayDeque;
import java.lang.Integer;

public class recursion2 {


  public static void main(String[] args) {
    // int [] nums = {2,4,8};
    // boolean found = groupSum(0, nums, 10);
    // System.out.println("found: " + found);

    // for (int k=0; k<nums.length; k++)
    //   System.out.println("Hello: " + nums);
  }


  // Given an array of ints, is it possible to choose a group of some
  // of the ints, such that the group sums to the given target? This is a
  // classic backtracking recursion problem. Once you understand the
  // recursive backtracking strategy in this problem, you can use the same
  // pattern for many problems to search a space of choices. Rather than
  // looking at the whole array, our convention is to consider the part of
  // the array starting at index start and continuing to the end of the
  // array. The caller can specify the whole array simply by passing start
  // as 0. No loops are needed -- the recursive calls progress down the
  // array.
  // assert groupSum(0, [2, 4, 8], 10) == true;
  // assert groupSum(0, [2, 4, 8], 14) == true;
  // assert groupSum(0, [2, 4, 8], 9) == false;
  // assert groupSum(0, [2, 4, 8], 8) == true;
  // assert groupSum(1, [2, 4, 8], 8) == true;
  // assert groupSum(1, [2, 4, 8], 2) == false;
  // assert groupSum(0, [1], 1) == true;
  // assert groupSum(0, [9], 1) == false;
  // assert groupSum(1, [9], 0) == true;
  // assert groupSum(0, [], 0) == true;
  // assert groupSum(0, [10, 2, 2, 5], 17) == true;
  // assert groupSum(0, [10, 2, 2, 5], 15) == true;
  // assert groupSum(0, [10, 2, 2, 5], 9) == true;
  public boolean groupSum(int start, int[] nums, int target) {
    if (start == nums.length)
      return target == 0;
    target -= nums[start];
    if (groupSum(start + 1, nums, target))
      return true;
    target += nums[start];
    if (groupSum(start + 1, nums, target))
      return true;
    return false;
  }


  // Given an array of ints, is it possible to choose a group of some of the
  // ints, beginning at the start index, such that the group sums to the given
  // target? However, with the additional constraint that all 6's must be chosen.
  // (No loops needed.)
  // groupSum6(0, [5, 6, 2], 8) → true
  // groupSum6(0, [5, 6, 2], 9) → false
  // groupSum6(0, [5, 6, 2], 7) → false
  public boolean groupSum6(int start, int[] nums, int target) {
    int accum = 0;  // accumulator to hold running sum
    int rem6 = count6(start, nums);
    return groupSum6Aux(start, nums, target, accum, rem6);
  }
  public boolean groupSum6Aux(int start, int[] nums, int target, int accum, int rem6) {
    if (target == 0)
      return true;
    if (start == nums.length)
      return (rem6 == 0) && (accum == target);

    accum += nums[start];
    if (nums[start] == 6)
      rem6--;
    if (groupSum6Aux(start + 1, nums, target, accum, rem6))
      return true;

    accum -= nums[start];
    if (nums[start] == 6)
      rem6++;
    if (groupSum6Aux(start + 1, nums, target, accum, rem6))
      return true;
    return false;
  }
  public int count6(int start, int[] nums) {
    int count = 0;
    for (int k = 0; k < nums.length; k++)
      if (nums[k] == 6)
        count++;
    return count;
  }


  // Given an array of ints, is it possible to choose a group of some of the
  // ints, such that the group sums to the given target with this additional
  // constraint: If a value in the array is chosen to be in the group, the value
  // immediately following it in the array must not be chosen. (No loops needed.)
  // groupNoAdj(0, [2, 5, 10, 4], 12) → true
  // groupNoAdj(0, [2, 5, 10, 4], 14) → false
  // groupNoAdj(0, [2, 5, 10, 4], 7) → false
  // groupNoAdj(0, [2, 5, 10, 4, 2], 7) → true // only this test is fasiling
  public boolean groupNoAdj(int start, int[] nums, int target) {
      boolean adj = false;
      return groupNoAdjAux(start, nums, target, adj);
  }

  public boolean groupNoAdjAux(int start, int[] nums, int target, boolean adj) {
    if (start >= nums.length)
      return target == 0;
    if (!adj)
      target -= nums[start];
    if (groupNoAdjAux(start + 1, nums, target, true))
      return true;
    if (!adj)
      target += nums[start];
    if (groupNoAdjAux(start + 1, nums, target, false))
      return true;
    return false;
  }


  // Given an array of ints, is it possible to choose a group of some of the
  // ints, such that the group sums to the given target with these additional
  // constraints: all multiples of 5 in the array must be included in the group.
  // If the value immediately following a multiple of 5 is 1, it must not be chosen.
  // (No loops needed.)
  // groupSum5(0, [2, 5, 10, 4], 19) → true
  // groupSum5(0, [2, 5, 10, 4], 17) → true
  // groupSum5(0, [2, 5, 10, 4], 12) → false
  public boolean groupSum5(int start, int[] nums, int target) {
    boolean seen5ish = false;
    return groupSum5Aux(start, nums, target, seen5ish);
  }
  public boolean groupSum5Aux(int start, int[] nums, int target, boolean seen5ish) {
    if (start == nums.length)
      return target == 0;
    if (nums[start] % 5 == 0)
      seen5ish = true; // TODO: should be reset once the offending condition is removed
    if (!seen5ish || nums[start] != 1) {
      target -= nums[start];
      if (groupSum5Aux(start + 1, nums, target, seen5ish))
        return true;
      target += nums[start];
    }
    if (nums[start] % 5 != 0) {
      if (groupSum5Aux(start + 1, nums, target, seen5ish))
        return true;
    }
    return false;
  }


  // Given an array of ints, is it possible to choose a group of some of the
  // ints, such that the group sums to the given target, with this additional
  // constraint: if there are numbers in the array that are adjacent and the
  // identical value, they must either all be chosen, or none of them chosen. For
  // example, with the array {1, 2, 2, 2, 5, 2}, either all three 2's in the middle
  // must be chosen or not, all as a group. (one loop can be used to find the extent
  // of the identical values).
  // groupSumClump(0, [2, 4, 8], 10) → true
  // groupSumClump(0, [1, 2, 4, 8, 1], 14) → true
  // groupSumClump(0, [2, 4, 4, 8], 14) → false
  // groupSumClump(0, [8, 2, 2, 1], 9) → true
  // groupSumClump(0, [8, 2, 2, 1], 11) → false
  // groupSumClump(0, [1], 1) → true
  // groupSumClump(0, [9], 1) → false
  public boolean groupSumClump(int start, int[] nums, int target) {
    if (start == nums.length)
      return target == 0;

    int n = _getRepeatCount(start, nums);
    int repeatSum = _getRepeatSum(n, start, nums);

    target -= repeatSum;
    if (groupSumClump(start+n+1, nums, target))
      return true;

    target += repeatSum;
    if (groupSumClump(start+n+1, nums, target))
      return true;

    return false;
  }

  public int _getRepeatCount(int start, int[] nums) {
    int n = 0;
    while (start+n < nums.length-1)
      if (nums[start+n] == nums[start+n+1])
        n++;
      else
        break;
    return n;
  }

  public int _getRepeatSum(int nRepeat, int start, int[] nums) {
    int sum = 0;
    for (int k = start; k < start + nRepeat + 1; k++)
      sum += nums[k];
    return sum;
  }


  // Given an array of ints, is it possible to divide the ints into two
  // groups, so that the sums of the two groups are the same. Every int must be
  // in one group or the other. Write a recursive helper method that takes
  // whatever arguments you like, and make the initial call to your recursive
  // helper from splitArray(). (No loops needed.)
  // splitArray([2, 2]) → true
  // splitArray([2, 3]) → false
  // splitArray([5, 2, 3]) → true
  public boolean splitArray(int[] nums) {
    if (nums.length == 0)
      return true;
    Deque<Integer> sums = new ArrayDeque<Integer>();  // container to store the sums
    _splitArrayAux(0, nums, sums, 0);
    return _splitArrayCheckCompSum(sums); // match the sums in complementary positions
  }

  public void _splitArrayAux(int start, int[] nums, Deque<Integer> sums, int accum) {
    if (start == nums.length) // if reached past the last element
      sums.addLast(accum);    // populate the container with the finished accumulator
    else {
      _splitArrayAux(start+1, nums, sums, accum + nums[start]); // advance while including the current element
      _splitArrayAux(start+1, nums, sums, accum);               // advance while NOT including the current element
    }
  }

  public boolean _splitArrayCheckCompSum(Deque<Integer> sums) {
    if (sums.size() == 0) // if the container is vanished
      return false;       // return failure, since no match was found
    else if (sums.pollFirst() == sums.pollLast()) // match the elements in complementary positions
      return true;  // TADA!
    else
      return _splitArrayCheckCompSum(sums); // recurse
  }


  // Given an array of ints, is it possible to divide the ints into two groups,
  // so that the sum of one group is a multiple of 10, and the sum of the other
  // group is odd. Every int must be in one group or the other. Write a
  // recursive helper method that takes whatever arguments you like, and make
  // the initial call to your recursive helper from splitOdd10(). (No loops
  // needed.)
  // splitOdd10([5, 5, 5]) → true
  // splitOdd10([5, 5, 6]) → false
  // splitOdd10([5, 5, 6, 1]) → true
  public boolean splitOdd10(int[] nums) {
    Deque<Integer> sums = new ArrayDeque<Integer>();
    _splitOdd10Aux(0, nums, sums, 0);
    if (sums.size() == 1)
      return false;
    return _splitOdd10CheckCompSum(sums);
  }

  public void _splitOdd10Aux(int start, int[] nums, Deque<Integer> sums, int accum) {
    if (start == nums.length)
      sums.addLast(accum);
    else {
      accum += nums[start];
      _splitOdd10Aux(start+1, nums, sums, accum);
      accum -= nums[start];
      _splitOdd10Aux(start+1, nums, sums, accum);
    }
  }

  public boolean _splitOdd10CheckCompSum(Deque<Integer> sums) {
    if (sums.size() == 0)
      return false;
    int a = sums.pollFirst();
    int b = sums.pollLast();
    if ((a%10==0 && b%2==1) || (b%10==0 && a%2==1))
      return true;
    else
      return _splitOdd10CheckCompSum(sums);
  }


  // Given an array of ints, is it possible to divide the ints into two groups,
  // so that the sum of the two groups is the same, with these constraints: all
  // the values that are multiple of 5 must be in one group, and all the values
  // that are a multiple of 3 (and not a multiple of 5) must be in the other.
  // (No loops needed.)
  // split53([1, 1]) → true
  // split53([1, 1, 1]) → false
  // split53([2, 4, 2]) → true
  public boolean split53(int[] nums) {
    // containers to store the sums
    Deque<Double> sums5x = new ArrayDeque<Double>();
    Deque<Double> sums3x = new ArrayDeque<Double>();
    // Scan the array twice...
    _split53Aux(0, nums, sums5x, 0, 3);   //    once while avoiding 3x
    _split53Aux(0, nums, sums3x, 0, 5);   //    then while avoiding 5x
    // match the sums in complementary positions
    return _split53CheckCompSum(sums5x, sums3x);
  }

  public void _split53Aux(int start, int[] nums, Deque<Double> sums, double accum, int to_avoid) {
    if (start == nums.length) { // if reached past the last element
      sums.addLast(accum);      // populate the container with the finished accumulator
      return;
    }
    // avoid the elements that need to be avoided
    double incr = nums[start];
    if (to_avoid == 5) {
      if (nums[start] % 5 == 0)
        incr = Double.NaN; // invalidate the accumulator to identify later
    }
    else if (to_avoid == 3) {
      if ((nums[start] % 3 == 0) && (nums[start] % 5 != 0))
        incr = Double.NaN; // invalidate the accumulator to identify later
    }
    // Recurse
    _split53Aux(start+1, nums, sums, accum + incr, to_avoid); // advance while including the current element
    _split53Aux(start+1, nums, sums, accum, to_avoid);        // advance while NOT including the current element
  }

  public boolean _split53CheckCompSum(Deque<Double> sums1, Deque<Double> sums2) {
    if (sums1.size() == 0)  // if the container is vanished
      return false;         // return failure, since no match was found
    double a = sums1.pollFirst(); // extract head of first array
    double b = sums2.pollLast();  // extract tail of second array
    double c = sums1.pollLast();  // extract tail of first array
    double d = sums2.pollFirst(); // extract head of second array
    if ((a == b) || (c == d))     // match the elements in complementary positions
      return true;                // TADA!
    else
      return _split53CheckCompSum(sums1, sums2);  // recurse
  }

}
