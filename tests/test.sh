#!/bin/bash
mkdir -p /logs/verifier

# Run the test suite
pytest /tests/test_parser.py

if [ $? -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi