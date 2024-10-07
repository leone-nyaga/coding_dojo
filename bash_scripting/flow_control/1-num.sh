#!/bin/bash

x=3
if [ "$x" -gt 5 ]; then
	echo "The number is greater than 5"
elif [ "$x" -eq 5 ]; then
	echo "The number is equal to 5"
else
	echo "The number is not equal to 5"
fi
