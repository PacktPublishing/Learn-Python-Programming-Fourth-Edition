# railway-project/src/railway_cli/__main__.py
import sys
from . import cli

sys.argv[0] = f"python -m {__package__}"
cli.main()
