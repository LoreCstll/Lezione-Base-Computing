import argparse
import time
import matplotlib.pyplot as plt
import pylab

start = time.time()


parser = argparse.ArgumentParser(description='Book structure.')
parser.add_argument('path',help='path to the input file')
parser.add_argument('-hist',help='display an historgramm of the result', action="count", default=0)
#parser.add_argument("-v", "--verbosity", action="count", default=0, help = 'add comments to the results')


args = parser.parse_args()


lower_var = open(args.path, "r").read().lower()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',  'z']
#count = numpy.arange(len(alphabet))

counts = list(map(lower_var.count,alphabet))
total = sum(counts)



print('letter |  freq%')
print('---------------')
for i in range(len(alphabet)):
    print(f'   {alphabet[i]}   |  {100*counts[i]/total:.2f}')
print('---------------')




if args.hist >= 1:
    plt.hist(alphabet,len(counts),weights = counts )



end = time.time()


print(f'escaled time: {end-start:.3f}')
pylab.show()
