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
parser.add_argument('-u', '--upper', help='to upper', action='store_true') # 設定するとtrue
# parser.add_argument('arg1', help='help') # 位置引数

def main(argv=sys.argv):    
    args = parser.parse_args()

    if args.upper:
        logger.info('Hello World!')
    else:
        logger.info('hello world!')