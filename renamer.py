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
import shutil
import scipy
from scipy import ndimage
import pandas as pd

parser = ArgumentParser(description="Display images in a folder and " +
                        "easily rename them.",
                        formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("input_path", type=str, default=".", nargs="?",
                    help="Directory storing the files to be renamed.")
parser.add_argument("output_path", type=str, default=None, nargs="?",
                    help="Directory where renamed files will be saved.")
parser.add_argument("-e", "--ext", type=str, default="png",
                    choices=["png", "svg", "jpg", "jpeg", "JPG"],
                    help="Extension of files you would like to rename.")
parser.add_argument("-r", "--replace", action="store_true",
                    help="Specify that the old files should be deleted.")
parser.add_argument("-v", "--vinyl", action="store_true",
                    help="Specify if the program will be used for renaming vinyl pictures.")
args = parser.parse_args()

input_path = Path(args.input_path)
output_path = Path(args.output_path) if args.output_path else input_path


def get_vinyl_name():
    confirm = "n"
    users = ["hanrahan", "kruse", "boekhoff",
             "swart", "pashek", "bryson"]
    print("\n")
    print(pd.DataFrame({'user':users, 'code':[1, 2, 3, 4, 5, 6]}))
    while confirm != "y":
        print("\n")
        print("Please enter the following information:", end = "\n")
        prt = input("Participant (six digits): ")
        side = input("Side (L or R): ") + "_"
        date = input("Date (YMD, e.g., 20180131): ") + "_"
        rep = "7_" + input("Replicate (1 or 2): ") + "_1_"
        usr1 =  users[int(input("User 1 (1-6): ")) - 1] + "_"
        usr2 =  users[int(input("User 2 (1-6): ")) - 1]
        vin_name = prt + side + date + rep + usr1 + usr2
        print("Proposed name: " + vin_name)
        confirm = input("Is the name correct (y/n)? ")
    return vin_name
    
def main():
    """Run only when this is executed from the command line."""
    print("For each image, type the new name of the file." +
          " No extension necessary!", end="\n\n")
    file_list = input_path.glob(f"*.{args.ext}")
    plt.ion()

    for pic in file_list:
        img = io.imread(str(pic))
        plt.imshow(ndimage.rotate(img, 90))
        plt.draw()
        plt.pause(0.001)
        if args.vinyl:
            new_name = get_vinyl_name()
        else:
            print("\n")
            new_name = input(
                "Please enter a new filename. Press [enter] to skip: ")
        if new_name:
            if not new_name.endswith(args.ext):
                new_name += "." + args.ext
                # io.imsave(output_path / new_name, img)
                shutil.copyfile(pic, output_path / new_name)
            if args.replace:
                os.remove(pic)


if __name__ == '__main__':
    main()
