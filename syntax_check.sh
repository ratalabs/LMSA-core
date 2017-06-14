#!/bin/sh

if python -m py_compile ~/Desktop/git/PIRT_ASU/blackboard_automation/tests.py; then
  echo "Exit code of 0: tests.py  --- SUCCESS"
else
  echo "Exit code of $?, tests.py --- FAILURE"
fi

if python -m py_compile ~/Desktop/git/PIRT_ASU/blackboard_automation/assignments.py; then
  echo "Exit code of 0: assignments.py  --- SUCCESS"
else
  echo "Exit code of $?, assignments.py --- FAILURE"
fi
