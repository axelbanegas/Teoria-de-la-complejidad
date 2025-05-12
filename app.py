from sort_methods import SortMethods
from benchmarking import Benchmarking
import random
from typing import List, Callable, Dict, Tuple
import matplotlib.pyplot as plt

class App:
    def __init__(self):
        self.tamanos = [5000, 10000, 30000, 50000, 100000]
        self.max_tamano = max(self.tamanos)
        self.arreglo_base = self.build_arreglo(self.max_tamano)
        self.algoritmos: Dict[str, Callable[[List[int]], List[int]]] = {
                "Burbuja Simple": SortMethods.sort_bubble,
                "Burbuja Optimizada": SortMethods.sort_bubble_optimized,
                "Selección": SortMethods.sort_selection,
                "Inserción": SortMethods.sort_insertion,
                "Shell Sort": SortMethods.sort_shell,
        }
        self.resultados: List[Tuple[int, str, float]] = []

    def build_arreglo(self, tamano: int) -> List[int]:
        return [random.randint(1, 100000) for _ in range(tamano)]

    def main(self):
        for tam in self.tamanos:
            sub_arreglo = self.arreglo_base[:tam]
            for nombre, algoritmo in self.algoritmos.items():
                copia = sub_arreglo.copy()
                tiempo = Benchmarking.medir_tiempo(algoritmo, copia)
                self.resultados.append((tam, nombre, tiempo))
                print(f"Tamaño: {tam}, Método: {nombre}, Tiempo: {tiempo:.6f} segundos")

        # Aquí llamamos al gráfico con los resultados
        generar_grafico(self.resultados)


def generar_grafico(resultados: List[Tuple[int, str, float]]):
    metodos = set(nombre for _, nombre, _ in resultados)
    colores = ['b', 'g', 'r', 'm', 'c', 'y', 'k']
    color_map = {metodo: colores[i % len(colores)] for i, metodo in enumerate(metodos)}

    plt.figure(figsize=(10, 6))
    for metodo in metodos:
        tamanos = [tam for tam, nombre, _ in resultados if nombre == metodo]
        tiempos = [tiempo for tam, nombre, tiempo in resultados if nombre == metodo]
        plt.plot(tamanos, tiempos, marker='o', label=metodo, color=color_map[metodo])

    plt.title("Comparación de algoritmos de ordenamiento")
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("grafico_resultados.png")
    print("Gráfico guardado como grafico_resultados.png")


if __name__ == "__main__":
    app = App()
    app.main()
