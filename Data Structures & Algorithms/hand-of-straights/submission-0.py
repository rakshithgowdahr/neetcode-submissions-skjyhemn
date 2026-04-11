class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
            
        # FIX 1: Sort first! Now your stored indices will actually align 
        # with the array, and identical numbers will be next to each other.
        hand.sort()
        
        hash_map = dict()
        for i in range(len(hand)):
            if hand[i] in hash_map:
                hash_map[hand[i]][1] += 1
            else:
                hash_map[hand[i]] = [i, 1] # index, count
                
        i = 0
        while i < len(hand):
            if hand[i] is True:
                i += 1
                continue
            
            # FIX 2: Remove the starting number of the sequence from the hash_map.
            start_num = hand[i]
            if hash_map[start_num][1] <= 1:
                del hash_map[start_num]
            else:
                hash_map[start_num][0] += 1
                hash_map[start_num][1] -= 1
                
            hand[i] = True # Mark it as used immediately
            
            hop, next_num = 1, start_num
            while hop < groupSize:
                temp_num = next_num + 1
                
                if temp_num not in hash_map:
                    return False
                
                # Mark the next sequence number as True using your index pointer
                hand[hash_map[temp_num][0]] = True
                
                if hash_map[temp_num][1] <= 1:
                    del hash_map[temp_num]
                else:
                    hash_map[temp_num][0] += 1 # Shifts the pointer to the next duplicate
                    hash_map[temp_num][1] -= 1
                    
                next_num = temp_num
                hop += 1
                
            i += 1
            
        return True