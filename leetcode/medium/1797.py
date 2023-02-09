"""
tag: 设计；哈希表
1797. 设计一个验证系统
https://leetcode.cn/problems/design-authentication-manager/
"""


class AuthenticationManager0:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.tokens.get(tokenId, None) and \
                currentTime - self.tokens.get(tokenId, None) < self.timeToLive:
            self.tokens[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        valid_time = currentTime - self.timeToLive
        self.tokens = {k: v for k, v in self.tokens.items() if v > valid_time}
        return len(self.tokens)


class AuthenticationManager1:
    """ Python 有序字典 OrderedDict (维护插入顺序的双向链表) """
    def __init__(self, timeToLive: int):
        self.t = timeToLive
        self.data = OrderedDict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.data[tokenId] = currentTime + self.t

    def renew(self, tokenId: str, currentTime: int) -> None:
        while self.data and next(iter(self.data.values())) <= currentTime:
            self.data.popitem(last=False)
        if tokenId in self.data:
            self.data[tokenId] = currentTime + self.t
            self.data.move_to_end(tokenId)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        while self.data and next(iter(self.data.values())) <= currentTime:
            self.data.popitem(last=False)
        return len(self.data)
