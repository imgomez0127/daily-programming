from functools import reduce
class Solution:
    def visit_rooms(self,current_room,rooms,visited_rooms):
        visited_rooms[current_room] = True
        for reachable_room in rooms[current_room]:
            if not visited_rooms[reachable_room]:
                visited_rooms = self.visit_rooms(reachable_room,rooms,visited_rooms)
        return visited_rooms

    def canVisitAllRooms(self, rooms) -> bool:
        if(len(rooms) == 0):
            return False
        visited_rooms = [False for _ in range(len(rooms))]
        visited_rooms = self.visit_rooms(0,rooms,visited_rooms)
        return all(visited_rooms)

print(Solution().canVisitAllRooms([[1,2,3],[2],[3],[]]))
