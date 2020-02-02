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
DP問題はAtCoderの問題から選んでいないものがあるが一応載せておく．  
下のDP(動的計画法)はとてもためになる（やばい）．その派生サイトも  
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
vscodeでmarkdown形式を見る方法  
[ctrl]+[k]→[v]  

### 書く予定(処理速度高速化)  
https://www.kumilog.net/entry/python-speed-comp  
https://juppy.hatenablog.com/entry/2019/06/14/Python_競技プログラミング高速化tips_%28PythonでAtcoderをやる際に個  