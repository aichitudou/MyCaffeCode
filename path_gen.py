# -*- coding: utf-8 -*-

import os
import sys
import argparse
import numpy as np

# current_path = os.path.abspath(os.path.dirname(__file__))

# 3：1 =》 neg:pos merge
def merge_file(file1, file2, file3):

    f1 = open(file1)
    f2 = open(file2)
    f3 = open(file3, "w")

    arr1 = []   # positive
    arr2 = []   # negtive

    for line1 in f1.readlines():
        arr1.append(line1)
    for line2 in f2.readlines():
        arr2.append(line2)

    for i in range(len(arr1) / 32 + 1):
        if (i+1)*32 > len(arr1):
            j = len(arr1)
            l = len(arr2)
        else:
            j = (i+1)*32
            l = (i+1)*64
        for k in range(i*32, j):
            f3.write(arr1[k])

        for b in range(i*64, l):
            f3.write(arr2[b])

    f1.close()
    f2.close()
    f3.close()
    print('All images path and class index has been merged!')


def generate_train_images_path(train_path):
    pos = train_path + '/positive'
    neg = train_path + '/negative'

    train_pos_txt = open('train_pos.txt', 'w+')
    train_neg_txt = open('train_neg.txt', 'w+')


    all_train_pos_lines = []
    all_train_neg_lines = []
    for fn in os.listdir(pos):
        filepath = os.path.join(pos, fn)
        if os.path.isdir(filepath):
            for root, dirs, files in os.walk(filepath):
                 if files:
                     for file in files:
                         imagefilepath = os.path.join(root, file)
    #                    print('{0} {1}'.format(imagefilepath, class_index_dict[fn]))
                         all_train_pos_lines.append(imagefilepath + ' ' + '0' + '\n')
    # if is_shuffle:
    #     np.random.shuffle(all_train_pos_lines)
    #     for line in all_train_pos_lines:
    #         train_pos_txt.write(line)
    # else:
    for line in all_train_pos_lines:
        train_pos_txt.write(line)

    for root, dirs, files in os.walk(neg):
        if files:
            for file in files:
                imagefilepath = os.path.join(root, file)
                all_train_neg_lines.append(imagefilepath + ' ' + '1' + '\n')

    for line in all_train_neg_lines:
        train_neg_txt.write(line)

    train_pos_txt.close()
    train_neg_txt.close()

    print('All train images path and class index has been saved into train.txt!')


def generate_val_images_path(train_path):
    pos = train_path + '/positive'
    neg = train_path + '/negative'

    train_pos_txt = open('val_pos.txt', 'w+')
    train_neg_txt = open('val_neg.txt', 'w+')


    all_train_pos_lines = []
    all_train_neg_lines = []
    for fn in os.listdir(pos):
        filepath = os.path.join(pos, fn)
        if os.path.isdir(filepath):
            for root, dirs, files in os.walk(filepath):
                 if files:
                     for file in files:
                         imagefilepath = os.path.join(root, file)
    #                    print('{0} {1}'.format(imagefilepath, class_index_dict[fn]))
                         all_train_pos_lines.append(imagefilepath + ' ' + '0' + '\n')
    # if is_shuffle:
    #     np.random.shuffle(all_train_pos_lines)
    #     for line in all_train_pos_lines:
    #         train_pos_txt.write(line)
    # else:
    for line in all_train_pos_lines:
        train_pos_txt.write(line)

    for root, dirs, files in os.walk(neg):
        if files:
            for file in files:
                imagefilepath = os.path.join(root, file)
                all_train_neg_lines.append(imagefilepath + ' ' + '1' + '\n')

    for line in all_train_neg_lines:
        train_neg_txt.write(line)

    train_pos_txt.close()
    train_neg_txt.close()

    print('All val images path and class index has been saved into val.txt!')





if __name__ == '__main__':
    current_path = os.getcwd()
    train_path = current_path + "/train"
    val_path = current_path + "/val"

   # generate_train_images_path(train_path)
    # make some operation, delete the last line of train_pos.txt and delete train_neg.txt to 10236 lines
    # then
    merge_file('train_pos.txt', 'train_neg.txt', 'train.txt')

   # generate_val_images_path(val_path)
    # make some operation, delete the last line of train_pos.txt and delete train_neg.txt to 10236 lines
    # then
    merge_file('val_pos.txt', 'val_neg.txt', 'val.txt')

