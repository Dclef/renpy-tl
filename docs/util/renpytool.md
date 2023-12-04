# 使用自制工具箱翻译

::: warning 注意

需关注微信公众号【老猫的杂货店】并加群获得

:::

首先先感谢katharsis提供的支持，这里是根据上面所述的excel汉化以及api翻译所做的整合包。

**首先先看界面，为了便于理解这里从左到右依次讲解**

## 文件移动和还原

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/renpytool-01.png)



#### 移动-----当前文件夹下所有rpy文件移动到当前文件夹（包括子文件夹）

此步骤需要将此程序放置在游戏game目录中的tl文件夹中(**此步骤是所有步骤最初的第一步**)

如![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/renpytool-14.png)

#### 还原-----移动的rpy文件还原回原文件夹

将tl中的rpy文件还原到原文件中

#### 清除-----清除文本框内容



## 利用腾讯api翻译(不可用)

因为百度api不能无限使用的原因，这里就推荐使用腾讯的api，每月500W字符

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/renpytool-02.png)

#### 翻译-----使用腾讯api翻译文件夹下 ””renpy生成翻译文件””

需要先移动文件夹才能进行翻译

#### 删除-----build_new中翻译文件替换到未翻译文件，之后删除生

#### 成文件

#### 清除-----清除文本框内容



![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/renpytool-03.png)



#### 设置-----填入腾讯api后保存



## 使用google游览器网页进行翻译

**这其实是excel的升级版，其原理还是一样的，所以推荐使用这种方法**

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/renpytool-04.png)



#### 先将所有文件移动到外面，然后点击生成翻译文件

并生成1、2、3、4文件

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/renpytool-05.png)

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/renpytool-06.png)

#### 右键或者将第二个文件丢进google游览器里，右键翻译成中文

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/renpytool-07.png)

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/renpytool-08.png)

#### 全选，全部复制到3_CN.rpy中

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/renpytool-08.png)



#### 合并-----将3_CN.rpy中翻译合并到1_alltxt.rpy

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/renpytool-10.png)

#### 分割rpy文件-----将所有rpy文件合并形成的1_alltxt.rpy分割为原rpy文件

#### 删除-----之后删除生成文件

#### 清除-----清除文本框内容



## menu提取并进行按钮翻译

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/renpytool-11.png)

#### 将该文件放置在game\\tl\\language文件夹下(language为你--生成翻译文件文件夹)



#### 提取-----扫描game路径下游戏选项，并将提取到选项保存在game\\tl\\language文件夹下menu.rpy文件中（若文件夹下有menu.rpy文件请注意！！！）



#### 汉化-----使用已翻译的menu.rpy文件，将源码中选项替换（源码操作，可能会导致游戏打不开，请慎重使用！）

这一步请与上一步的google_tran进行同时翻译

#### 清除-----清除文本框内容

## 润色

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/renpytool-12.png)

#### 文润-----仅在译文中润色，对工具所在文件夹下所有rpy文件进行润色，包括子文件夹内文件。

**注意只能在new与译文里润色**

```
old "Self-voicing disabled."
new "自动发声已禁用。"
```

#### 全局-----对rpy文件所有信息进行润色，对工具所在文件夹下所有rpy文件进行润色，包括子文件夹内文件。

**这里指如果直接翻译的源码可进行直接进行润色**
