#!/usr/bin/env python3
"""Copy the pre-rendered entry image to the output directory.

The image (entry.png) was rendered offline by render.py and is shipped in
this repository. This program only copies it, so both grader runs write
identical bytes. Standard library only.
"""
import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        raise SystemExit("entry.png not found next to main.py")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
