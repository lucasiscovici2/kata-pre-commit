import pandas as pd
from typing import Union


from pathlib import Path
def import_file(filename: Union[str, Path]   ) -> 			pd.DataFrame:
	return 			pd.read_csv(			filename)