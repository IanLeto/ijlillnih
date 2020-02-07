# -*- coding: utf-8 -*-
# @Time    : 2020/2/5 1:47 下午
# @Author  : Ian Leto
# @File    : sort.py
# 干啥的    : py 各种排序

def bubble_sort(raw_list: list) -> list:
    length = len(raw_list) - 1
    for x in range(length):
        for i in range(length - x):
            j = i + 1
            if raw_list[i] > raw_list[j]:
                raw_list[i], raw_list[j] = raw_list[j], raw_list[i]
            i += 1

    # for i in raw_list:
    #     if i > raw_list[j]:
    #         raw_list[i], raw_list[j] = raw_list[j], raw_list[i]
    #
    # while i < len(raw_list) - 1:
    #     for x in raw_list:
    #         if raw_list[i] > raw_list[j]:
    #             raw_list[i], raw_list[j] = raw_list[j], raw_list[i]
    #     i += 1
    return raw_list
