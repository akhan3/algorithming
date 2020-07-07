// https://codingbat.com/prob/p115011

// Modify and return the given map as follows: if the keys "a" and "b" are
// both in the map and have equal values, remove them both.

// mapAB2({"a": "aaa", "b": "aaa", "c": "cake"}) → {"c": "cake"}
// mapAB2({"a": "aaa", "b": "bbb"}) → {"a": "aaa", "b": "bbb"}
// mapAB2({"a": "aaa", "b": "bbb", "c": "aaa"}) → {"a": "aaa", "b": "bbb", "c": "aaa"}
// mapAB2({"a": "aaa"}) → {"a": "aaa"}
// mapAB2({"b": "bbb"}) → {"b": "bbb"}
// mapAB2({"a": "", "b": "", "c": "ccc"}) → {"c": "ccc"}
// mapAB2({}) → {}
// mapAB2({"a": "a", "b": "b", "z": "zebra"}) → {"a": "a", "b": "b", "z": "zebra"}

import java.util.Map;
import java.util.HashMap;

public class mapAB2 {

    public static void main(String[] args) {
        Map<String, String> map = new HashMap<String, String>();
        map.put("a", "aaa");
        map.put("b", "aaa");
        map.put("c", "cake");
        System.out.println(map);

        // How to get a new copy of map from the function?
        // Map<String, String> map2 = new mapAB2(map);
        Map<String, String> map2 = mapAB2(map);
        System.out.println(map);
        System.out.println(map2);

        // mapAB2({"a": "", "b": "", "c": "ccc"}) → {"c": "ccc"}
        map = new HashMap<String, String>();
        map.put("a", "");
        map.put("b", "");
        map.put("c", "ccc");

        System.out.println(map);
        System.out.println(mapAB2(map));
    }

    public static Map<String, String> mapAB2(Map<String, String> map) {
      if (map.containsKey("a") && map.containsKey("b")) {
        if (map.get("a") == map.get("b")) {
          map.remove("a");
          map.remove("b");
        }
      }
      return map;
    }
}

