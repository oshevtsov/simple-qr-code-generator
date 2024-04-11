#!/usr/bin/env python
from argparse import ArgumentParser

import segno


def parse_args():
    parser = ArgumentParser(description="Generate QR code from the input string")
    parser.add_argument("input", type=str, help="Input string to generate QR code for")
    parser.add_argument(
        "-s",
        "--scale",
        type=float,
        default=5,
        help="Output image scale",
    )
    parser.add_argument(
        "-b",
        "--border",
        type=int,
        help="Output image border (aka quiet zone)",
    )
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        default="svg",
        help="Output image format",
    )
    parser.add_argument(
        "-o",
        "--out",
        type=str,
        default="out",
        help="Output image name (without extension)",
    )
    parser.add_argument(
        "-u",
        "--unit",
        type=str,
        default="cm",
        choices=["em", "ex", "px", "pt", "pc", "cm", "mm"],
        help="Output image format",
    )
    return parser.parse_args()


def generate_qr(args):
    qr_code = segno.make_qr(args.input)
    qr_code.save(
        f"{args.out}.{args.format}",
        border=args.border,
        scale=args.scale,
        unit=args.unit,
    )


def main():
    args = parse_args()
    generate_qr(args)


if __name__ == "__main__":
    main()
