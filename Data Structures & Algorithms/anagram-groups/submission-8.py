class Solution:
    '''def groupAnagrams(self, strs: List[str]):
        output = defaultdict(list)
        for word in strs:
            sorted_words = ''.join(sorted(word))
            output[sorted_words].append(word)
        #print(list(output.values()))
        return output'''

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        output = {} # Use a regular dictionary 
        for word in strs: 
            sorted_words = ''.join(sorted(word)) 
            if sorted_words not in output: 
                output[sorted_words] = [] 
                # Initialize an empty list if the key does not exist 
            output[sorted_words].append(word) 
        return list(output.values())