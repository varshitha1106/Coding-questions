class Solution:
    def ExtractNumber(self,sentence):
        #code here
        words=sentence.split()
        max_num=-1
        for word in words:
            if word.isdigit() and '9' not in word:
                num=int(word)
                max_num=max(max_num,num)
        return max_num
                
        