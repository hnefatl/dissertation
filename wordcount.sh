#!/bin/bash

texcount dissertation.tex | head -n3 | tail -n1 | awk '{print $4}'
