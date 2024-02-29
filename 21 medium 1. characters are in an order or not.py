def is_valid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False
        else:
            # If the character is neither opening nor closing bracket
            return False

    # After iterating through the string, the stack should be empty if it's valid
    return not stack


# Example usage:
input_str = "([{}])"
print(is_valid(input_str))  # Output: True

input_str = "([)]"
print(is_valid(input_str))  # Output: False
