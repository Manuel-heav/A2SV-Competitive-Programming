class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ticketQueue = deque()
        for i,tik in enumerate(tickets):
            ticketQueue.append((tik, i))

        counter = 0
        print(ticketQueue)
        while ticketQueue:
            tik, i =  ticketQueue.popleft()
            counter += 1
            tik -= 1
            if tik > 0:
                ticketQueue.append((tik, i))
            if tik == 0 and i == k:
                break
        return counter




        # for i in range(len(ticketQueue)):
        #     if ticketQueue[k] != 0:
        #         first_el = ticketQueue.popleft() - 1
        #         if first_el != -1:
        #             ticketQueue.append(first_el)
        #         counter += 1
        # print(ticketQueue)
        return counter
                






















        