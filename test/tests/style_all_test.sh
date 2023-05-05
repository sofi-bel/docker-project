#!/bin/bash

sleep 1

find . -type f -name "*.py" -print0 | xargs -0 pylint  \
--output-format="colorized" \
--msg-template="{C}: {line}: {msg} ({symbol})" \
--evaluation="10.0 -((float(5 * error + warning + refactor + convention) / statement) * 10)" \
--score="yes"
status=$?

if [ $status -eq 0 ]
then
  echo "Pylint: PASSED"
  exit 0
else
  echo "Pylint: FAILED"
  exit 1
fi
