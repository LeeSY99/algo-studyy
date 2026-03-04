class Solution {
    public int minSteps(String s, String t) {
        int n = s.length();
        Map<Character, Integer> map_s = new HashMap<>();
        Map<Character, Integer> map_t = new HashMap<>();

        for (int i=0; i<n; i++) {
            char cs = s.charAt(i);
            char ct = t.charAt(i);

            map_s.put(cs, map_s.getOrDefault(cs, 0) + 1);
            map_t.put(ct, map_t.getOrDefault(ct, 0) + 1);
        }
        int answer = 0;
        
        for (Map.Entry<Character, Integer> e: map_t.entrySet()){
            char c = e.getKey();
            int cnt_t = e.getValue();
            int cnt_s = map_s.getOrDefault(c, 0);
            
            if (cnt_t > cnt_s) {
                answer += (cnt_t - cnt_s);
            }
        }
        return answer;

    }
}