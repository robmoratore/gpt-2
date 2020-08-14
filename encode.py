#!/usr/bin/env python3
# Usage:
#  PYTHONPATH=src ./encode.py <file|directory|glob> /path/to/output.npz
#  PYTHONPATH=src ./train --dataset /path/to/output.npz

import sys, os
sys.path.extend([f'./{name}' for name in os.listdir(".") if os.path.isdir(name)])

import argparse
import numpy as np

from load_dataset import load_dataset
import encoder

parser = argparse.ArgumentParser(
    description='Pre-encode text files into tokenized training set.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--models_dir', metavar='MODELDIR', type=str, default='models', help='Pretrained model directory')
parser.add_argument('--model_name', metavar='MODEL', type=str, default='124M', help='Pretrained model name')
parser.add_argument('--combine', metavar='CHARS', type=int, default=50000, help='Concatenate files with <|endoftext|> separator into chunks of this minimum size')
parser.add_argument('--encoding', type=str, default='utf-8', help='Set the encoding for reading and writing files.')
parser.add_argument('in_text', metavar='PATH', type=str, help='Input file, directory, or glob pattern (utf-8 text).')
parser.add_argument('out_npz', metavar='OUT.npz', type=str, help='Output file path')

def main():
    args = parser.parse_args()
    enc = encoder.get_encoder(args.model_name, args.models_dir)
    print('Reading files')
    chunks = load_dataset(enc, args.in_text, args.combine, encoding=args.encoding)
    print('Writing', args.out_npz)
    np.savez_compressed(args.out_npz, *chunks)


if __name__ == '__main__':
    main()
