# two pointers, linked list

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        n = 0

        curr = head
        arr = []

        while curr:
            arr.append(curr)
            n+=1
            curr = curr.next
        
        left, right = 0, n - 1
        last = head

        while left < right:
            arr[left].next = arr[right]
            left += 1

            if left == right:
                last = arr[right]
                break

            arr[right].next = arr[left]
            right -= 1

            last = arr[left]
        if last:
            last.next = None
