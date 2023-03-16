import sys


import Ethack
from Ethack import webattack,accountattack,viewer


def main() -> None:
    
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    opts = [o for o in sys.argv[1:] if o.startswith("-")]

    # Show help message
    if "-h" in opts or "--help" in opts:
        viewer.show(__doc__)
        raise SystemExit()

  


if __name__ == "__main__":
    main()
