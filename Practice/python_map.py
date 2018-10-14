import datetime, argparse

parser =  argparse.ArgumentParser(description='Network layer implementation.')
parser.add_argument('file')
args = parser.parse_args()

with open(args.file) as f:
    lines = f.read().splitlines()

print("using map\n%s" % datetime.datetime.now())
l = map(sum, lines) # constant time, couldn't find anything
# online? but it always runs in .000111 - .000200 sec
# whether it's 10,000 or 1,000,000 lines of code
print("after map\n%s" % datetime.datetime.now())


print("using loop\n%s" % datetime.datetime.now())
sum = 0
for n in lines:
    sum += 0
print("after loop\n%s" % datetime.datetime.now())
