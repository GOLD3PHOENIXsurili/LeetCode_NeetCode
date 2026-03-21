# Python

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x,y = m-1,n-1

        for z in range(m+n-1,-1,-1):
            if x < 0:
                nums1[z] = nums2[y]
                y -= 1
            elif y < 0:
                break
            elif nums1[x] > nums2[y]:
                nums1[z] = nums1[x]
                x -= 1
            else:
                nums1[z] = nums2[y]
                y -= 1


# CPP
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int a=0, b=0;
        vector<int> temp;
        while(a<m && b<n){
            if(nums1[a] >= nums2[b]){
                temp.push_back(nums2[b++]);
            }
            else{
            temp.push_back(nums1[a++]);
            }
        }
        while(a<m){
            temp.push_back(nums1[a++]);
        }
        while(b<n){
            temp.push_back(nums2[b++]);
        }
        
        nums1 = temp;
    }
};