import operator
import argparse

parser = argparse.ArgumentParser(description='Vote counter for ORE Election')
parser.add_argument('Votes', metavar='Votes', type=str,
        help="Copy Paste file of all votes")

args = parser.parse_args()
vote = args.Votes
votes = open(vote, 'r')
results = open('results.txt', 'w+')
res = {}

for i in votes.readlines():
    v = i.strip('\n').split()
    if v[0] not in res.keys():
        res[v[0]] = int(v[1])
    res[v[0]] += int(v[1])

res = sorted(res.items(), key=operator.itemgetter(1))
res.reverse()
    
for x in res:
    results.write(x[0]+ " : "+str(x[1])+"\n")

votes.close()
results.close()
