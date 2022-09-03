import sys
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--filename', type=str, default='test1')
parser.add_argument('--layout', type=int, default=6)
parser.add_argument('--binarization', action='store_true', help='Add to binarize image manually.')


def get_args():
    opts = parser.parse_args()
    return opts