class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for word in strs:
            sorted_words = ''.join(sorted(word))
            output[sorted_words].append(word)
        #print(list(output.values()))
        return list(output.values())
