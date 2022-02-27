class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        a= nums1
        b =nums2
        
        if len(a) > len(b) :
            a,b = b,a
            
        l= 0 
        r= len(a) -1 
        total = ( len(a) + len(b))//2
        
        
        while True:
            mid_a = (l+r)//2
            mid_b = total - 2 -mid_a
            
            
            a_left = a[mid_a] if mid_a >=0 else float('-inf')
            a_right = a[mid_a+1] if mid_a +1 < len(a) else float('inf')
            
            b_left = b[mid_b] if mid_b >=0 else float ('-inf')
            
            b_right = b[mid_b +1] if mid_b +1 < len(b) else float('inf')
            
            if b_left <= a_right and a_left<=b_right:
                
                if (len(a) + len(b)) % 2 ==1:
                    return min(a_right,b_right)
                
                else:
                    return (max(a_left,b_left) + min(a_right,b_right))/2
                
            elif a_left > b_right:
                r = mid_a - 1
            else:
                l =mid_a +1 
                
                
        
        
        
        
        