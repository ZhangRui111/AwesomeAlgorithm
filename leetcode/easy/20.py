"""
tag: 栈；字符串
20. 有效的括号
https://leetcode.cn/problems/valid-parentheses/
"""


def isValid(s: str) -> bool:
    if len(s) % 2 == 1:
        return False

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack = list()
    for ch in s:
        if ch in pairs:  # i.e., if ch in pairs.keys():
            # not stack == True, i.e., stack is empty
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)

    return not stack


def main():
    print(isValid("{()}"))
    print(isValid("{(})}"))


if __name__ == '__main__':
    main()
