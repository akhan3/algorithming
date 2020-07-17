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
    if (groupSum(start + 1, nums, target - nums[start]))
      return true;
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
    if (start == nums.length)
      return target == 0;
    if (groupSum6(start + 1, nums, target - nums[start]))
      return true;
    if (nums[start] != 6)
      if (groupSum6(start + 1, nums, target))
        return true;
    return false;
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
    return groupNoAdj(0, nums, target, true);
  }

  public boolean groupNoAdj(int start, int[] nums, int target, boolean allowed) {
    if (start == nums.length)
      return target == 0;
    if (allowed)
      if (groupNoAdj(start+1, nums, target-nums[start], false))
        return true;
    if (groupNoAdj(start+1, nums, target, true))
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
    if (start == nums.length)
      return target == 0;
    if (!((start > 0) && (nums[start-1] % 5 == 0) && nums[start] == 1))
      if (groupSum5(start + 1, nums, target - nums[start]))
        return true;
    if (!(nums[start] % 5 == 0))
      if (groupSum5(start + 1, nums, target))
        return true;
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

    int k = 0;
    while((start+k+1 < nums.length) && (nums[start+k+1] == nums[start+k]))
        k++;

    if (groupSumClump(start+k+1, nums, target - (k+1)*nums[start]))
      return true;
    if (groupSumClump(start+k+1, nums, target))
      return true;
    return false;
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
    return splitArray(0, nums, 0, 0);
  }

  public boolean splitArray(int start, int[] nums, int accum1, int accum2) {
    if (start == nums.length)
      return accum1 == accum2;
    if (splitArray(start+1, nums, accum1 + nums[start], accum2))
      return true;
    if (splitArray(start+1, nums, accum1, accum2 + nums[start]))
      return true;
    return false;
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
    return splitOdd10(0, nums, 0, 0);
  }

  public boolean splitOdd10(int start, int[] nums, int accum1, int accum2) {
    if (start == nums.length)
      return ((accum1 % 10 == 0) && (accum2 % 2 == 1)) ||
             ((accum2 % 10 == 0) && (accum1 % 2 == 1));
    if (splitOdd10(start+1, nums, accum1 + nums[start], accum2))
      return true;
    if (splitOdd10(start+1, nums, accum1, accum2 + nums[start]))
      return true;
    return false;
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
    return split53(0, nums, 0, 0);
  }

  public boolean split53(int start, int[] nums, int accum1, int accum2) {
    if (start == nums.length)
      return accum1 == accum2;
    if (nums[start] % 5 == 0)
      return split53(start+1, nums, accum1+nums[start], accum2);
    else if ((nums[start] % 3 == 0) && (nums[start] % 5 != 0))
      return split53(start+1, nums, accum1, accum2+nums[start]);
    else {
      if (split53(start+1, nums, accum1 + nums[start], accum2))
        return true;
      if (split53(start+1, nums, accum1, accum2 + nums[start]))
        return true;
    }
    return false;
  }

}
