#!/bin/bash
#install VSCode extension coverage gutters to display test code coverage with this script

# Run tests with coverage
coverage run -m unittest discover -s test

# Generate XML coverage report
coverage xml

# Optional: Notify Coverage Gutters in VS Code (if using VS Code)
# code --goto coverage.xml
