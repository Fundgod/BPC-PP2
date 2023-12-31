from pathlib import Path

table_columns = ["ID", "Title", "Author", "Year", "Rate"]
table_columns_sizes = [100, 300, 300, 200, 75]

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)