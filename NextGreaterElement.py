#You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in #the corresponding places of nums2.
#
#The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.
#
#Example 1:
#Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
#Output: [-1,3,-1]
#Explanation:
#    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
#    For number 1 in the first array, the next greater number for it in the second array is 3.
#    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
#Example 2:
#Input: nums1 = [2,4], nums2 = [1,2,3,4].
#Output: [3,-1]
#Explanation:
#    For number 2 in the first array, the next greater number for it in the second array is 3.
#    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
#Note:
#All elements in nums1 and nums2 are unique.
#The length of both nums1 and nums2 would not exceed 1000.

class Solution:
    NOT_EXISTS = -1
    
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        self.__numbers_first = nums1
        self.__numbers_second = nums2
        self.__output = list()
        self.__getResult()
        return self.__output
    
    def __getResult(self):
        for i in self.__numbers_first:
            try:
                index_in_other_array = self.__numbers_second.index(i)
            except ValueError:
                index_in_other_array = self.NOT_EXISTS
            
            greater_or_not_exists = self.__getNextGreaterElementFromSecond(index_in_other_array,i)
            self.__output.append(greater_or_not_exists)
            
    def __getNextGreaterElementFromSecond(self,index_in_other_array,element_value):          
        if index_in_other_array == self.NOT_EXISTS:
            return self.NOT_EXISTS
        for i in self.__numbers_second[index_in_other_array:]: 
            next = self.NOT_EXISTS
            if i > element_value: 
                next = i 
                break
        return next
    