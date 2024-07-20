import math
from typing import Tuple

from HapticsBase import HapticsBase


class ImpactEffect(HapticsBase):
    '''
    Creates an impact effect based on the provided parameters
    '''
    def __init__(self):
        super().__init__()

    def _get_distance(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    def _print_matrix(matrix):
        for row in matrix:
            print(' '.join(str(int(x)) for x in row))

    def _matrix_to_pattern(self, matrix: list):
        pattern = []
        for x, row in enumerate(matrix):
            for y, intensity in enumerate(row):
                pattern.append({"index": x * 4 + y, "intensity": intensity})
        return pattern

    def GetPattern(
            self, 
            base_intensity: int,
            decay_factor: float,
            effect_center: Tuple[float, float],
            effect_frames: int,
            matrix_length_y: int = 4,
            matrix_length_x: int = 5,
        ) -> dict:
        '''
        Generates an impact pattern
        '''
        pattern = []

        dot_matrix = [[base_intensity for _ in range(matrix_length_y)] for _ in range(matrix_length_x)]

        #print_matrix(dot_matrix)

        for _ in range(effect_frames):
            for x in range(matrix_length_y):
                for y in range(matrix_length_x):
                    distance = self._get_distance(x, y, effect_center[0], effect_center[1])
                    dot_matrix[y][x] = max(dot_matrix[y][x] - (decay_factor * distance), 0)
            
            #print("-" * 10)
            #print_matrix(dot_matrix)
            pattern.append({"front": self._matrix_to_pattern(dot_matrix), "back": []})

        return pattern