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


####  2.2.5 点击chinese(教程自带多语言支持，一般游戏是没做的)，如图所示

<<<<<<< HEAD

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-26-22.png)

#### 2.2.6 点击有rpy后缀文件(如果汉化他人的游戏是没有rpy后缀，只有rpyc，如果想汉化他人游戏的教程请看 [3](#3))->右键->选择打开方式->以记事本的形式打开，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-27-06.png)


=======

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-26-22.png)






#### 2.2.7 打开后会显示如图所示页面

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-28-39.png)



#### 2.2.8 复制英文到 百度翻译或者谷歌翻译，这里选择的是谷歌翻译，如图所示

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-29-17.png)

#### 2.2.9 再将中文复制到文件中的new 下面(注意，必须放在空字符串也就是""中间，否则renpy会报错)，初步的简单翻译就大功告成，如图所示。

![](https://cdn.jsdelivr.net/gh/Dclef/CDN/renpy/renpy_2022-01-28_00-29-37.png)



## <span id="3" >3. 如何汉化他人游戏？</span>

默认你[2.1](#2.1)的步骤已经全部准备好，如果[2.1](#2.1)的环境没有搭好请不要看下面的操作。

3.1 将unrpyc放进游戏game目录下面，如图所示