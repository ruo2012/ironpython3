"""Basic pip uninstallation support, helper for the Windows uninstaller"""

import argparse
import ensurepip


def main():
    parser = argparse.ArgumentParser(prog="python -m ensurepip._uninstall")
    parser.add_argument(
        "--version",
        action="version",
        version="pip {}".format(ensurepip.version()),
        help="Show the version of pip this will attempt to uninstall.",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="count",
        default=0,
        dest="verbosity",
        help=("Give more output. Option is additive, and can be used up to 3 "
              "times."),
    )

    args = parser.parse_args()

    ensurepip._uninstall(verbosity=args.verbosity)


if __name__ == "__main__":
    main()