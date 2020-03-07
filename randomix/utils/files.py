"""Files utils."""
import os

__all__ = ('get_output_filepath')


def get_output_filepath(vocab_dirpath, rtype, dim, normloc=None,
                        normscale=None):
    """Return absolute path to output file."""
    if rtype not in ['uniform', 'normal']:
        raise Exception('Unsupported rtype: {}'.format(type))
    otp_fp = os.path.join(vocab_dirpath, 'rand-d{}-{}'.format(dim, rtype))
    if rtype == 'normal':
        if not normloc or not normscale:
            raise Exception('Unspecified normloc/normscale parameters')
        otp_fp = '{}-m{}-s{}'.format(otp_fp, normloc, normscale)
    return '{}.txt'.format(otp_fp)
