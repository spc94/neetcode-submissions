class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        return_digits = digits
        current_index = len(digits) - 1
        current_value = digits[current_index]

        while current_value >= 9:
          return_digits[current_index] = 0
          if current_index == 0:
            return_digits = [1] + return_digits
            return return_digits
          current_index -= 1
          current_value = digits[current_index]
        
        return_digits[current_index] = return_digits[current_index]+1
        

        return return_digits


        
        