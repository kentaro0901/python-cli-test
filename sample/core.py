import logging
import argparse
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(
    prog='samplecli', # プログラムの名称
    usage='how to use', # 利用方法
    description='test cli', # 説明
)
parser.add_argument('arg1', help='help')

def main(argv=sys.argv):
    if len(argv) == 1:
        parser.parse_args(["-h"])
        sys.exit(0)
    
    args = parser.parse_args()

    if args.arg1 == 'u':
        logger.info('Hello World!')
    else:
        logger.info('hello world!')