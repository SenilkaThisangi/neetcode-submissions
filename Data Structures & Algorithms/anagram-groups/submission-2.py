class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_array = defaultdict(list)
        
        for string in strs:
            alphabet = [0] * 26
            for i in string:
                alphabet[ord(i)-97] += 1


            word_array[tuple(alphabet)].append(string)
        return list(word_array.values())
                



                


            

        
        