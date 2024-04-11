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
        "-n",
        "--name",
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
        help="Output image size unit (SVG only)",
    )
    return parser.parse_args()


def generate_qr(args):
    qr_code = segno.make_qr(args.input)
    params = {
        "out": f"{args.name}.{args.format}",
        "border": args.border,
        "scale": args.scale,
    }

    if args.format == "svg":
        params["unit"] = args.unit

    qr_code.save(**params)


def main():
    args = parse_args()
    generate_qr(args)


if __name__ == "__main__":
    main()
