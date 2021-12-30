from time import ctime


def print_data(arg1):
    print("{}: {}".format(ctime()[4:-5].replace('  ', '_'), arg1))

