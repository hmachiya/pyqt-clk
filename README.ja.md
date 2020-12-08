# pyqt-clk

PyQtを使用した簡易時計ウィジェット。

## Requirements

- Python 3.x
- PyQt5
- Windows10+Anacoda環境のみで動作確認済み

## Installation

ダウンロードして好きな場所に展開

## Usage

起動するには、Anaconda等のターミナルからqtclk.pyを実行してください。

`pythonw {path to qtclk.py}`

ウインドウをダブルクリックすると閉じます。

## Known issue(s)

ExpolorerからPythonw.exeを使ってqtclk.pyを開いても起動できるが、なぜか常に最前面に来なくなる。

## To do

- macOSとLinuxでの動作確認
- JSONかなんかでテーマを変えられるようにする

## Motivation

"タスクバーを自動的に隠す"という設定はノートPC等で縦の解像度が足りない場合に重宝するが、時計も消えてしまうのが難点だった。

フリーソフトで時計を表示するものは多数あるが、会社支給PCなどでは自由にインストールできないことが多く、なら自分で最初から作ってしまえと言うことで作成した(*)。

(*) なお、ここで公開しているのは個人として作成したものであり、所属組織とは一切関係ありません。