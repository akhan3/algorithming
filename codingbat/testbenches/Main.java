// How to compile and run
// javac Main.java && java -ea Main

import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");

        // assert array220(new int [] {3, 30}, 0) == true;
        // assert array220(new int [] {3}, 0) == false;
        // assert array220(new int [] {}, 0) == false;
        // assert array220(new int [] {3, 3, 30, 4}, 0) == true;
        // assert array220(new int [] {2, 19, 4}, 0) == false;
        // assert array220(new int [] {20, 2, 21}, 0) == false;
        // assert array220(new int [] {20, 2, 21, 210}, 0) == true;
        // assert array220(new int [] {2, 200, 2000}, 0) == true;
        // assert array220(new int [] {0, 0}, 0) == true;
        // assert array220(new int [] {1, 2, 3, 4, 5, 6}, 0) == false;
        // assert array220(new int [] {1, 2, 3, 4, 5, 50, 6}, 0) == true;
        // assert array220(new int [] {1, 2, 3, 4, 5, 51, 6}, 0) == false;
        // assert array220(new int [] {1, 2, 3, 4, 4, 50, 500, 6}, 0) == true;

        boolean a = array220(new int [] {30, 1, 4, 5, 3, 17}, 0);
        System.out.println("array220(new int [] {30, 1, 4, 5, 3, 17}, 0) returns " + a);
        assert a == true;


    }

  // public static boolean array220(intnew int [] {} nums, int index) {
  //   if (index >= nums.length - 1)
  //     return false;
  //   else if (numsnew int [] {index} * 10 == numsnew int [] {index+1})
  //     return true;
  //   else
  //     return array220(nums, index+1);
  // }

  // Another solution challenged by Umair
  // public static boolean array220(int[] nums, int index) {
  //   if (nums.length <= 1)
  //     return false;
  //   else if (nums[0] * 10 == nums[1])
  //     return true;
  //   else {
  //     nums = Arrays.copyOfRange(nums, 1, nums.length);
  //     return array220(nums, -1);
  //   }
  // }

  // Umair's solution based on associative arrays
  public static boolean array220(int[] nums, int index) {
    return array220___(nums, index, new HashMap<Integer, Integer>());
  }
  public static boolean array220___(int[] nums, int index, Map<Integer, Integer> map) {
    if(index >= nums.length)
      return false;
    Integer [] k_arr = map.keySet().toArray(new Integer [map.keySet().size()]);
    Integer [] v_arr = map.values().toArray(new Integer [map.keySet().size()]);
    System.out.println(nums[index] + "\tmap: " + map.keySet() + " --> " + map.values());
    if(map.get(nums[index]) != null) {
      return true;
    }
    else {
      map.put(nums[index]*10, nums[index]);
      map.put(nums[index], nums[index]*10);
      return array220___(nums, index+1, map);
    }
  }

}
