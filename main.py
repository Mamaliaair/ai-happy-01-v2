# A make.fun ai-happy-01 entry (Python 3.13, standard library only).
# The image beside this file is the entry: a golden retriever puppy and a
# small orange kitten snuggled together cheek to cheek in warm golden
# sunlight, both with soft happy relaxed expressions. The program copies
# it to /output/entry.png.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)
shutil.copyfile(
    os.path.join(os.path.dirname(__file__), "entry.png"),
    os.path.join(OUTPUT_DIR, "entry.png"),
)
