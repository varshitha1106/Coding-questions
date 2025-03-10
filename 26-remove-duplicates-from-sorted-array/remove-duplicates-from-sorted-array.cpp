class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        set <int> set;
        int n=nums.size();
        for(int i=0;i<n;i++){
            set.insert(nums[i]);
        }
        int k=set.size();
        int index=0;
        for(auto i:set){
            nums[index]=i;
            index++;
        }
        return k;
        
    }
};