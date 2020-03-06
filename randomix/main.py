"""Welcome to randomix.

This is the entry point of the application.
"""
import os

import argparse
import logging
import logging.config

import randomix.utils.config as cutils

logging.config.dictConfig(
    cutils.load(
        os.path.join(os.path.dirname(__file__), 'logging', 'logging.yml')))

logger = logging.getLogger(__name__)


def _generate():
    pass


def main():
    """Launch entropix."""
    parser = argparse.ArgumentParser(prog='entropix')
    subparsers = parser.add_subparsers()
    parser_generate = subparsers.add_parser(
        'generate', formatter_class=argparse.RawTextHelpFormatter,
        help='generate random vectors for input vocabulary')
    parser_generate.set_defaults(func=_generate)
    parser_generate.add_argument('-c', '--corpus', required=True,
                                 help='an input .txt corpus to compute \
                                 counts on')
    parser_generate.add_argument('-o', '--output',
                                 help='absolute path to output directory. '
                                 'If not set, will default to corpus dir')
    parser_generate.add_argument('-m', '--min-count', default=0, type=int,
                                 help='frequency threshold on vocabulary')
    parser_generate.add_argument('-w', '--win-size', default=2, type=int,
                                 help='size of context window')
    parser_generate.add_argument('-i', '--with-info', action='store_true',
                                 help='Whether or not to use informativeness')
    parser_generate.add_argument('-f', '--info-model',
                                 help='Absolute path to gensim cbow model')
    parser_generate.add_argument('-n', '--num-threads', type=int, default=1,
                                 help='number of threads to use for parallel '
                                      'processing with informativeness only')
    args = parser.parse_args()
    args.func(args)
