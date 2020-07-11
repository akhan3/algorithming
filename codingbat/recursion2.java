// https://codingbat.com/java/Recursion-2

// Harder recursion problems. Currently, these are all recursive
// backtracking problems with arrays.

// groupSum         groupSum6       groupNoAdj
// groupSum5        groupSumClump   splitArray
// splitOdd10       split53

import java.util.Stack;
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


  // Given an array of ints, is it possible to choose a group of some of the ints, beginning at the start index, such that the group sums to the given target? However, with the additional constraint that all 6's must be chosen. (No loops needed.)
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


  // Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target with this additional constraint: If a value in the array is chosen to be in the group, the value immediately following it in the array must not be chosen. (No loops needed.)
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



  // Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target with these additional constraints: all multiples of 5 in the array must be included in the group. If the value immediately following a multiple of 5 is 1, it must not be chosen. (No loops needed.)
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

}

