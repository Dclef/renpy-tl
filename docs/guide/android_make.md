# 8.0版本的安卓制作(壳子)

前言：这玩意其实在现在的时间已经有很多汉化者制作了这种类型的游戏，
也就是一个100MB左右的游戏壳子和一个archive.rpa的大文件。将archive.rpa拖入到指定的目录在运行之前安装的游戏即可流程的运行游戏，不再像以前一样需要安装很长时间和打开闪退之类的。(早在21年renpy就有了这种安装模式，不过那时是末法时间，这里就不做赘述)

接下来就是制作安卓壳子教程。

## 环境准备

以下你需要准备以下工具

1.一个魔改版本的renpysdk (请加群获得)

2.一个反编译后的pc版renpy游戏(尽量是原版反编译)



## 1.整合archive.rpa

当你反编译完以后，进入game目录发现并没有archive.rpa这个东西，而是script.rpa或者是videos.rpa多个rpa文件，这时候你需要重新制作pc版本将其打包成一个archive.rpa文件。

![image-20240721203359200](https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-01.png)

### 1.1 修改options.rpy

找到options.rpy这个文件，如果没有的话请用工具(如vs code)全局搜索这个代码

```
build.archive
```

找到以后你会发现有这些代码(每个游戏情况会不一样)

![image-20240721203535111](https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-02.png)

将videos image gui script audio 全部删掉，替换成如图所示

```python
 build.archive('archive','all')
 build.classify('game/**', 'archive')
```



![image-20240721203810362](https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-03.png)

完成以后关闭并将之前的rpa全部删除(建议做备份)

### 1.2 制作archive.rpa

打开魔改版renpy-sdk，选择构建发行版,只勾选windows，然后选择构建,等待构建完毕。

你变会得到一个非常大的archive.rpa文件

![image-20240721205728400](https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-04.png)

## 2.制作安卓壳子

打开原版游戏目录，将其中的audio  images video 目录以及exe等文件删除(每个游戏情况会不一样) 如图所示

![image-20240721205439257](https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-05.png)然后打开打开魔改版renpy-sdk ,选择构建安卓版**(关于如何构建安卓版环境，这里不做赘述)**

在构建应用包名称时请输入你能识别这个游戏的名称(如果安卓上只有这款游戏可忽略)

![image-20240721205602057](https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-06.png)

然后构建安装包，这时候你会发现安装包会非常小

![image-20240721210207087](https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-07.png)

## 3. 安装游戏

将游戏安装后，必须要先运行一次，你会发现能运行，只是说没有图片。![image-20240721210442537](https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-08.png)



然后退出，用文件管理其找到Documents/RenPy_Saves/ 这个目录

![image-20240721210528353](https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-09.png)

你会发现安装的游戏就在这里，将archive.rpa丢进游戏的game目录里，如图

![image-20240721210729076](https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-10.png)

然后再运行游戏你会发现图片回来了，这样就可以进行和PC一样画质的游玩体验，至此，本篇教程结束。

![image-20240721210856066](https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-11.png)