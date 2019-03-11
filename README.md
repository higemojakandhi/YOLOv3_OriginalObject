# Overview
Used YOLO to recognize original object (Eggplant)

# Difficulty
Eggplant is difficult to detect using OpenCV,
due to its darkness that cannot be classified between shadow and the object itself.

# How to make YOLO learn the original object
1. Collect Images (from ImageNet)
2. Annotate By Yourself by using [BBox-Label-Tool](https://github.com/puzzledqs/BBox-Label-Tool)
3. Divide into Training Sets and Testing Sets
4. Preparing Some Config Files needed for YOLO

5. Install YOLO V3 from [darknet](https://pjreddie.com/darknet/yolo/)
6. Make it Learn

# Example
### Test 1
<img src="https://user-images.githubusercontent.com/11141442/44299831-e1b40400-a337-11e8-9a6e-7d567dfc23ca.jpg" alt="001" width="300px"/>

### Test 2
<img src="https://user-images.githubusercontent.com/11141442/44299853-0dcf8500-a338-11e8-8b76-ee114ddeea38.jpg" alt="002" width="300px"/>


### Test 3
<img src="https://user-images.githubusercontent.com/11141442/44299836-e973a880-a337-11e8-8612-04f823601a4e.jpg" alt="003" width="300px"/>

### Test 4
<img src="https://user-images.githubusercontent.com/11141442/44299837-e973a880-a337-11e8-9870-127e340ba1a5.jpg" alt="004" width="300px"/>

### Test 5
<img src="https://user-images.githubusercontent.com/11141442/44299838-ea0c3f00-a337-11e8-8845-871315a63673.jpg" alt="005" width="300px"/>

### Test 6
<img src="https://user-images.githubusercontent.com/11141442/44299840-ea0c3f00-a337-11e8-88df-fd68271f2211.jpg" alt="006" width="300px"/>

### Test 7
<img src="https://user-images.githubusercontent.com/11141442/44299841-eaa4d580-a337-11e8-99c3-0badb236cd6e.jpg" alt="007" width="300px"/>

### Test 8
<img src="https://user-images.githubusercontent.com/11141442/44299842-eaa4d580-a337-11e8-90b4-f6ef51871e75.jpg" alt="008" width="300px"/>

### Test 9
<img src="https://user-images.githubusercontent.com/11141442/44299843-ed072f80-a337-11e8-983a-adf6ae2778b6.jpg" alt="009" width="300px"/>

### Test 10
<img src="https://user-images.githubusercontent.com/11141442/44299844-ed9fc600-a337-11e8-8abc-a6d3ae3a6af8.jpg" alt="010" width="300px"/>



# 導入
```shell
$ git clone https://github.com/pjreddie/darknet.git
$ cd darknet
$ vi Makefile
$ make
$ wget https://pjreddie.com/media/files/yolov3.weights
$ ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
```
結果

```shell
layer     filters    size              input                output
    0 conv     32  3 x 3 / 1   416 x 416 x   3   ->   416 x 416 x  32  0.299 BFLOPs
    1 conv     64  3 x 3 / 2   416 x 416 x  32   ->   208 x 208 x  64  1.595 BFLOPs
    .......
  105 conv    255  1 x 1 / 1    52 x  52 x 256   ->    52 x  52 x 255  0.353 BFLOPs
  106 detection
truth_thresh: Using default '1.000000'
Loading weights from yolov3.weights...Done!
data/dog.jpg: Predicted in 0.029329 seconds.
dog: 99%
truck: 93%
bicycle: 99%
```

![predictions.png](https://qiita-image-store.s3.amazonaws.com/0/146448/680a012c-ecab-a616-2f2f-d9d60d3cc4b3.png)


# MY Original YOLO
## 手順
1. 画像のダウンロード
2. 画像にラベリング
3. ラベリングをYOLOで使用する形に変換
4. train用とtest用に分ける
5. 設定ファイル作成
6. 学習！

### 1. 画像のダウンロード 
1. ImageNetからガシガシダウンロード  
1.1. [ImageNetのサイト](http://image-net.org/download-imageurls)から画像がダウンロードできるURLが載ったtxtをダウンロードしてきます。  
1.2 `python download_imagenet.py`で落としてきます。  
※ [コードは作りました](https://github.com/higemojakandhi/YOLOv3_OriginalObject/blob/master/download_images/download_imagenet.py)  
2. Google Imagesからダウンロード

```
sudo apt-get install chromium-chromedriver
sudo pip install google_images_download
googleimagesdownload -k "なす　栽培" -la Japanese -l 2000 -f "jpg" -cd "/usr/lib/chromium-browser/chromedriver"
```


### 2. 画像にラベリング
[BBox-Label-Tool](https://github.com/puzzledqs/BBox-Label-Tool)を使ってラベリングします。

```
git clone https://github.com/puzzledqs/BBox-Label-Tool
cd BBox-Label-Tool/
python main.py 
``` 
画像は以下のフォルダーのようにおいておきます。

```
BBox-Label-Tool
 |- Images
   |- 001
     |- 001.jpg 
     |- 002.jpg ....
```
![image.png](https://qiita-image-store.s3.amazonaws.com/0/146448/650c04cc-6f10-98f2-965f-4ad518ab26eb.png)

### 2. ラベリングをYOLOで使用する形に変換
`convert.py`を`https://github.com/Guanghan/darknet/blob/master/scripts/convert.py`からダウンロードしてきます。
先ほどラベリングした画像とラベルをconvert.pyのフォルダーに入れます。
![Workspace 1_001.png](https://qiita-image-store.s3.amazonaws.com/0/146448/64c2e2dd-4d21-6579-653e-398274d85c8e.png)

```
python convert.py
```

### 4. train用とtest用に分ける
再度先ほどconvertした画像とラベルをdarknetのフォルダに入れておきます。
#### 全体像
```
darknet
 |- data
 |   |- images
 |       |- 001.jpg
 |       |- 002.jpg
 |       |- 003.jpg ...
 |       |- divide_into_traintestdata.py
 |       |- test.txt
 |       |- train.txt
 |       |- obj.name
 |   |- labels
 |       |- 001.txt
 |       |- 002.txt
 |       |- 003.txt ...
 |- cfg
     |- obj.data
     |- yolov3-obj.cfg
```

[git](https://github.com/higemojakandhi/YOLOv3_OriginalObject/blob/master/divide_into_traintestdata.py)から`divide_into_traintestdata.py`をダウンロードして走らせれば学習データとテストデータにわけられます。

### 5. 設定ファイル作成
1. 物体名一覧ファイル
2. ネットワークの構成
3. これら全体のファイルの保存場所を示すファイル

#### 5.1 物体名一覧ファイル
```obj.name
eggplant
```
#### 5.2 ネットワークの構成

```
cp yolov3.cfg  yolov3-obj.cfg
```
中身を書き換えていく。
１〜7行目を以下のように変更する。

```
# Testing
#batch=1
#subdivisions=1
# Training
batch=64
subdivisions=16 # 16
```
次に、classesとfiltersを変更する。
filters=(クラス数+5)*3なので、filtersは18とする。

```
605行目 filters=18
611行目 classes=1
689行目 filters=18
695行目 classes=1
773行目 filters=18
779行目 classes=1
```

### 6.  学習
```
cd darknet/
wget https://pjreddie.com/media/files/darknet53.conv.74
./darknet detector train cfg/obj.data cfg/yolov3-obj.cfg darknet53.conv.74
```

# 学習させたYOLOをrosで動かす
## あると望ましい
 - CUDA

## install
```
cd ~/catkin_ws/src
git clone –recursive git@github.com:leggedrobotics/darknet_ros.git
cd ..
catkin_make -DCMAKE_BUILD_TYPE=Release
```

## 設定
### 重み
重みとネットワークの構成は以下のフォルダに入れる

```
catkin_ws/src/darknet_ros/darknet_ros/yolo_network_config/weights/
catkin_ws/src/darknet_ros/darknet_ros/yolo_network_config/cfg/
```

### 画像トピックの設定

```
catkin_ws/src/darknet_ros/darknet_ros/config/ros.yaml
```

```ros.yaml
topic: /camera/color/image_raw
```


### 全体の設定

```
cd ~/catkin_ws/src/darknet_ros/darknet_ros/config
cp yolov3.yaml  yolov3-obj.yaml
```

```yolov3-obj.yaml
yolo_model:
  config_file:
    name: yolov3-obj.cfg
  weight_file:
    name: yolov3-obj_900.weights
  threshold:
    value: 0.3
  detection_classes:
    names:
      - eggplant
````

### launch file

```
cp yolo_v3.launch eggplant.launch
```

```eggplant.launch
  <rosparam command="load" ns="darknet_ros" file="$(find darknet_ros)/config/yolov3-obj.yaml"/>
```

# RealSenseで認識して距離をとってくる。
YOLOで認識した画像中の物体の距離を取得するプログラムは自作した。
https://github.com/watakandhi/darknet_ros/blob/master/darknet_ros/scripts/ObjectDepth.py

# 実行する
```
roslaunch realsense2_camera rs_rgbd.launch
roslaunch darknet_ros yolo_v3.launch
rosrun darknet_ros ObjectDepth.py
rviz
```
rvizで`camera/depth_registered/points`トピックが飛ばしているPointCloud2データを可視化させると以下のようになる

![image.png](https://qiita-image-store.s3.amazonaws.com/0/146448/65949dbc-1d96-9e92-9b0f-0e0aa5ea4a86.png)
