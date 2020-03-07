"""Welcome to randomix.

This is the entry point of the application.
"""
import os

import argparse
import logging
import logging.config

import numpy as np
from scipy import stats

import embeddix

import randomix.utils.config as cutils
import randomix.utils.files as futils

logging.config.dictConfig(
    cutils.load(
        os.path.join(os.path.dirname(__file__), 'logging', 'logging.yml')))

logger = logging.getLogger(__name__)


def get_truncated_normal(mean=0, sd=1, low=0, upp=10):  # pylint: disable=invalid-name
    """Return refactored scipy-based truncated normal."""
    return stats.truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)


def _generate_model(vocab, rtype, dim, normloc=None, normscale=None):
    if rtype not in ['uniform', 'normal']:
        raise Exception('Unsupported rtype: {}'.format(type))
    if rtype == 'uniform':
        return np.random.uniform(-1, 1, [len(vocab), dim])
    if rtype == 'normal':
        if normloc is None or normscale is None:
            raise Exception('Unspecified normloc/normscale parameters')
        distrib = get_truncated_normal(mean=normloc, sd=normscale, low=-1,
                                       upp=1)
        return distrib.rvs((len(vocab), dim))
    return


def _generate(args):
    vocab = embeddix.load_vocab(args.vocab)
    model = _generate_model(vocab, args.rtype, args.dim, args.normloc,
                            args.normscale)
    vocab_dirpath = os.path.dirname(args.vocab)
    output_filepath = futils.get_output_filepath(
        vocab_dirpath, args.rtype, args.dim, args.normloc, args.normscale)
    if 'text' in args.output:
        embeddix.save_to_text(vocab, model, '{}.txt'.format(output_filepath))
    if 'numpy' in args.output:
        embeddix.save_to_numpy(vocab, model, output_filepath)


def restricted_normscale(x):  # pylint: disable=invalid-name
    """Ensure --normscale is > 0."""
    x = float(x)
    if x < 0.:
        raise argparse.ArgumentTypeError('{} --normscale < 0'.format(x))
    return x


def restricted_normloc(x):  # pylint: disable=invalid-name
    """Ensure --normloc is in [-1, 1]."""
    x = float(x)
    if x < -1. or x > 1.:
        raise argparse.ArgumentTypeError('{} --normloc not in range [-1, 1]'
                                         .format(x))
    return x


def main():
    """Launch randomix."""
    parser = argparse.ArgumentParser(prog='randomix')
    subparsers = parser.add_subparsers()
    parser_generate = subparsers.add_parser(
        'generate', formatter_class=argparse.RawTextHelpFormatter,
        help='generate random vectors for input vocabulary')
    parser_generate.set_defaults(func=_generate)
    parser_generate.add_argument('-v', '--vocab', required=True,
                                 help='input vocabulary in word\tid format')
    parser_generate.add_argument('-t', '--rtype', required=True,
                                 choices=['uniform', 'normal'],
                                 help='type of random distribution to use')
    parser_generate.add_argument('-d', '--dim', required=True, type=int,
                                 help='dimensions of the vectors to generate')
    parser_generate.add_argument('--normloc', type=restricted_normloc,
                                 help='mean of --randtype normal '
                                      'distribution. Should be in [-1, 1]')
    parser_generate.add_argument('--normscale', type=restricted_normscale,
                                 help='std of --randtype normal distribution. '
                                      'Should be > 0')
    parser_generate.add_argument('-o', '--output', required=True, nargs='+',
                                 choices=['text', 'numpy'],
                                 help='type of random distribution to use')
    args = parser.parse_args()
    args.func(args)
