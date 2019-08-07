import math
import heapq
from helpers import Map, load_map, show_map

class Node():

    """A node class for A* Pathfinding"""



    def __init__(self, parent=None, position=None, number = None):

        self.parent = parent

        self.position = position

        self.number = number

        self.g = 0

        self.h = 0

        self.f = 0



    def __eq__(self, other):

        return self.position == other.position
def distance(start,end):
    return math.hypot(end[0] - start[0], end[1] - start[1])
    
"""
def shortest_path(M,start,goal):
    print("shortest path called")
    # Initialize both open and closed list
    start_0 = M.intersections[start][0]
    start_1 = M.intersections[start][1]
    start_node = Node(None, (start_0,start_1),start)
    start_node.g = start_node.h = start_node.f = 0

    goal_0 = M.intersections[goal][0]
    goal_1 = M.intersections[goal][1]
    end_node = Node(None, (goal_0,goal_1),goal)

    end_node.g = end_node.h = end_node.f = 0
    open_list = []
    closed_list = []
    # add the start node
    open_list.append(start_node) # list contains tuples(?)
    while len(open_list) > 0 :
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
        
        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                #path.append(current.position)
                path.append(current.number)
                current = current.parent
            return path[::-1] # Return reversed path
        #generate children
        #print(current_index)
        children = []
        for neighbor in M.roads[current_index]:
            #create new_node
            position_0 = M.intersections[neighbor][0]
            position_1 = M.intersections[neighbor][1]
            new_node = Node(current_node,(position_0, position_1),neighbor)
            children.append(new_node)
            
        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue
                    
            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = distance(child,end_node)
            #child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h
            
            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
    return
"""
def shortest_path(M,start,goal):
    # idea source : https://www.redblobgames.com/pathfinding/a-star/implementation.html
    frontier = [] # expanding ring on the grid, implemented as priority queue, as min-heap
    heapq.heappush(frontier, (0,start)) # priority queue has cost and node
    came_from = {} #for each location points to the place where we came from. 
    cost_so_far = {} #to keep track of the total movement cost from the start location
    came_from[start] = None
    cost_so_far[start] = 0
    
    while len(frontier) > 0 : # until frontier is empty
        #pick a location from min-heap,look at neighbors, any neighbors not visited add it to frontier and mark it visited 
        current = heapq.heappop(frontier)[1]
        
        if current == goal: #stop expanding frontier as soon as we find our goal
            break
        for neighbor in M.roads[current]:
            cost = distance(M.intersections[current],M.intersections[neighbor])
            new_cost = cost_so_far[current] + cost
            # heuristic will not be larger than the shortest distance to choose optimal path
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                came_from[neighbor] = current
                cost_so_far[neighbor] = new_cost
                heapq.heappush(frontier,(new_cost,neighbor)) # add location if the new path to the location is better than the best previous path.
                
    path = reconstruct_path(came_from,start,goal)
    return path
                
#To build the path, start at the end and follow the came_from map, which points to the previous node. When we reach start, we’re done. It is the backwards path, so call reverse() 
def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    #follow backwards from the goal to the start
    if current not in came_from:
        print("goal not in map")
        return
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    
    return path[::-1]

