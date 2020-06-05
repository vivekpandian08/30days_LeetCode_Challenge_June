class Solution:
    def reverseString(self, array: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(array)
        left =0
        right=n-1
        while left<=right:
            array[left],array[right]=array[right],array[left]
            left+=1
            right-=1
        return array