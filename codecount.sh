#!/bin/bash

shopt -s globstar
compiler_size=$(wc -l ../compiler/**/*.hs | tail -n1 | awk '{print $1}')

cd ../hs-java
hs_java_size=$(git log --author=hnefatl --pretty=tformat: --numstat | gawk '{ total += $1 - $2; } END { printf "%s\n", total }' -)
cd ../haskell-src
haskell_src_size=$(git log --author=hnefatl --pretty=tformat: --numstat | gawk '{ total += $1 - $2; } END { printf "%s\n", total }' -)

echo "$((compiler_size + hs_java_size + haskell_src_size))"