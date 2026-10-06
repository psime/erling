import runpy
from pathlib import Path


def main():
    print("Hello from erling!")
    runpy.run_path(str(Path(__file__).parent / "src" / "athletic_shotmap_erling.py"), run_name="__main__")


if __name__ == "__main__":
    main()
