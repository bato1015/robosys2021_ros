# robosys2021_ros
ロボットシステム学課題2提出用レポジトリです。rand関数、ROSを使用してルーレットを作成しました。  
*オマケの機能  
オッズ、掛け金、番号を入力し、メッセージで勝敗と金額を表示します。
***

## 動作環境
OS:ubuntu 20.04 sever  
ROS:Noetic  
Librar:RPi.GPIO  
***

## 用意するもの
・Raspberry Pi 4 ModelB  
・ブレッドボード  
・ステッピングモータ(28BYJ-48 5V)  
・<a href="https://www.amazon.co.jp/KKHMF-2%E5%80%8B%E3%82%BB%E3%83%83%E3%83%88-28BYJ-48-%E3%82%B9%E3%83%86%E3%83%83%E3%83%94%E3%83%B3%E3%82%B0%E3%83%A2%E3%83%BC%E3%82%BF%E3%83%BC-ULN2003%E3%82%B9%E3%83%86%E3%83%83%E3%83%94%E3%83%B3%E3%82%B0%E3%83%A2%E3%83%BC%E3%82%BF%E3%83%BC%E9%A7%86%E5%8B%95%E3%83%86%E3%82%B9%E3%83%88%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB%E3%83%9C%E3%83%BC%E3%83%89/dp/B088FLLYF3/ref=pd_lpo_2?pd_rd_i=B088FLLYF3&psc=1">ULN2003ドライバー</a>  
・ジャンパー線 オス−メス 12本  
・<a href="https://user-images.githubusercontent.com/70883743/148672282-8a0ee486-3e10-4556-bdd9-a6a12cfef9dc.jpg">ルーレット台</a>

***
## ピン配置
| DRIVER | GPIO |
| ------ | ---- |
| IN1    | 4    |
| IN2    | 17   |
| IN3    | 27   |
| IN4    | 22   |
***
## 回路
Raspberry Pi 4の回路データがなかったため、Raspberry Pi 3で代用  
![image](https://user-images.githubusercontent.com/70883743/148645451-f5ca7c53-aea2-4464-841c-572230a073bd.png)

***
## ノード図
![image](https://user-images.githubusercontent.com/70883743/148645940-1d103b15-44c5-4d56-ac6c-d13cddba1f39.png)

***
## インストール
ワークスペースを作成し、パッケージ内にcloneしてください.  

PythonライブラリーRPi.GPIOがインストールされていない場合
```bash
 sudo apt-get install python-rpi.gpio
 ```
以下コードを続けて実行
```
git clone git@github.com:bato1015/robosys2021_ros.git
git checkout mastr
cd ..
catkin_make
cd src/robosys2021_ros/scripts
chmod +x roullette.py cal_num.py
```
***
## 実行手順
合計4つのターミナルを使用します。以下コードをそれぞれのターミナルで実行してください。  
*ターミナル4は最後にコマンドを打つようにしてください

・ターミナル1(ros起動)
```
roscore
```
・ターミナル2(結果出力)
```
rosrun robosys2021_ros rullette.py
```
・ターミナル3(ルーレット起動)
```
rostopic echo /result
```
・ターミナル4(入力画面)
```
rosrun robosys2021_ros cal_num.py
```
## 遊び方
ターミナル3はルーレットが止まる前に結果が表示されるため、隠すことを推奨します。  
1.ターミナル4実行後、標準出力に従って数字を入力してください.  
2.ルーレットが回ります。  
3.ターミナル3で勝敗を確認してください。
### 具体例
```
2?4?  　　　　　　　　　　//掛率
2　　　　　　　//入力1
How much bet?　　　　　　//オッズ
2000          //入力２
blue:1 red:2 
1　　　　　　　//入力3
```
## 動画
***

<a href="https://www.youtube.com/watch?v=UQO0qApB6VU">ロボットシステム学課題2</a>

## 参考資料
<a href="https://kazuyamashi.github.io/ros_lecture/ros_study_py.html">ROSの基本的な開発</a>  
<a href="https://tutorials-raspberrypi.com/how-to-control-a-stepper-motor-with-raspberry-pi-and-l293d-uln2003a/">ステッピングモーターの動かし方</a>  
<a href="https://stupiddog.jp/note/archives/1235">ULN2003Aの回路図</a>
***
## ライセンス
<a href="https://github.com/bato1015/robosys2021_ros/blob/master/LICENSE">BSD 3-Clause License</a>
