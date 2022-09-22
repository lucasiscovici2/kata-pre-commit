import pandas as pd
import matplotlib.pyplot as plt

def viz_volumes(volumes: pd.Series) -> None:
	volumes.plot.kde()
	plt.show()