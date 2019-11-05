# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 11:00
# @Author  : Ian Leto
# @File    : pyNote.py
# 干啥的    : python 注释语法


# python 注释demo
def python_note_demo(text: str, i: 'int>100' = 1100) -> str:
    print(text, i)
    # idea 会检查这里的注释
    # 不符合条件会warn but 仍会执行
    return i


def main():
    #
    python_note_demo(1, 1000)


if __name__ == '__main__':
    main()
