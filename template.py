"""memo（https://www.kumilog.net/entry/python-speed-comp）
    ・sorted(A)より若干A.sort()が速い(破壊的メソッドの方が良い)
    ・二次元配列や辞書をソートする場合lambdaよりoperator.itemgetterの方が速い
    　但し「from operator import itemgetter」をインポートする必要あり
    　上二つを組み合わせた速度の比較(左の方が速い)
    ・A.sort(key=itemgetter(0)) > sorted,itemgetter > sort,lambda > A = sorted(A, key=lambda x: x[0])
    ・while文よりfor文が圧倒的に速い
    ・リストの初期化は[]*Nで良い
    ・二次元配列の場合は[[]*N for _ in range(N)]
    ・リストの値参照は「インデックスが必要でない場合」for文にリストをそのまま渡す方が速い
    ・要素の追加はappendでも良い
（https://juppy.hatenablog.com/entry/2019/06/14/Python_競技プログラミング高速化tips_%28PythonでAtcoderをやる際に個）
    ・appendで使うどっとを消すと速いと書いているが遅くなった
"""

import sys
input == sys.stdin.readline

def main():
    """ここにコードを書く"""

if __name__ == '__main__':
    main()