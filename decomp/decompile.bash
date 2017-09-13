#!/bin/bash
for d in */; do
  echo "$d"
	uncompyle6 -o $d $d/*.pyc
done
