import time
from typing import Callable, List

class Benchmarking:
    @staticmethod
    def medir_tiempo(func: Callable[[List[int]], List[int]], array: List[int]) -> float:
        inicio = time.time()
        func(array)
        fin = time.time()
        return fin - inicio
