#!/usr/bin/env python3

# Parser for command-line options, arguments and sub-commands:
# https://docs.python.org/3/library/argparse.html
import argparse

from dprs.default_variables import DEFAULT_ARCHITECTURE_OPTIONS, DEFAULT_ARCHITECTURE, DEFAULT_MIRROR_URL, \
    DEFAULT_NUMBER, DEFAULT_OUTPUT_DIR


def cli_arg_parser():
    """
    Command-line Interface Arguments Parser
    """
    parser = argparse.ArgumentParser(
        description=(
            "Debian Repository Package Statistics (DRPS) Tool "
            "Tool takes the architecture (amd64, arm64, mipsel etc.) as an argument, "
            "and downloads the compressed Contents file associated with it from a Debian mirror. "
            "The program will parse the file, "
            "and output the statistics of the top 10 packages that have the most files associated with them. "
        )
    )
    parser.add_argument(
        "architecture",
        type=str,
        choices=DEFAULT_ARCHITECTURE_OPTIONS,
        default=DEFAULT_ARCHITECTURE,
        nargs="?",
        help=(
            "The architecture type of the Contents-*.gz file in the Debian repository. "
            "Options: " + DEFAULT_ARCHITECTURE_OPTIONS.__str__()
        )
    )
    parser.add_argument(
        "-c",
        "--clean",
        action="store_true",
        help=(
            "Clean the outputs folder. "
            "This operation can not be irreversible. "
            "Default value: False "
        )
    )
    parser.add_argument(
        "-m",
        "--mirror_url",
        type=str,
        default=DEFAULT_MIRROR_URL,
        help=(
            "Debian Package Repository Mirror URL. "
            "Default value: " + DEFAULT_MIRROR_URL
        )
    )
    parser.add_argument(
        "-n",
        "--number",
        type=int,
        default=DEFAULT_NUMBER,
        help=(
            "Number of the top packages to show. "
            "Use -1 to show all packages. "
            "Default value: " + DEFAULT_NUMBER.__str__()
        )
    )
    parser.add_argument(
        "-o",
        "--output_dir",
        type=str,
        default=DEFAULT_OUTPUT_DIR,
        help=(
            "Directory to store downloaded contents. "
            "Default value: " + DEFAULT_OUTPUT_DIR
        )
    )
    parser.add_argument(
        "-p",
        "--use_profiler",
        action="store_true",
        help=(
            "Uses cProfile for debugging purpose. "
            "Default value: False "
        )
    )
    parser.add_argument(
        "-r",
        "--reuse_contents_file",
        action="store_true",
        help=(
            "Reuses Contents-*.gz file if it exists in the output directory. "
            "Default value: True "
        )
    )
    parser.add_argument(
        "-s",
        "--sort_descending",
        action="store_true",
        help=(
            "Sort package statistics by descending order. "
            "Default value: True "
        )
    )
    parser.add_argument(
        "-u",
        "--include_udeb",
        action="store_true",
        help=(
            "Include udeb file for the given architecture. "
            "Default value: False "
        )
    )
    return parser.parse_args()
