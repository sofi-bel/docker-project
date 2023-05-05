#!/bin/bash

sleep 1

find . -type f -name "*.py" -print0 | xargs -0 black --check -v
status=$?

if [ $status -eq 0 ]
then
   echo "Black: PASSED"
  exit 0
else
  echo "Black: FAILED"
  exit 1
fi
