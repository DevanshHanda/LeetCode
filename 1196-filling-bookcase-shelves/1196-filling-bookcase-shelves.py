# from typing import List

# class Solution:
#     def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
#         return self.arrangeBooks(books, shelfWidth)

#     def arrangeBooks(self, books: List[List[int]], maxShelfWidth: int) -> int:
#         minHeights = [float('inf')] * (len(books) + 1)
#         minHeights[0] = 0

#         for bookIndex in range(1, len(books) + 1):
#             currentShelfHeight = 0
#             currentShelfWidth = 0

#             for lastBook in range(bookIndex - 1, -1, -1):
#                 currentBookThickness, currentBookHeight = books[lastBook]

#                 if currentShelfWidth + currentBookThickness > maxShelfWidth:
#                     break

#                 currentShelfWidth += currentBookThickness
#                 currentShelfHeight = max(currentShelfHeight, currentBookHeight)

#                 currentArrangementHeight = minHeights[lastBook] + currentShelfHeight
#                 minHeights[bookIndex] = min(minHeights[bookIndex], currentArrangementHeight)

#         return minHeights[len(books)]

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n+1)
        dp[n-1] = books[n-1][1]
        for i in range(n-2, -1, -1):
            curr_w, curr_h = books[i]
            dp[i] = dp[i+1] + curr_h
            for j in range(i+1, n):
                curr_h = max(curr_h, books[j][1])
                curr_w += books[j][0]
                if curr_w > shelfWidth:
                    break
                dp[i] = min(dp[i], dp[j+1]+curr_h)
        return dp[0]