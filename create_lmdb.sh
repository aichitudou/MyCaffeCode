#!/usr/bin/env sh
rm -rf img_train_lmdb
../build/tools/convert_imageset \
--resize_height=256 --resize_width=256 \
/ train.txt img_train_lmdb 
