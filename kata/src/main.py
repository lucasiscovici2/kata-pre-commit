from pathlib import Path
from calculations import total_volume
from data import import_file
from viz import viz_volumes



def   run_volume(filename:   str, settings_id: int = 0) -> None:
	df =import_file(filename)
	settings = {0: "home_id", 1: "maison_ID",2:"ID", 3:"id", 0:"maison_id"}
	volumes = df.groupby(settings.get(settings_id,0)).apply(lambda x:total_volume(x.drop(columns=["maison_id"],axis=1).to_records(index=False)))
	print(volumes)

	img = 	viz_volumes(volumes)


def main() -> None:
	run_volume(Path(__file__).parent / ".." / "data" / "maisons.csv")
if __name__ == '__main__':
	main()