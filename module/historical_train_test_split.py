# default module
import os
import time
import multiprocessing
import pandas as pd
import threading


# read file
path = '../data/'
train = pd.read_csv(path + 'train.csv')
test = pd.read_csv(path + 'test.csv')
history = pd.read_csv(path + 'historical_transactions.csv')


def split_data(card_id):
    print(len(history))
    print(len(history[history.card_id == card_id]))


def main():

    # constants
    NUM_OF_PROCESSOR = int(input("please input number of processor: "))

    # train, test idx
    train_idx = train.card_id.unique()
    test_idx = test.card_id.unique()

    # processor pool
    pool = multiprocessing.Pool(processes=NUM_OF_PROCESSOR)

    # start time
    start = time.time()

    # temp = pool.map(split_data, train_idx[:100])
    # t = threading.Thread(target=split_data, args=train_idx[:100])
    # t.start()

    # execution time
    exec_time = int(time.time() - start)
    print("hour: {}, minute: {}, second: {}".format(exec_time // 3600, exec_time % 3600 // 60, exec_time % 60))

if __name__ == '__main__':
    main()
