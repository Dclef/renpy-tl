# Q&A

## 我想查看里面的CG和视频，但找不到如何解决？

使用unrpa解决。

解决步骤为：找到后缀为.rpa文件，在文件路径上方输入cmd，如图所示。

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_23-30-52.png)

输入代码后，等待出现如图所示的Extracting files from ，在game目录中便会出现你想要的

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_23-32-19.png)

```
python -m unrpa archive.rpa
```

archive.rpa 指的是你要反编译的文件。

如果发现python 不是内部或外部命令，也不是可运行的程序或批处理文件，请另行解决。

如果发现 **No module named unrpa** ，请在cmd命令行中输入**pip install unrpa**

## unrpyc文件我下载不了(不会下载)？

### 以放入百度网盘

```
链接: https://pan.baidu.com/s/1sCOcXudmkPjDAWMuy0n2Ag?pwd=tifz 提取码: tifz 
```

### 如果百度网盘慢的话请使用蓝奏云

```
https://dclef.lanzouj.com/b0bap2qbg
密码:bvd8
```



##  翻译后的文本出现口口(方块)字，该怎么办？

每个游戏作者都有不同写法，这里使用通杀的方式解决(不代表全部有效)

将**SourceHanSansLite.ttf**字体放入game目录中，在game目录中找到gui.rpy文件，用vscode进行全文检索找到所有带.otf或.ttf后缀的代码，请全部替换成**SourceHanSansLite.ttf**。

## 有时候打开renpy.exe会报错，该如何解决？

**请删除renpy.exe目录下的game 文件。、**

## 在vscode使用翻译插件的时候会出现超时的情况，该如何解决？

如果出现这类情况，说明你翻译的速度太快，目前最好的方法就是配置Baidu的通用翻译(免费)，

你需要打开[百度翻译平台](http://api.fanyi.baidu.com/manage/developer)，将APP ID和密钥配置到Comment Translate，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/2022-02-11_21-25-54.png)

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/2022-02-11_22-02-48.png)

注意：你需要申请[通用翻译服务](http://api.fanyi.baidu.com/product/11)，否则不会有上图方框中显示的信息并且调用API时会报错，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/2022-02-11_22-03-15.png)



## 我想替换图标(如PC和安卓)该如何替换？

安卓你只要准备两张png图片，大小为432*432像素。

命名为android-icon_background.png和android-icon_foreground.png并放在游戏根目录即可。如果想下载案例请[点我](https://dclef.lanzouj.com/iuT9F02r89li)。

如果你想替换启动图，设置一张android-presplash.jpg，大小为500*500像素并放在游戏根目录即可。

为什么是要设置为432像素？因为这是新版安卓的自适应图标标准大小。

可看renpy的[官方文档](https://www.renpy.cn/doc/android.html#presplash)，有详细解释。

PC端你只需要设置一张为icon.ico的图标，大小为48*48像素并放在游戏根目录即可。详情请看下图。

![](https://cdn.jsdelivr.net/gh/Dclef/CDN@master/renpy/2022-04-07_09-46-34.png)

##### 以上均要重新再次封包才能生成。

#### 如果你要设置PC端桌面的图标，如下图

![](https://cdn.jsdelivr.net/gh/Dclef/CDN@master/renpy/2022-04-07_16-33-59.png)

你只需要准备一张250*250像素的图片，并在options.rpy中设置一行代码。如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN@master/renpy/2022-04-07_09-46-13.png)

上图所示图标路径如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN@master/renpy/2022-04-07_09-45-32.png)

关于如何去修改像素大小和生成图标，这里我建议使用ps要或者在线ps

##### 在线ps我推荐使用[photopea](https://www.photopea.com/)

## 翻译后打开游戏却是一片空白，该如何解决？

这种情况要么是你根本没有去翻译，游戏扫描到的是**空字符串**，要么就是你没有去**更换字体**，具体情况以游戏而定。

## 我想游戏一打开就是中文，该如何解决？

如果希望游戏一打开默认是中文，可以在 game 目录下的 screens.rpy最前面添上下面这句：

```
define config.language = "chinese"
```

这句话的意思是设置默认语言，这里的chinese是根据你**生成翻译文件的命名**而定，详情可看2.2.2部分。

## 有时候用renpysdk打开工程会报错，打开游戏则不会，该如何解决？

这种情况按报错而定，这里讲一种最常见的

```
ImportError: No module named unittest
```

显而易见，这是在本地没有unittest的包，全文搜索并在代码中删除有关unittest即可。

## 有时候游戏没有没有screen.rpy文件，该如何解决？

全文检索是否有preferences()或者vbox，我们的目的只是更换语言，这是作者自定义的问题，没有screen.rpy很正常。

## renpy翻译文件导出的rpy文本不全怎么办?

这是由于renpysdk的正则没有扫描到作者所自定义的文本导致的，这种情况你必须在源码里面改，找到英文单词或句子汉化并替换，不能局限于tl目录下的翻译文件。

## 我想打包成安卓，但PC端已经有2-5G以上的内存，一打包就报错，该如何解决？

打不了2G以上的包是因为renpysdk本身性能的问题，所以很多作者打包安卓版都会压缩图片和视频，以保证在2G左右，所以图片视频其实有两套，而我们只找到PC端，却忽略了安卓端，所以我们只需要把安卓端拿来并解压即可(安卓端也可能会加密，所以只能解决99%的游戏)。

**但拿到安卓端却有X-前缀，该如何解决？**

这里本人写了个python小工具，可以用这个解决，源码以放在github上，这里给个开箱即用的。

```
https://dclef.lanzouj.com/iA4Kc0441mbi
```

注意：该工具只能重命名当前目录下的文件，不能命名目录下以及子目录下的文件，所以如果作者做了多个文件夹请多次使用。

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/Snipaste_2022-05-01_19-09-49.png)

##### 为什么打包会报错？

大概率你没有挂魔法，因为要去下Gradle,这个请自行解决。

