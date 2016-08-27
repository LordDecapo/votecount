import json
import argparse

parser = argparse.ArgumentParser(description='An assembler for the Minora CPU\
        \ emulator')
parser.add_argument('Candidates', metavar='Candidates',  type=str,
        help='text file containing a list of Candidates.')
parser.add_argument('Votes', metavar='Votes', type=str,
        help="Copy Paste file of all votes")

args = parser.parse_args()
cand = args.Candidates
vote = args.Votes

config = open(cand, 'r')
source = open(vote, 'r')
results = open('results.txt', 'w+')
res = {}

for i in config:
    tok = i.strip('\n')
    res[tok] = 0
print(res)

for i in source:
    tok = i.strip('\n').split()
    res[tok[0]] += int(tok[1])

#x = ' '
#results.write(str(x.join(res)))
json.dump(res, results)

source.close()
config.close()
results.close()
