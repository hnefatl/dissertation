#!/bin/bash

wordcount=0

for file in $(ls *.tex | grep -Ev "proposal.tex|declarationoriginality.tex|proforma.tex") ; do
    wordcount=$(($wordcount + $(texcount "$file" | head -n3 | tail -n1 | awk '{print $4}')))
done

echo $wordcount
