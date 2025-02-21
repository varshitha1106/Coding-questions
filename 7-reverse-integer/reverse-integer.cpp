class Solution {
public:
    int reverse(int x) {
        long revnum=0;
        while(x!=0){
            int lastdigit=x%10;
            revnum=(revnum*10)+lastdigit;
            x=x/10;
        }
        if(revnum>INT_MAX || revnum<INT_MIN) return 0;
       
        return revnum;
        
    }
};