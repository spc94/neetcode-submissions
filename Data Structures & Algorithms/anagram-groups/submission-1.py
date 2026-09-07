class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #it allows to add if it didnt exist before
        output = defaultdict(list)
        for word in strs:
            sorted_words = ''.join(sorted(word))
            output[sorted_words].append(word)
        print(list(output.values()))
        return list(output.values())
        