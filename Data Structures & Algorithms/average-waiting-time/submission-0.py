class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        avg_wait = 0
        prev_order_end = customers[0][0]
        for i, cust in enumerate(customers):
            # print("prev_order_end", prev_order_end)
            cust_arrived_at, order_prepare_time = cust
            order_finished_at = max(prev_order_end, cust_arrived_at)+order_prepare_time#(3+5)
            # print("order_finished_at", order_finished_at)
            curr_await = order_finished_at-cust_arrived_at
            # print("curr_wait", curr_await)
            avg_wait += (curr_await)
            # print("avg_wait", avg_wait)
            prev_order_end = order_finished_at
        return avg_wait/len(customers)
