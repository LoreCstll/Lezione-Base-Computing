import argparse
parser = argparse.ArgumentParser(description='Book structure.')
parser.add_argument('path',help='path to the input file')
#parser.add_argument("-v", "--verbosity", action="count", default=0, help = 'add comments to the results')
args = parser.parse_args()
var_lettura = open(args.path, "r").read()
lower_var = var_lettura.lower()
#count = lower_var.count("a")
#print(count)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',  'z']


for i in alphabet:
   print('La lettera %s è ripetuta %i nel libro' %(i,lower_var.count(i)))
   
