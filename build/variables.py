from pathlib import Path

table_columns = ["ID", "Title", "Author"]

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\fundg\Desktop\prog\projects\BPC-PP2\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)