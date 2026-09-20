import math
import random as rd
import wfdb
import numpy as np
import matplotlib as mpl

def main():
    record = wfdb.rdrecord('100', pn_dir='mitdb')
    wfdb.plot_wfdb(record=record, title='Example signals')


if __name__ == "__main__":
    main()