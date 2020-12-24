/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    var head = 0;
    var tail = nums.length-1;
    var new_nums = new Array(nums.length);
    for(var i = nums.length-1; i >= 0; i--){
        if(Math.abs(nums[tail]) > Math.abs(nums[head])){
            new_nums[i] = nums[tail] * nums[tail];
            tail--;
        }
        else{
            new_nums[i] = nums[head] * nums[head];
            head++;
        }
    }
    return new_nums;
};
