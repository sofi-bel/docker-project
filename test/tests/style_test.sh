#!/bin/bash

sleep 1

find . -type f -name "*.py" -print0 | xargs -0 pylint --rcfile=./tests/.pylintrc
status=$?

if [ $status -eq 0 ]
then
  echo "Pylint: PASSED"
  exit 0
else
  echo "Pylint: FAILED"
  exit 1
fi
