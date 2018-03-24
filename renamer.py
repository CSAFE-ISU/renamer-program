#! /usr/bin/env python
"""
Sequentially show all images in a folder and allow them to be renamed.

Author: Jason Saporta
Date: 3/20/2018
"""
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import os
from pathlib import Path

import matplotlib.pyplot as plt
import skimage.io as io

parser = ArgumentParser(description="Display images in a folder and " +
                        "easily rename them.",
                        formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("input_path", type=str, default=".", nargs="?",
                    help="Directory storing the files to be renamed.")
parser.add_argument("output_path", type=str, default=None, nargs="?",
                    help="Directory where renamed files will be saved.")
parser.add_argument("-e", "--ext", type=str, default="png",
                    choices=["png", "svg", "jpg", "jpeg"],
                    help="Extension of files you would like to rename.")
parser.add_argument("-r", "--replace", action="store_true",
                    help="Specify that the old files should be deleted.")
args = parser.parse_args()

input_path = Path(args.input_path)
output_path = Path(args.output_path) if args.output_path else input_path


def main():
    """Run only when this is executed from the command line."""
    print("For each image, type the new name of the file." +
          " No extension necessary!", end="\n\n")
    file_list = input_path.glob(f"*.{args.ext}")
    plt.ion()

    for pic in file_list:
        img = io.imread(str(pic))
        plt.imshow(img)
        plt.draw()
        plt.pause(0.001)
        new_name = input(
            "Please enter a new filename. Press [enter] to skip: ")
        if new_name:
            if not new_name.endswith(args.ext):
                new_name += "." + args.ext
            io.imsave(output_path / new_name, img)
            if args.replace:
                os.remove(pic)


if __name__ == '__main__':
    main()
