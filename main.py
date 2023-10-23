# This is a sample Python script.




import collections, sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            if line.strip():
                n = list(map(int, line.split(';')[1].split(',')))
                print(sum(n) - (len(n) - 1) * (len(n) - 2) // 2)


