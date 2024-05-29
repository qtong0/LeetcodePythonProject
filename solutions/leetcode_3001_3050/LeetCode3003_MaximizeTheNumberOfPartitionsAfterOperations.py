class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        states = set()
        states.add((0, 0, 0))  # (partition_count, chart_bitmask, change_used)

        for c in s:
            new_states = set()
            char_bit = 1 << (ord(c) - ord('a'))  # Bit representation of the current character

            for partition_count, char_mask, changed_used in states:
                # If adding this character exceeds k distinct characters, start a new partition
                if bin(char_mask | char_bit).count('1') > k:
                    new_states.add((partition_count + 1, char_bit, changed_used))
                else:
                    new_states.add((partition_count, char_mask | char_bit, changed_used))

                # If change operation has not been used, try changing the current character
                if changed_used == 0:
                    change_attempts = 0
                    for bit in range(26):
                        new_char_bit = 1 << bit
                        if char_mask & new_char_bit:
                            continue  # Skip if this character already exists in the current partition

                        # Check the new state after changing the character
                        if bin(char_mask | new_char_bit).count('1') > k:
                            new_states.add((partition_count + 1, new_char_bit, 1))
                        else:
                            new_states.add((partition_count, char_mask | new_char_bit, 1))
                        change_attempts += 1

                        if change_attempts == 3:
                            break  # Limit the number of changes to check

            states = new_states

        return max(states)[0] + 1


    def test(self):
        pass


if __name__ == '__main__':
    Solution().test()
