import sys
import json


def main():
    args = sys.argv
    if len(args) <= 1:
        print("Argument Error.")
    else:
        json_tree(args[1])


def json_tree(target_file):
    f = open(target_file, 'r')
    target_data = json.load(f)
    print_for(target_data, depth=4)
    f.close()


def print_for(data, depth=0, current=0):
    """再帰的にtree構造のキーのみを表示する
    Args:
        data (str): 対象データ
        depth (int): 表示したいネストの深さ
        current (int): データのrootからのネストの深さを格納
    """
    if depth == 0:
        return
    else:
        depth -= 1
        current += 1
        for key in data:
            whitespace = " "
            for i in range(current):
                whitespace += "   "
            output = whitespace + key
            print(output)
            print_for(data[key], depth, current)


if __name__ == '__main__':
    main()
