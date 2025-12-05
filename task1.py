import argparse
import shutil
from pathlib import Path
import sys


def parse_args():
    res = argparse.ArgumentParser(description="Recursive file copying and sorting by extension.")
    res.add_argument("source", type=Path, help="Path to the source directory")
    res.add_argument("output", type=Path, nargs="?", default=Path("dist"), help="Path to the destination directory (default is 'dist')")

    return res.parse_args()

def copy_file(file_path: Path, output_base: Path):
    try:
        ext = file_path.suffix[1:] if file_path.suffix else "others"
        
        target_dir = output_base / ext
        target_dir.mkdir(parents=True, exist_ok=True)
        
        target_file = target_dir / file_path.name
        
        shutil.copy2(file_path, target_file)
        print(f"[ok] Copied: {file_path} -> {target_file}")
        
    except PermissionError:
        print(f"[err] Access denied: {file_path}")
    except Exception as e:
        print(f"[err] Error copying {file_path}: {e}")

def read_folder(path: Path, output_base: Path):
    try:
        if not path.exists():
            print(f"[err] Path {path} does not exist.")
            return

        for item in path.iterdir():
            if item.is_dir():
                read_folder(item, output_base)
            elif item.is_file():
                copy_file(item, output_base)
                
    except PermissionError:
        print(f"[err] Access denied: {path}")
    except Exception as e:
        print(f"[err] Unexpected error in {path}: {e}")

def main():
    args = parse_args()
    
    source_path = args.source
    output_path = args.output

    print(f"Starting from '{source_path}' to '{output_path}'\n")
    read_folder(source_path, output_path)
    print("Done!")

if __name__ == "__main__":
    main()