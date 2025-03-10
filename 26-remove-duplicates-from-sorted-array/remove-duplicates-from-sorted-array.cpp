class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n=nums.size();
        int i=0;
        for (int j=1;j<n;j++)
        {
            if(nums[j]!=nums[i])
            {
                nums[i+1]=nums[j];
                i++;
            }
            
        }
        return i+1;
    }
};
    

    /*Brute force solution
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
    */
