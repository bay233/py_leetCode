# 815. 公交路线

class Solution:
    # def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
    def numBusesToDestination(self, routes, source: int, target: int) -> int:
        if source == target: return 0
        station_index = {}
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                if routes[i][j] in station_index:
                    station_index[routes[i][j]].append(i)
                else:
                    station_index[routes[i][j]] = [i]
        print(station_index)
        station_book = set()
        route_book = set()
        queue = [station_index[source]]
        res = 0
        while queue:
            res += 1
            if res > len(routes): return -1
            tmp_queue = []
            for route_idx in queue.pop():
                if route_idx in route_book: continue
                for station in routes[route_idx]:
                    if station == target: return res
                    if station in station_book: continue
                    tmp_queue.extend(station_index[station])
                    station_book.add(station)
                route_book.add(route_idx)
            if tmp_queue: queue.append(tmp_queue)
        return -1

s = Solution()
print(s.numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6))