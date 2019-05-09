#!/usr/bin/env python3.7

import subprocess
import termcolor

sections = {
    "Intro": ("introduction.tex", 500, 0.05),
    "Prep": ("preparation.tex", 2500, 0.20),
    "Impl": ("implementation.tex", 6500, 0.40),
    "Eval": ("evaluation.tex", 2000, 0.16),
    "Conc": ("conclusion.tex", 500, 0.04),
}

total_wordcount = 0
for section, (path, target, percentage) in sections.items():
    wordcount = subprocess.check_output(f"texcount -1 -sum {path}", shell=True).decode().strip()
    total_wordcount += int(wordcount)
    print(f"{section.ljust(5)}:\t{wordcount.rjust(5)}/{str(target).rjust(5)}\t({percentage * 100}%)")

target_total_wordcount = 12000
okay_string = ""
if total_wordcount < target_total_wordcount:
    okay_string = termcolor.colored("✓", "green")
else:
    okay_string = termcolor.colored("❌", "red")
print(f"Total:\t{total_wordcount}/{target_total_wordcount}\t{okay_string}")
