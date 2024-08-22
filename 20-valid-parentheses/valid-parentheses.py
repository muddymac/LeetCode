class Solution:
    def isValid(self, s: str) -> bool:
        # iterate over each string item
        # create a mapping_dict
        paranthesis_map = {
            "}": "{", 
            ")": "(", 
            "]": "["
        }
        # second approach
        # create a mapping and when each closes, then reduce the opening
        stack = []
        '''
        for each_par in s:
            if each_par in mapping_dict:
                mapping_dict[each_par] += 1
            else:
                if mapping_dict.get(paranthesis_map.get(each_par)):
                    mapping_dict[paranthesis_map[each_par]] -= 1
                    if mapping_dict[paranthesis_map[each_par]] == 0:
                        del mapping_dict[paranthesis_map[each_par]]
                else:
                    mapping_dict[each_par] = 1
        print(mapping_dict)
        return True if not mapping_dict else False
        '''
        for char in s:
            if char in paranthesis_map.values():
                stack.append(char)
            elif char in paranthesis_map.keys():
                if not stack or paranthesis_map[char] != stack.pop():
                    return False
        return not stack

        