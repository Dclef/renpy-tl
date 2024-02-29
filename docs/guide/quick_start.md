# 快速开始

## 环境准备

1. [python 3.7以上](https://www.python.org/)版本环境【可忽略】
2. ~~[unrpyc](https://github.com/CensoredUsername/unrpyc/releases/tag/v1.1.7)文件 (用于反编译rpyc文件)~~【已过时】
3. ~~unrpa文件 【安装完python以后以及配置好环境变量(Path路径)请使用 **pip install unrpa** 安装unrpa包】(用于反编译rpa文件)~~【已过时】
4. 以上3点可用[unren](https://dclef.lanzouj.com/iaveH00ukc1e)工具一次性解决(如果解决不了请使用高版本)，直接放入游戏根目录根据提示执行即可
5. [ren'py sdk](https://www.renpy.org/latest.html) (本人使用的是renpy-7.4.11版本)
6. 汉化包所描述的游戏【本人不提供任何游戏】

## 基础汉化

### 打开renpy.exe ，点击教程，生成翻译文件，如图所示

[![img](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/quick_start_1.png)]

### 语言下方输入**chinese** ，选择为翻译生成空字符串(默认选择)，点击生成翻译文件，如图所示

[![img](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/quick_start_2.png)]

### 如果成功你会得到如图所示信息。

[![img](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/quick_start_3.png)]

### 点击继续以后会返回到初始界面，在打开目录下方，选择打开game目录，如图所示

[![img](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/quick_start_4.png)]

### 选择tl(翻译)文件，如图所示

[![img](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/quick_start_5.png)]

### 点击chinese(教程自带多语言支持，一般游戏是没做的)，如图所示

[![img](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/quick_start_6.png)]

### 点击有rpy后缀文件(如果汉化他人的游戏是没有rpy后缀，只有rpyc->右键->选择打开方式->以记事本的形式打开，如图所示

[![img](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/quick_start_7.png)]

### 打开后会显示如图所示页面

[![img](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/quick_start_8.png)]

### 复制英文到 百度翻译或者谷歌翻译，这里选择的是谷歌翻译，如图所示

[![img](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/quick_start_9.png)]

### 再将中文复制到文件中的new 下面(注意，必须放在空字符串也就是""中间，否则renpy会报错)，初步的简单翻译就大功告成，如图所示。

[![img](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/quick_start_10.png)]

## 界面汉化

::: warning 注意
现以不需要多余的环境，只需下载好renpysdk即可。

:::

### ~~将unrpyc放进游戏game目录下面，如图所示~~【可忽略，此操作已过时】

[![img](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/quick_start_11.png)]

### 返回到初始界面(是指带有exe的游戏目录界面)，运行一次游戏，运行成功并显示游戏界面以后，请关闭游戏，并~~删掉un.rpyc~~文件，你会发现多出来了后缀为rpy的文件，这类文件是可以打开的，如图所示。

[![img](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/quick_start_12.png)]

### 在game目录中放入SourceHanSansLite.ttf字体(此字体renpy sdk自带,在launcher\game\fonts 路径中)，打开**screens.rpy**文件，在其中搜索 preferences() ，如果你使用的是记事本的格式打开，请使用ctrl+F ，如图所示

[![img](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/quick_start_13.png)]

### 在vbox相同格式下方添加以下代码(注意格式)，如图所示

[![img](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/quick_start_14.png)]

```
                vbox:
                    style_prefix "radio"
                    label _("Language")
                    textbutton _("English") action Language(None)
                    textbutton _("Chinese") text_font "SourceHanSansLite.ttf" action Language("chinese")
```

### 在基础汉化完成以后请在tl目录下新建一个style.rpy文件，如图所示【如果你直接更换了字体，此步骤可以跳过】

[![img](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/quick_start_15.png)]

里面的代码如下

```
translate chinese python:
    gui.system_font = gui.main_font = gui.text_font = gui.name_text_font = gui.interface_text_font = gui.button_text_font = gui.choice_button_text_font = "SourceHanSansLite.ttf"
```

### 请运行游戏，找到设置中的Language，选择Chinese。

[![img](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/quick_start_16.png)]

#### 注意：教程中的多语言支持自带有简体中文，不要搞混淆了。

### 以上的步骤完成以后理论上便可以汉化大部分的游戏文本，如果汉化的文本出现口口字，请查看FAQ