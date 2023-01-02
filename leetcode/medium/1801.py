"""
tag: 数组；模拟；堆（优先队列）
1801. 积压订单中的订单总数
https://leetcode.cn/problems/number-of-orders-in-the-backlog/
"""
import heapq


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy_backlog, sell_backlog = [], []
        for od_price, od_amount, od_type in orders:
            if od_type == 0:  # a buy order
                while sell_backlog and sell_backlog[0][0] <= od_price \
                        and od_amount:
                    if sell_backlog[0][1] > od_amount:
                        sell_backlog[0][1] -= od_amount
                        od_amount = 0
                    else:
                        od_amount -= heapq.heappop(sell_backlog)[1]
                if od_amount:
                    heapq.heappush(buy_backlog, [-od_price, od_amount])
            else:  # a sell order
                while buy_backlog and -buy_backlog[0][0] >= od_price \
                        and od_amount:
                    if buy_backlog[0][1] > od_amount:
                        buy_backlog[0][1] -= od_amount
                        od_amount = 0
                    else:
                        od_amount -= heapq.heappop(buy_backlog)[1]
                if od_amount:
                    heapq.heappush(sell_backlog, [od_price, od_amount])

        buy_backlog = [item[1] for item in buy_backlog]
        sell_backlog = [item[1] for item in sell_backlog]
        return (sum(buy_backlog) + sum(sell_backlog)) % (10 ** 9 + 7)
