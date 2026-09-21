class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        word_array = []
        index = 0
        for string in strs:
            alphabet = [0] * 26
            for i in string:
                alphabet[ord(i)-97] += 1


            if tuple(alphabet) in word_dict:
                word_array[word_dict[tuple(alphabet)]].append(string)
          
            else:
                word_dict[tuple(alphabet)] = index
    
            
                word_array.append([string])

                index += 1
        return word_array
                



                


            

        
        