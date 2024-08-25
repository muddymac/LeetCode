class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        # start looping over each word in the list
        for word in strs:
            # create a hashmap for each word from 0..26 as key and the word as the value
            # [0, 0, 1,...0]: ["cop"]
            count = [0] *26
            # loop over each letter
            for letter in word:
                count[ord(letter) - ord("a")] += 1
                # when looping over c, count becomes: [0,0,1,0,0..]
            res[tuple(count)].append(word)
        return res.values()