import sys

sys.stderr.write('This is a stderr text\n')
sys.stderr.flush()

sys.stdout.write('This is a stdout text\n')

print(sys.argv)
