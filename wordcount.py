#!/usr/bin/env python3.7

import subprocess

sections = {
    "Intro": ("introduction.tex", 500, 0.05),
    "Prep": ("preparation.tex", 2500, 0.20),
    "Impl": ("implementation.tex", 4500, 0.40),
    "Eval": ("evaluation.tex", 2000, 0.16),
    "Conc": ("conclusion.tex", 500, 0.04)
}

for section, (path, target, percentage) in sections.items():
    wordcount = subprocess.check_output(f"texcount {path} | head -n3 | tail -n1 | awk '{{print $4}}'", shell=True).decode().strip()
    print(f"{section.ljust(5)}:\t{wordcount.rjust(5)}/{str(target).rjust(4)}\t({percentage * 100}%)")
