# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 6:41 下午
# @Author  : Ian Leto
# @File    : stra.py
# 干啥的    : 策略模式

import os


class Output:
    def __init__(self, strategy):
        self.strategy = strategy

    def output(self):
        raise NotImplementedError()


class StrategyOutputByFile:
    def __init__(self, file_path: str, content, file_name: str):
        self.file_path = file_path
        self.content = content
        self.file_name = file_name

    def output(self) -> (str, bool):
        try:
            with open(self.file_path, 'w') as f:
                f.write(self.content)
        except IOError as e:
            raise IOError("file to write file {0} ,{1} by {2}".format(self.file_path, self.file_name, e))
        except Exception as e:
            raise Exception("unknown err {0}".format(e), )

        return os.path.join(), True


class StrategyOutputNormal:
    def __init__(self, content):
        self.content = self.content

    def output(self) -> (str, bool):
        return self.content, True


class StrategyDefault:
    def __init__(self, content):
        self.content = content

    def output(self) -> (str, bool):
        return self.content, True


class OutputContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def output(self):
        return self.strategy.output()


if __name__ == '__main__':
    if 1 == 1:
        output_stra = OutputContext(StrategyDefault("11"))
    print(output_stra.output())
