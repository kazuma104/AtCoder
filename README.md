# AtCoder

[AtCoder](https://atcoder.jp/home)（アットコーダー）とは、「**競技プログラミング**」と呼ばれるコンピュータプログラムのコンテストを行うサービス、および高橋直大が代表を務めるその運営会社を指す。[by.wiki](https://ja.wikipedia.org/wiki/AtCoder)

## AtCoder Beginner Contest (ABC)

競技プログラミング初心者/初級者向けのコンテスト．  
必ずしもABCと書かれているものだけが，Beginnerではない．  
自分はここのC~Dあたりが難しいので頑張ってもっと解けるようにする．  
**Rated対象:～1999**

* [ABC147](https://atcoder.jp/contests/abc147)
* [ABC148](https://atcoder.jp/contests/abc148)
* [三井住友信託銀行プログラミングコンテスト2019](https://atcoder.jp/contests/sumitrust2019)

## AtCoder Regular Contest (ARC)

競技プログラミング中級者/上級者向けのコンテスト．  
必ずしもARCと書かれているものだけが，Regularではない．  
やったことない．  
**Rated対象:～2799**

## AtCoder Grand Contest (AGC)

やばいやつ．  
やったことない．  
**Rated対象:ALL**

## DP(動的計画法)

DP問題はAtCoderから選んでいないものがある．[ここ](https://qiita.com/drken/items/a5e6fe22863b7992efdb)を参考させていただいた．
あと[ここ](http://wakabame.hatenablog.com/entry/2017/09/10/211428)も．  

* [DP(動的計画法)](https://qiita.com/drken/items/a5e6fe22863b7992efdb)  
* [EDPC](https://atcoder.jp/contests/dp)

## bit全探索(作成途中)

bit全探索をするためには，for文で各ビットごとに2進数のn乗でループを回す．  

【Python】

```python
# bit全探索
for i in range(2 ** n):
    for j in range(n):
        if((i >> j) & 1):
```

### 便利機能

ブランチ作成とチェックアウトを同時に

```bash
git checkout -b【ブランチ名】
```

VSCode内でmarkdownのプレビューを見る．  
[Ctrl]+[K]+[V]
