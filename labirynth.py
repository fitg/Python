# Copyright (c) 2016 Hubert Jarosz
#
# This software is provided 'as-is', without any express or implied
# warranty. In no event will the authors be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgement in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.
# origin: https://github.com/vadim-job-hg/Codingame/blob/master/HARD/THE%20LABYRINTH/python3/the-labyrinth.py

import sys
import math

BFS = 1

# quick debug method as codingame does not display stdout
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

class Game:
    def __init__(self, search_strategy, num_rows, num_columns, num_rounds_to_alarm):
        self.strategy = SearchStrategy(search_strategy, num_rows, num_columns)

    def get_destination(self, start, back):
        if not back:
            go_to = self.strategy.search(start, '?')
            return go_to if go_to else self.strategy.search(start, 'C')
        else:
            return self.strategy.search(start, 'T')

    def move_kirk(self, destination, kirk_location_row, kirk_location_column):
        if destination[0] > kirk_location_row:
            print("DOWN")
        elif destination[0] < kirk_location_row:
            print("UP")
        elif destination[1] > kirk_location_column:
            print("RIGHT")
        else:
            print("LEFT")


class MapUtils:
    def __init__(self, num_rows, num_columns):
        self.num_rows = num_rows
        self.num_columns = num_columns

    def _is_coordinate_in_map(self, coordinate):
        if coordinate[0] < 0 or coordinate[0] >= self.num_rows or coordinate[1] < 0 or coordinate[1] >= self.num_columns:
            return False
        return True

    def _get_neighbouring_locations(self, vertex):
        vr, vc = vertex
        first_set = {(vr-1, vc), (vr+1, vc), (vr, vc-1), (vr, vc+1)}

        return {v for v in first_set if self._is_coordinate_in_map(v)}

    def get_valid_neighbours(self, game_map, forbidden_symbols, vertex):
        return {x for x in self._get_neighbouring_locations(vertex) if game_map[x[0]][x[1]] not in forbidden_symbols}

    def take_step(self, parent, start, n):
        v = n
        while parent[v[0]][v[1]] != start:
            v = parent[v[0]][v[1]]
        return v

class SearchStrategy:
    def __init__(self, strategy_selector, num_rows, num_columns):
        self.strategy = None
        if strategy_selector == BFS:
            self.strategy = SearchStrategyBFS(num_rows, num_columns)

    def update_map(self, game_map):
        self.strategy.update_map(game_map)

    def search(self, start, goal):
        return self.strategy.search(start, goal)

#breadth-first search
class SearchStrategyBFS:
    def __init__(self, num_rows, num_columns):
        self.map_utils = MapUtils(num_rows, num_columns)
        self.queue = []
        self.reviewed = []
        self.parents = []
        self.forbidden_symbols = ['#']

    def update_map(self, game_map):
        self.game_map = game_map

    # this method just resets the tracking of visited nodes and parents
    def _prepare_tracking(self, start):
        self.queue = []
        self.reviewed = []
        self.parents = []
        self.forbidden_symbols = ['#']
        
        for row in range(len(self.game_map)):
            self.reviewed.append([])
            self.parents.append([])
            for column in range(len(self.game_map[row])):
                self.reviewed[row].append(0)
                self.parents[row].append(None)

        self.reviewed[start[0]][start[1]] = True

        self.queue.append(start)

    def _mark_reviewed(self,u,n):
        self.reviewed[n[0]][n[1]] = True
        self.parents[n[0]][n[1]] = u        

    def _review_and_append_forbidden_symbols(self, goal):
        if goal == '?':
            self.forbidden_symbols.append('C')

    def search(self, start, goal):
        # preparation
        self._prepare_tracking(start)

        # algorithm loop
        while self.queue:
            u = self.queue.pop(0)
            self._review_and_append_forbidden_symbols(goal)
            neighbours = self.map_utils.get_valid_neighbours(self.game_map,self.forbidden_symbols,u)
            for n in neighbours:
                if not self.reviewed[n[0]][n[1]]:
                    self._mark_reviewed(u,n)
                    self.queue.append(n)
                    if self.game_map[n[0]][n[1]] == goal:
                        return self.map_utils.take_step(self.parents, start, n)        
        return None 

#################### GAME LOGIC #######################

num_rows, num_columns, num_rounds_to_alarm = [int(i) for i in input().split()]
game = Game(BFS, num_rows, num_columns, num_rounds_to_alarm)

# game loop
back = False
while True:
    # kr: row where Kirk is located.
    # kc: column where Kirk is located.
    kr, kc = [int(i) for i in input().split()]
    rows = []
    for i in range(num_rows):
        rows.append(input())

    if rows[kr][kc] == 'C':
        back = True

    game.strategy.update_map(rows)

    game.move_kirk(game.get_destination((kr, kc), back),kr,kc)
