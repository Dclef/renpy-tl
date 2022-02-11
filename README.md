## 1.创建的初衷

现如今以是末法时代(指众多汉化组在11月前后消失事件)，虽然觉得被抓是应该的(指冷狐)，但是为爱发电的(指脸肿)也被喝茶解散以后，那么汉化组是否存在意义已经不大了，所以在人人自危的环境下，个人汉化似乎成为了唯一且安全的趋势，但一个人的所贡献的力量太小，于是乎想到了开源。

## 2.如何翻译文件？

### <span id="2.1" >2.1 首先你得准备以下工具：</span>

1. [python 3.7以上](https://www.python.org/)版本环境
2. [unrpyc](https://github.com/CensoredUsername/unrpyc/releases/tag/v1.1.7)文件 (用于反编译rpyc文件)
3. unrpa文件 【安装完python以后以及配置好环境变量(Path路径)请使用 **pip install unrpa** 安装unrpa包】(用于反编译rpa文件)
4. [ren'py sdk](https://www.renpy.org/latest.html) (本人使用的是renpy-7.4.11版本)  
5. 汉化包所描述的游戏

### 2.2 为了方便理解这里使用ren'py自带的教程

####  2.2.1 打开renpy.exe ，点击教程，生成翻译文件，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-20-15.png)

#### 2.2.2 语言下方输入**chinese** ，选择为翻译生成空字符串(默认选择)，点击生成翻译文件，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-22-27.png)

#### 2.2.3 如果成功你会得到如图所示信息。

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-23-04.png)



#### 2.2.4 点击继续以后会返回到初始界面，在打开目录下方，选择打开game目录，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-24-49.png)

#### 2.2.5 选择tl(翻译)文件，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-25-31.png)

####  2.2.6 点击chinese(教程自带多语言支持，一般游戏是没做的)，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-26-22.png)

#### 2.2.7 点击有rpy后缀文件(如果汉化他人的游戏是没有rpy后缀，只有rpyc，如果想汉化他人游戏的教程请看 [3](#3))->右键->选择打开方式->以记事本的形式打开，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-27-06.png)



#### 2.2.8 打开后会显示如图所示页面

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-28-39.png)



#### 2.2.9 复制英文到 百度翻译或者谷歌翻译，这里选择的是谷歌翻译，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-29-17.png)

#### 2.2.10 再将中文复制到文件中的new 下面(注意，必须放在空字符串也就是""中间，否则renpy会报错)，初步的简单翻译就大功告成，如图所示。

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-29-37.png)



## <span id="3" >3. 如何汉化他人游戏？</span>

**默认你[2.1](#2.1)的步骤已经全部准备好，如果[2.1](#2.1)的环境没有搭好请不要看下面的操作。**

### 3.1 将unrpyc放进游戏game目录下面，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_21-41-56.png)

### 3.2 返回到初始界面(是指带有exe的游戏目录界面)，运行一次游戏，运行成功并显示游戏界面以后，请关闭游戏，并删掉un.rpyc文件，你会发现多出来了后缀为rpy的文件，这类文件是可以打开的，如图所示。

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_22-18-15.png)

### 3.3 在game目录中放入SourceHanSansLite.ttf字体(此字体renpy sdk自带,在launcher\game\fonts 路径中)，打开**screens.rpy**文件，在其中搜索 preferences() ，如果你使用的是记事本的格式打开，请使用ctrl+F ，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_22-29-09.png)

### 3.4 在vbox相同格式下方添加以下代码(注意格式)，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_22-32-58.png)

```
                vbox:
                    style_prefix "radio"
                    label _("Language")
                    textbutton _("English") action Language(None)
                    textbutton _("Chinese") text_font "SourceHanSansLite.ttf" action Language("chinese")

```

### 3.5 请重复[2.2](#2.1)步骤，完成以后请在tl目录下新建一个style.rpy文件，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_22-48-29.png)

里面的代码如下

```
translate chinese python:
    gui.system_font = gui.main_font = gui.text_font = gui.name_text_font = gui.interface_text_font = gui.button_text_font = gui.choice_button_text_font = "SourceHanSansLite.ttf"

```

### 3.6 请运行游戏，找到设置中的Language，选择Chinese。如图所示

### 注意：教程中的多语言支持自带有简体中文，不要搞混淆了。

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/Snipaste_2022-02-09_21-56-17.png)



### 3.7 以上的步骤完成以后理论上便可以汉化大部分的游戏文本，如果汉化的文本出现口口字，请查看[Q&A](#q&a)



## <span id="vscode">4. 如果想用更简单方式，请看以下步骤</span>

### 4.1 安装使用[vscode](https://code.visualstudio.com/) 

下载并安装到你本地，打开默认是英文界面，所以你需要安装汉化插件，如图所示(这里题主以安装过插件)。安装完成以后需要重新打开vscode，这样你的界面便是汉化界面。



![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_23-01-49.png)



### 4.2 安装翻译插件

请使用Comment Translate这个翻译插件(本用于翻译注释，但用于汉化却有着天然的优势)，如图所示。



![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_23-04-23.png)



### 4.3 点击左边第一个图标(资源管理器)，默认是无工作区，无工作夹的，请点击添加文件夹，将要翻译的文件夹添加到工作区即可，如图所示。



![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_23-10-57.png)

### 4.4 请选择信任该文件夹，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_23-13-17.png)

### 4.5 选择一个rpy文件，便可以直接进行翻译(无须复制粘贴到游览器翻译，节省大量时间)，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_23-17-46.png)

### 4.6 翻译插件默认是google翻译，如果想换成baidu翻译，如图所示。

### 此插件需要划词选中鼠标在其上面要停顿几秒(大概3s以内)，否则不容易显示。且必须将vscode中的python插件卸载(vscode会在打开rpy文件时在右下角推荐安装python扩展，请不要点)，否则不会显示翻译。

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_23-15-22.png)

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-30_23-20-11.png)



**注意：翻译的API的字数是有限制，如果出现网络错误请随时更换翻译api。**



### 4.7 如果悬停翻译不显示，那么请手动在插件中更换成BaiduApi，请打开Comment Translate插件扩展设置，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/2022-02-11_21-24-57.png)



![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/2022-02-11_21-25-10.png)

### 4.8 请勾选开启悬停翻译字符串和变量，以及将默认的Google改为Baidu，如图所示。你可以更换三种API (Google,Baidu,Bing)，注意首字母大写。

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/2022-02-11_21-25-36.png)





## 5. <span id="q&a">Q&A</span>【常见问题】

### <span id="5.1">5.1 我想查看里面的CG和视频，但找不到如何解决？</span>

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

如果发现 No module named unrpa ，请在cmd命令行中输入**pip install unrpa**

### 5.2 unrpyc文件我下载不了(不会下载)？

以放入百度网盘

```
链接: https://pan.baidu.com/s/1sCOcXudmkPjDAWMuy0n2Ag?pwd=tifz 提取码: tifz 
```

### 5.3 翻译后的文本出现口口(方块)字，该怎么办？

每个游戏作者都有不同写法，这里使用通杀的方式解决(不代表全部有效)

将**SourceHanSansLite.ttf**字体放入game目录中，在game目录中找到gui.rpy文件，如果没有请重复[5.1](#5.1)步骤。找到所有带.otf或.ttf后缀的代码，请全部替换成**SourceHanSansLite.ttf**。

### 5.4 有时候打开renpy.exe会报错，该如何解决？

请删除renpy.exe目录下的game 文件。、

### 5.5  在vscode使用翻译插件的时候会出现超时的情况，该如何解决？

如果出现这类情况，说明你翻译的速度太快，目前最好的方法就是配置Baidu的通用翻译(免费)，

你需要打开[百度翻译平台](http://api.fanyi.baidu.com/manage/developer)，将APP ID和密钥配置到Comment Translate，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/2022-02-11_21-25-54.png)

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/2022-02-11_22-02-48.png)

注意：你需要申请[通用翻译服务](http://api.fanyi.baidu.com/product/11)，否则不会有上图方框中显示的信息并且调用API时会报错，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/2022-02-11_22-03-15.png)

### 5.6 请在github中提交[issues](https://github.com/Dclef/renpy-tl/issues)，问题会根据issues中的问题或其他平台反馈的问题持续更新...............



## 6.参与本开源项目

如果你只想单纯的提出问题请提交[issues](https://github.com/Dclef/renpy-tl/issues)即可，如果你本身有代码基础或者无基础想参与到本项目中并修改机翻的话，请看以下步骤。

### 6.1 git 的安装与使用

下载[git](https://git-scm.com/downloads)，下载完成以后安装到本地(网上搜一下安装教程，这里就不多解释)。

安装完成后，在开始菜单里找到“Git”->“Git Bash”，弹一个类似命令行窗口的东西，就说明Git安装成功

接着需要设置一下信息，这台机器上的所有Git仓库都会使用这个配置 （步骤可以省略）

```
$ git config --global user.name "username"
$ git config --global user.email "email@example.com"
```

### 6.2 vscode中git的使用

安装vscode，如果不会请[点击查看](#vscode)，并在插件商店中下载GitLens，或者[此链接](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)

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

### 6.3 在你的项目主页中提交request

如果你完成了很多代码修改，请提交一个request，请求合并，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-31_00-45-45.png)

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-31_00-46-33.png)

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-31_00-47-39.png)

**注意：标题以及内容请说明清楚，否则不会合并请求。**



提交完成以后就可以不用管了，感谢你本开源项目做出了一份贡献



