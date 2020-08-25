class Solution {
    public int longestSubarray(int[] nums, int limit) {
        PriorityQueue<Integer> max = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> min = new PriorityQueue<>();
        int runningSize = 0;
        int start = 0; 
        for(int end = 0; end < nums.length; end++){
            max.add(nums[end]);
            min.add(nums[end]);
            int largest = max.peek();
            int smallest = min.peek();
            if (largest - smallest <= limit) {
                runningSize = Math.max(runningSize, (end-start) + 1);
            } else {
                min.remove(new Integer(nums[start]));
                max.remove(new Integer(nums[start]));
                start++;
            }
        }
        return runningSize;
    }
}