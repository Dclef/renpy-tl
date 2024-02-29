# 使用Translator++进行翻译

::: warning 注意

此方法不需要生成chinese文件

:::

使用t++方法很简单，你只需要下载[t++](https://pan.baidu.com/s/1VDu1LBDqYAFXfBIpn-kCDQ?pwd=pay2)，打开工程翻译即可。

```
https://pan.baidu.com/s/1VDu1LBDqYAFXfBIpn-kCDQ?pwd=pay2
解压密码：Dreamsavior
```

### 打开一个新工程 如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/translator_1.png)

### 选择要翻译的类型，如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/translator_2.png)

### 选择你游戏目录的exe文件，如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/translator_3.png)

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/translator_4.png)

#### 注意：有rpa文件的建议先解包，然后将rpa文件删除不然容易出现下面这种情况，如图

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/translator_5.png)

#### 打开完以后你会出现以下界面

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/translator_6.png)

##### 这时候就体现了t++的缺点，他将renpy里面的代码也给提取出来了，请不要去翻译。同时也要注意在game目录下的一些文本也不能去翻译，如图

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/translator_7.png)

##### 这里很明显看出这是一个icon目录下的png文件，他也给提取出来翻译了，请不要翻译。

### 选中文件，右键选中批量翻译，如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/translator_8.png)

##### 你可以更换翻译引擎，这里推荐google或者baidu

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/translator_9.png)

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/translator_10.png)

### 导出并覆盖到原文本（建议备份），如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/translator_11.png)

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/translator_12.png)

##### 这样你就成功翻译了该游戏，是不是很简单，之前国内大部分汉化组就是依靠着t++进行翻译（我称之为机翻汉化组），虽然简单但缺点也很明显，文本直接覆盖了，导致没有英文原版，所以下面讲的如何用脚本进行翻译。

:::tip 润色系统

t++的润色系统做的还行，如果机翻完了有时间可以去润色，他分为三种润色，机器翻译，较好的翻译和最好的翻译，实际上三种就是让你做对比，导出时他会根据你是否润色过选择权重最高的翻译，如果你啥都没有润色，就选取inital下的翻译

:::