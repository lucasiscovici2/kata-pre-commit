import pandas as pd
import numpy as np
from typing import List, Tuple
def volume(longueur:float, largeur, hauteur:float ):
	return longueur*largeur*	\
	hauteur





import numpy as np
def total_volume(pieces: List[Tuple[float, float,float]]) -> float:
	pi = np.pi
	return np.sum([volume(longueur, largeur, hauteur) for longueur, largeur, hauteur in pieces] )


def calculations(a: int, b: int, c: int, d: bool) -> List[float]:
    res: List[float] = []
    if a < b**2:
        if b > c**2:
            if d == True:
                for i in range(b):
                    for j in range(a):
                        for j in range(a**2):
                            res.append(1 if b + c > a + c * 2 else 2)
            elif not d and b - c**2 > a:
                for i in range(b):
                    for j in range(a):
                        for j in range(a**2):
                            res.append(2 if b + c > a + c * 2 else 3)
            else:
                for i in range(b):
                    for j in range(a):
                        res.append(6 if b * c > a * c * 2 else 0)
        else:
            if d:
                for i in range(b):
                    for j in range(a):
                        res.append(b**2)
            else:
                for i in range(b):
                    for j in range(a):
                        res.append(b * c**2)
    else:
        for i in range(b):
            for j in range(a):
                res.append(b**2 if d else a**2)
    return res