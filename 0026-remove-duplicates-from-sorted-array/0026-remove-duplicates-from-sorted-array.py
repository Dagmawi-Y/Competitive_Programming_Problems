class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_pointer = 0
        for read_pointer in range(1, len(nums)):
            if nums[write_pointer] != nums[read_pointer]:
                write_pointer += 1
                nums[write_pointer] = nums[read_pointer]
        return write_pointer + 1


        