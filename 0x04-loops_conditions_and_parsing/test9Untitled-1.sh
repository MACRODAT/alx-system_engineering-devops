#!/usr/bin/env bash

i=0
for i in {1..100}; do
	if (( i % 3 == 0)); then
		echo "Fizz"
	else
		echo "$i"
	fi
done
