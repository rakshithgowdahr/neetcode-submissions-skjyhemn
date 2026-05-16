class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        #1, 2, 4, 5
        #1, 2, 2, 3, 3
        i, j = 0, len(people)-1
        required_boats = 0
        while i <= j:
            if people[i]+people[j] > limit:
                j -= 1
            else:
                i += 1
                j -= 1
            required_boats += 1
        return required_boats