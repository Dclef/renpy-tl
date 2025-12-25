# 使用RenpyBox进行翻译

现在已经是属于AI新时代了，**末法时代**结束了。如今人人都可以使用AI进行汉化,只是时间快慢而已，所以此工具是集成了Renpy的相关模块制作的集成工具，包含

**解包、反编译、提取翻译、补新翻译、本地词库、禁翻库、使用LLM AI进行翻译、自动填充字体、自动增加中文选项、封包**等功能，因为本人只针对Renpy游戏引擎，所以其他游戏引擎一律不进行优化，请知晓。

**下载地址**：https://github.com/Dclef/renpybox/

::: info 说明

此项目集成了几个项目的结合体,本人也无力去做UI，所以凑合看吧

:::

## 基本配置

接下来就是开始翻译，首先我们打开翻译器，为了保持一致我会下载官网的版本，下载是这个样子，然后我们打开（有惊喜）

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225221316.png)

接着点开接口管理，它跟[LinguaGacha](https://github.com/neavo/LinguaGacha) 是一样的UI（抄的它的，我做的是Renpy的功能）![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225221442.png)

然后我们选中某一个API，请自行设置，这里我用的是deepseek

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225221722.png)

然后返回到项目设置理，找到这里的原文和译文，请看游戏的语言做判断，这里的输入和输出文件夹最好是先去设置，虽然本项目做了自动化的设置但为了防止万一还是先去设置一下。

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225222301.png)

然后点开基础设置，这来到并发和行数可以自行设置，当然你用默认也无所谓，我这里设置成默认的，做完以后就可以进行一键翻译了。

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225222451.png)

## 一键翻译

打开百宝箱，找到一键翻译，如图

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225223530.png)

为了防止意外，我这里也设置了原文和译文的设置

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225223640.png)

输入游戏目录，注意是游戏跟目录，这里还是拿老演员来进行翻译

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225224330.png)

显示提取完成，如图所示，这里可以去看另外一个控制台，那里也有详细的说明

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225224430.png)

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225224521.png)

点击开始翻译，这里就会有术语表和禁翻表，这里先点击自动提取角色名

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225224559.png)

当然你也可以在本地词库里面重新扫描角色名，如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225224718.png)

::: warning 注意

请看到这里会有很多选项，如果你要添加术语库，最好的方式就是自己手动去翻译，因为LLM或者其他都可以翻译不到位，其次这里的自动分类是根据NER的模型去识别分类，有一定概率是识别不到的。然后配置好一定要点击保存到配置！一定要保存配置！

:::



![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225225205.png)

翻译好以后如图所示，接下来需要返回到一键翻译的界面去，点击下一步，开始翻译

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225225310.png)

接下来就是等待翻译完成

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225225417.png)

你会发现有一些报错，但无关紧要

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225232444.png)

点开百宝箱，找到批量修正

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225232604.png)

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225232642.png)

生成相应的EXCEL，如图，这里为了快速演示，就随意修改

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225232752.png)

然后点击注入，即可修正完成

接下来就是第五步，使用工具去处理问题

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225232940.png)

设置默认语言，一键完成

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225233027.png)

语言切换，一键完成

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225233056.png)

字体注入，一键完成（可以忽略，因为一键翻译过程中已经实现这里只是额外的功能）

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225233411.png)

再将out的文件夹迁移到正式的文件夹以后，迁移以后删除out就可以打开游戏了！

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpybox/20251225233902.png)

至此一键翻译流程完成。