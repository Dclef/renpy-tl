文档以迁移至https://docs.dclef.icu/

# 1.创建的初衷

现如今以是末法时代(指众多汉化组在11月前后消失事件)，虽然觉得被抓是应该的(指冷狐)，但是为爱发电的(指脸肿)也被喝茶解散以后，那么汉化组是否存在意义已经不大了，所以在人人自危的环境下，个人汉化似乎成为了唯一且安全的趋势，但一个人的所贡献的力量太小，于是乎想到了开源。

# 2.如何翻译文件？

## <span id="2.1" >2.1 首先你得准备以下工具：</span>

1. [python 3.7以上](https://www.python.org/)版本环境
2. [unrpyc](https://github.com/CensoredUsername/unrpyc/releases/tag/v1.1.7)文件 (用于反编译rpyc文件)
3. unrpa文件 【安装完python以后以及配置好环境变量(Path路径)请使用 **pip install unrpa** 安装unrpa包】(用于反编译rpa文件)
3. 以上3点可用[unren](https://dclef.lanzouj.com/iaveH00ukc1e)工具一次性解决(以汉化，如果打开闪退请使用[封装版](https://dclef.lanzouj.com/icHaM02i8ebe))，直接放入游戏根目录根据提示执行即可【目前unren不适用于一些作者进行简单加密的游戏，建议使用unrpyc+unrpa】
4. [ren'py sdk](https://www.renpy.org/latest.html) (本人使用的是renpy-7.4.11版本)  
5. 汉化包所描述的游戏

## 2.2 为了方便理解这里使用ren'py自带的教程

##  2.2.1 打开renpy.exe ，点击教程，生成翻译文件，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-20-15.png)

## 2.2.2 语言下方输入**chinese** ，选择为翻译生成空字符串(默认选择)，点击生成翻译文件，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-22-27.png)

## 2.2.3 如果成功你会得到如图所示信息。

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-23-04.png)



## 2.2.4 点击继续以后会返回到初始界面，在打开目录下方，选择打开game目录，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-24-49.png)

## 2.2.5 选择tl(翻译)文件，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-25-31.png)

##  2.2.6 点击chinese(教程自带多语言支持，一般游戏是没做的)，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-26-22.png)

## 2.2.7 点击有rpy后缀文件(如果汉化他人的游戏是没有rpy后缀，只有rpyc，如果想汉化他人游戏的教程请看 [3](#3))->右键->选择打开方式->以记事本的形式打开，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-27-06.png)



## 2.2.8 打开后会显示如图所示页面

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-28-39.png)



## 2.2.9 复制英文到 百度翻译或者谷歌翻译，这里选择的是谷歌翻译，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-29-17.png)

## 2.2.10 再将中文复制到文件中的new 下面(注意，必须放在空字符串也就是""中间，否则renpy会报错)，初步的简单翻译就大功告成，如图所示。

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-29-37.png)



# <span id="3" >3. 如何汉化他人游戏？</span>

**默认你[2.1](#2.1)的步骤已经全部准备好，如果[2.1](#2.1)的环境没有搭好请不要看下面的操作。**

## 3.1 将unrpyc放进游戏game目录下面，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_21-41-56.png)

## 3.2 返回到初始界面(是指带有exe的游戏目录界面)，运行一次游戏，运行成功并显示游戏界面以后，请关闭游戏，并删掉un.rpyc文件，你会发现多出来了后缀为rpy的文件，这类文件是可以打开的，如图所示。

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_22-18-15.png)

## 3.3 在game目录中放入SourceHanSansLite.ttf字体(此字体renpy sdk自带,在launcher\game\fonts 路径中)，打开**screens.rpy**文件，在其中搜索 preferences() ，如果你使用的是记事本的格式打开，请使用ctrl+F ，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_22-29-09.png)

## 3.4 在vbox相同格式下方添加以下代码(注意格式)，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_22-32-58.png)

```
                vbox:
                    style_prefix "radio"
                    label _("Language")
                    textbutton _("English") action Language(None)
                    textbutton _("Chinese") text_font "SourceHanSansLite.ttf" action Language("chinese")

```

## 3.5 请重复[2.2](#2.1)步骤，完成以后请在tl目录下新建一个style.rpy文件，如图所示【如果你直接更换了字体，此步骤可以跳过】

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_22-48-29.png)

里面的代码如下

```
translate chinese python:
    gui.system_font = gui.main_font = gui.text_font = gui.name_text_font = gui.interface_text_font = gui.button_text_font = gui.choice_button_text_font = "SourceHanSansLite.ttf"

```

## 3.6 请运行游戏，找到设置中的Language，选择Chinese。如图所示

### 注意：教程中的多语言支持自带有简体中文，不要搞混淆了。

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/Snipaste_2022-02-09_21-56-17.png)



## 3.7 以上的步骤完成以后理论上便可以汉化大部分的游戏文本，如果汉化的文本出现口口字，请查看[Q&A](#q&a)



# <span id="vscode">4. 如果想用更简单方式，请看以下步骤</span>

## 4.1 安装使用[vscode](https://code.visualstudio.com/) 

下载并安装到你本地，打开默认是英文界面，所以你需要安装汉化插件，如图所示(这里题主以安装过插件)。安装完成以后需要重新打开vscode，这样你的界面便是汉化界面。



![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_23-01-49.png)



## 4.2 安装翻译插件

请使用**Comment Translate**这个翻译插件(本用于翻译注释，但用于汉化却有着天然的优势)，如图所示。



![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_23-04-23.png)



## 4.3 点击左边第一个图标(资源管理器)，默认是无工作区，无工作夹的，请点击添加文件夹，将要翻译的文件夹添加到工作区即可，如图所示。



![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_23-10-57.png)

## 4.4 请选择信任该文件夹，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_23-13-17.png)

## 4.5 选择一个rpy文件，便可以直接进行翻译(无须复制粘贴到游览器翻译，节省大量时间)，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_23-17-46.png)

## 4.6 翻译插件默认是google翻译，如果想换成baidu翻译，如图所示。

此插件需要划词选中鼠标在其上面要停顿几秒(大概3s以内)，否则不容易显示。且必须将vscode中的python插件卸载(vscode会在打开rpy文件时在右下角推荐安装python扩展，请不要点)，否则不会显示翻译。

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_23-15-22.png)

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_23-20-11.png)



**注意：翻译的API的字数是有限制，如果出现网络错误请随时更换翻译api。**



## 4.7 如果悬停翻译不显示，那么请手动在插件中更换成BaiduApi，请打开Comment Translate插件扩展设置，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/2022-02-11_21-24-57.png)



![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/2022-02-11_21-25-10.png)

## 4.8 请勾选开启悬停翻译字符串和变量，以及将默认的Google改为Baidu，如图所示。你可以更换三种API (Google,Baidu,Bing)，注意首字母大写。

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/2022-02-11_21-25-36.png)



# 5.使用excel进行翻译(以更新视频)

对你没看错，确实能进行翻译，用excel翻译的原理来源于贴吧 (原帖已被删除)，本人进行了一定量的简化。

##### 下载表格汉化文件压缩包以及教程视频的，[请点击这里](https://dclef.lanzouj.com/inxOS03ha69g)

## 以下思路只提供参考，上面文件已经集成了，不需要你去实现操作。

###   5.1拿到原版游戏，进行unrpa和unrpyc解包和反编译， 用“Renpy解包助手汉化版.exe”软件或UnRen解包，看到文件里有大量.rpy文件就完成了

###  5.2用官方Ren'Py软件生成翻译文件，导出后在game目录下面就出现tl文件夹，文件夹chiese目录和下有很多.rpy和.rpyc文件，用记事本打开会发现很多垃圾注释。

### 5.3把chinese子目录下所有文件复制出来，先删除所有rpy文件后再反编译一次.rpyc文件重新生rpy文件，这时打开rpy文件垃圾注释消失。

### 5.4用文本合并工具把所有需要翻译的rpy文件合并为一个大文件，打开合并后的大文件，合并发现翻译一共几十万多行代码

### 5.5全选复制几十万多行文件内容，打开一个表格文件，粘贴到第一列，然后选中整列，生成筛选空行，然后删除所有空行。（可不删除，但建议删除，删除后可方面双击下拉填充表格）

### 5.6.这里我们需要提取两个引号中间的文字，用要两个表格函数，一个是find()函数用来定位两个引号的位置，另一个mid()函数,用来提取定位引号之间的字符串。

### 5.7.部分对话中内有\”表示引号，为避免出错，可先查找替换后再进行后操作。

### 5.8.筛选有翻译的整列，复制，只粘贴数值单独提出来

### 5.9把提出来的英文机翻成中文。我直接整列复制到谷歌浏览器，即可直接一建翻译，然后再选把翻译好的文件复制回来贴在下一列

### 5.10.再用=SUBSTITUTE()函数把翻译字符替换回去，结合一个简单IF函数输出在最右边，到这里我们机翻工作就完成了，

### 5.11.由于是机翻，本人想中英对照就原英文加个换行符(\n)一起替换回去，具体方法加个&合连接表格即可（注意：对话可以加换行符，new”语句加换行符容易出错，本模板只需手动删除\n即可）

### 5.12.把翻译并替换好的部分整列复制到文本文件，重命名为.rpy文件(不能用中文名)，放回Chinese目录下面，删除原目录里的所有文件，留一个文件就够了

## 注意 :

### 以上思路来源于贴吧，如果问到上面的问题本人不会回复

### 使用精简版的时候，留意里面的黄字部分即可。

# 6.使用Translator++进行翻译

##### 注意：此方法不需要生成chinese文件 

使用t++方法很简单，你只需要下载[t++](https://pan.baidu.com/s/1VDu1LBDqYAFXfBIpn-kCDQ?pwd=pay2)，打开工程翻译即可。

```
https://pan.baidu.com/s/1VDu1LBDqYAFXfBIpn-kCDQ?pwd=pay2
解压密码：Dreamsavior
```

### 6.1打开一个新工程 如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/Snipaste_2022-05-01_19-57-40.png)

### 6.2 选择要翻译的类型，如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/Snipaste_2022-05-01_19-57-49.png)

### 6.3 选择你游戏目录的exe文件，如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/Snipaste_2022-05-01_19-58-08.png)

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/Snipaste_2022-05-01_21-30-43.png)

#### 注意：有rpa文件的建议先解包，然后将rpa文件删除不然容易出现下面这种情况，如图

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/Snipaste_2022-05-01_19-58-31.png)

#### 打开完以后你会出现以下界面

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/Snipaste_2022-05-01_20-57-27.png)

##### 这时候就体现了t++的缺点，他将renpy里面的代码也给提取出来了，请不要去翻译。同时也要注意在game目录下的一些文本也不能去翻译，如图

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/Snipaste_2022-05-01_21-37-53.png)

##### 这里很明显看出这是一个icon目录下的png文件，他也给提取出来翻译了，请不要翻译。

### 6.4 选中文件，右键选中批量翻译，如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/Snipaste_2022-05-01_20-57-40.png)

##### 你可以更换翻译引擎，这里推荐google或者baidu

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/Snipaste_2022-05-01_21-45-56.png)

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/Snipaste_2022-05-01_21-41-09.png)

### 6.5 导出并覆盖到原文本（建议备份），如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/Snipaste_2022-05-01_20-59-29.png)

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/Snipaste_2022-05-01_20-59-46.png)

##### 这样你就成功翻译了该游戏，是不是很简单，之前国内大部分汉化组就是依靠着t++进行翻译（我称之为机翻汉化组），虽然简单但缺点也很明显，文本直接覆盖了，导致没有英文原版，所以下面讲的如何用脚本进行翻译。（t++的润色系统做的还行，如果机翻完了有时间可以去润色，他分为三种润色，机器翻译，较好的翻译和最好的翻译，实际上三种就是让你做对比，导出时他会根据你是否润色过选择权重最高的翻译，如果你啥都没有润色，就选取inital下的翻译）

# 7.使用脚本(调用百度API)进行翻译

##### 这里感谢katharsis提供的脚本，代码由本人简单修改上传在github中，有兴趣的可以去看一下，这里给个开箱即用的。

```
https://dclef.lanzouj.com/iwG9n044fdbi
```

##### 使用方法也很简单，先去百度拿到api，详情可看**8.5**。

##### 然后生成chinese文件，详情可看2.2.2

### 7.1 输入你的appid和密钥，输入要翻译的路径，以及源语言和要翻译的语言，替换路径选择填n 如图所示

### ![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/Snipaste_2022-05-01_22-17-41.png)

### 7.2 翻译完成你会生成new文件，如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/Snipaste_2022-05-01_22-18-31.png)

##### 翻译替换即可，也非常方便。

### 请注意：任何翻译软件都会有漏翻或翻译报错打不开的现象(包括以上两种方法)，如果用机翻软件报错请自行查看问题所在。

# 8. <span id="q&a">Q&A</span>【常见问题】

## 8<span id="8.1">.1 我想查看里面的CG和视频，但找不到如何解决？</span>

请完成[2.1](#2.1)步骤中的1和3，使用unrpa解决。

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

## 8.2 unrpyc文件我下载不了(不会下载)？

### 以放入百度网盘

```
链接: https://pan.baidu.com/s/1sCOcXudmkPjDAWMuy0n2Ag?pwd=tifz 提取码: tifz 
```

### 如果百度网盘慢的话请使用蓝奏云

```
https://dclef.lanzouj.com/b0bap2qbg
密码:bvd8
```



## 8.3 翻译后的文本出现口口(方块)字，该怎么办？

每个游戏作者都有不同写法，这里使用通杀的方式解决(不代表全部有效)

将**SourceHanSansLite.ttf**字体放入game目录中，在game目录中找到gui.rpy文件，如果没有请重复[5.1](#5.1)步骤。**或者用vscode进行全文检索找到所有带.otf或.ttf后缀的代码**，请全部替换成**SourceHanSansLite.ttf**。

## 8.4 有时候打开renpy.exe会报错，该如何解决？

**请删除renpy.exe目录下的game 文件。、**

## 8.5  在vscode使用翻译插件的时候会出现超时的情况，该如何解决？

如果出现这类情况，说明你翻译的速度太快，目前最好的方法就是配置Baidu的通用翻译(免费)，

你需要打开[百度翻译平台](http://api.fanyi.baidu.com/manage/developer)，将APP ID和密钥配置到Comment Translate，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/2022-02-11_21-25-54.png)

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/2022-02-11_22-02-48.png)

注意：你需要申请[通用翻译服务](http://api.fanyi.baidu.com/product/11)，否则不会有上图方框中显示的信息并且调用API时会报错，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/2022-02-11_22-03-15.png)



## 8.6 我想替换图标(如PC和安卓)该如何替换？

安卓你只要准备两张png图片，大小为432*432像素。

命名为android-icon_background.png和android-icon_foreground.png并放在游戏根目录即可。如果想下载案例请[点我](https://dclef.lanzouj.com/iuT9F02r89li)。

如果你想替换启动图，设置一张android-presplash.jpg，大小为500*500像素并放在游戏根目录即可。

为什么是要设置为432像素？因为这是新版安卓的自适应图标标准大小。

可看renpy的[官方文档](https://www.renpy.cn/doc/android.html#presplash)，有详细解释。

PC端你只需要设置一张为icon.ico的图标，大小为128*128像素并放在游戏根目录即可。详情请看下图。

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

## 8.7 翻译后打开游戏却是一片空白，该如何解决？

这种情况要么是你根本没有去翻译，游戏扫描到的是**空字符串**，要么就是你没有去**更换字体**，具体情况以游戏而定。

## 8.8 我想游戏一打开就是中文，该如何解决？

如果希望游戏一打开默认是中文，可以在 game 目录下的 screens.rpy最前面添上下面这句：

```
define config.language = "chinese"
```

这句话的意思是设置默认语言，这里的chinese是根据你**生成翻译文件的命名**而定，详情可看2.2.2部分。

## 8.9 有时候用renpysdk打开工程会报错，打开游戏则不会，该如何解决？

这种情况按报错而定，这里讲一种最常见的

```
ImportError: No module named unittest
```

显而易见，这是在本地没有unittest的包，全文搜索并在代码中删除有关unittest即可。

## 8.10 有时候游戏没有没有screen.rpy文件，该如何解决？

全文检索是否有preferences()或者vbox，我们的目的只是更换语言，这是作者自定义的问题，没有screen.rpy很正常。

## 8.11 renpy翻译文件导出的rpy文本不全怎么办?

这是由于renpysdk的正则没有扫描到作者所自定义的文本导致的，这种情况你必须在源码里面改，找到英文单词或句子汉化并替换，不能局限于tl目录下的翻译文件。

## 8.12 我想打包成安卓，但PC端已经有2-5G以上的内存，一打包就报错，该如何解决？

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

## 8.13 请在github中提交[issues](https://github.com/Dclef/renpy-tl/issues)，问题会根据issues中的问题或其他平台反馈的问题持续更新...............



# 9.参与本开源项目

如果你只想单纯的提出问题请提交[issues](https://github.com/Dclef/renpy-tl/issues)即可，如果你本身有代码基础或者无基础想参与到本项目中并修改机翻的话，请看以下步骤。

## 9.1 git 的安装与使用

下载[git](https://git-scm.com/downloads)，下载完成以后安装到本地(网上搜一下安装教程，这里就不多解释)。

安装完成后，在开始菜单里找到“Git”->“Git Bash”，弹一个类似命令行窗口的东西，就说明Git安装成功

接着需要设置一下信息，这台机器上的所有Git仓库都会使用这个配置 （步骤可以省略）

```
$ git config --global user.name "username"
$ git config --global user.email "email@example.com"
```

## 9.2 vscode中git的使用

安装vscode，如果不会请[点击查看](#vscode)

默认你已经注册了github账号，请fork我的项目，为了便于理解，这里新创建了一个账号，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-31_00-12-46.png)

fork完成以后，便会直接跳转到你的仓库，如图所示。

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-31_00-18-30.png)

注意：如果项目更新，你需要点击Fetch upstream来更新你的项目，如图所示。

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-31_00-22-21.png)

打开你的vscode，新建一个文件夹到你的工作区，选择要放入项目的文件夹中，右键在集成终端中打开，请输入git clone代码，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-31_00-26-49.png)

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-31_00-26-30.png)

代码如下

```
git clone 你的git链接
```

clone完成以后，修改你想要汉化文本或添加你要翻译的文本文件。这里仅演示修改文件。

修改完以后请点击左侧第三个按钮，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-31_00-33-55.png)

如果首次同步更改会让你去登陆github，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-31_00-34-36.png)

会出现允许打开url，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-31_00-35-38.png)

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-31_00-35-10.png)

打开并返回到vscode即可成功更新

## 9.3 在你的项目主页中提交request

如果你完成了很多代码修改，请提交一个request，请求合并，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-31_00-45-45.png)

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-31_00-46-33.png)

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-31_00-47-39.png)

**注意：标题以及内容请说明清楚，否则不会合并请求。**



# 10.尾声

renpy汉化教程到这里完结了(常见问题后续会在github上更新)，感谢你看到最后！

如果该项目对你有帮助，可以请我喝杯咖啡。

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/Snipaste_2022-05-01_22-32-56.png)



