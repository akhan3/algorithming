// https://codingbat.com/java/Recursion-2

// Harder recursion problems. Currently, these are all recursive
// backtracking problems with arrays.

// groupSum         groupSum6       groupNoAdj
// groupSum5        groupSumClump   splitArray
// splitOdd10       split53

public class recursion2 {


  public static void main(String[] args) {
    int [] nums = {2,4,8};
    boolean found = groupSum(0, nums, 10);
    System.out.println("found: " + found);

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
  public static boolean groupSum(int start, int[] nums, int target) {
    if (nums.length == 0 && target == 0)
      return true;
    // sum =
    // if (target == 0)
      return false;
  }


  public int arraySum(int start, int[] nums) {
    if (start == nums.length - 1)
      return nums[start];
    else
     return nums[0] + arraySum(start+1, nums);
  }




}

