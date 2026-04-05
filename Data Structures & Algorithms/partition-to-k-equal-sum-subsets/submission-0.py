class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        partition_length = total / k
        partitions = [0] * k
        nums.sort(reverse=True)

        return self.dfs(0, partition_length, partitions, nums)
    
    def dfs(self, index, length, partitions, nums):
        if index == len(nums):
            return partitions[0] == length
        
        for i in range(len(partitions)):
            if nums[index] + partitions[i] > length:
                continue
            
            if i > 0 and partitions[i - 1] == partitions[i]:
                continue
            
            partitions[i] += nums[index]
            if self.dfs(index + 1, length, partitions, nums):
                return True
            partitions[i] -= nums[index]
            
        return False