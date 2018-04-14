# genera un file che contiene un elenco di documenti smarriti/rubati di test

from optparse import OptionParser
from bz2 import BZ2File
import csv

parser = OptionParser()
parser.add_option('-f', '--file', metavar='FILE', dest='filename',
    help='output filename (default="documents")', default='documents')
parser.add_option('-c', '--count', metavar='N', dest='count', type='int',
    help='how many documents will generate (default=1000)', default=1000)
(options, args) = parser.parse_args()

fp = BZ2File(options.filename + '.csv.bz2', 'w')
c = csv.writer(fp)
for i in range(options.count):
    c.writerow(['doc%07i' % i])

