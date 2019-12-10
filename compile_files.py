import compileall
import os
import sys

# Get path of this file's directory
DIRECTORY = os.path.dirname(os.path.realpath(__file__))

# Check that files are can compile
SUCCESS = compileall.compile_dir(dir=DIRECTORY, maxlevels=20, force=True)

# Return appropriate exit code
if SUCCESS:
    sys.exit(0)
else:
    sys.exit(1)
