# 使用renpy-translator进行翻译

该工具是一款完全开源的翻译工具(完全打renpy-thief的脸)

下载地址：https://github.com/anonymousException/renpy-translator

如果github下载慢，可关注微信公众号老猫的杂货铺搜索renpy-translator直接下载

::: warning 注意

此工具是真正意义上的免费开源，且功能非常完全(只专注于renpy)，可无视我之前翻译教程(除QA)

:::

## 优势

这款工具有以下优势:

1.支持翻译引擎API(可离线AI翻译)

2.支持一键解包(替代unren)

3.支持生成翻译(替代官方工具的生成翻译)

4支持一键翻译(多文件翻译，可跳过重复翻译)

5.支持替换字体(可直接注入翻译设置无需自行添加代码)

6.支持在线润色(支持excel导入导出)

7.可打包游戏(脱离官方打包)

接下来我将以此讲解此工具的优势用途



## 1. 翻译引擎

| 翻译引擎                                                     | 支持翻译语言种类 | 是否需要token          |
| ------------------------------------------------------------ | ---------------- | ---------------------- |
| [Google](https://cloud.google.com/translate/docs/quickstarts) | 108              | Free \| Token Required |
| [Youdao](https://ai.youdao.com/doc.s#guide)                  | 11 \| 114        | Free \| Token Required |
| [Deepl](https://www.deepl.com/account/?utm_source=github&utm_medium=github-python-readme) | 29               | Token Required         |
| [OpenAI](https://platform.openai.com/api-keys)               | 108              | Token Required         |
| [Alibaba](https://translate.alibaba.com/)                    | 214              | Free                   |
| [ModernMt](https://www.modernmt.com/translate)               | 200              | Free                   |
| [Bing](https://www.bing.com/Translator)                      | 133              | Free                   |
| [lingvanex](https://lingvanex.com/demo)                      | 109              | Free                   |
| [CloudTranslation](https://www.cloudtranslation.com/#/translate) | 8                | Free                   |
| [Caiyun](https://fanyi.caiyunapp.com/)                       | 3                | Free                   |
| baidu                                                        | 108              | Token Required         |

你只需要根据官网去申请API即可使用

如果你觉得麻烦可以用免费的API，不过容易被封IP，这里可以使用代理去解决。

该工具还提供了本地AI翻译，如果你显卡牛逼则可以直接使用离线AI进行翻译。

## 2. 解包

原理其实是通过 hook 游戏加载 rpa 包后的节点，将内存中的数据 dump 出来，但解出来的脚本是 rpyc 

需要再结合 unren 反编译（会自动调用），点开工具的高级选项，找到解压游戏包，你只需要把game.exe放进去即可进行解包

自动关闭选项是用来针对某些不在初始化时就加载所有 rpa 包的游戏，需要等相关 rpa 被游戏加载后再关闭

这里又拿老朋友jump来测试了点开高级选项 点击解压游戏包 如图所示

![renpy-translator-01-01](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01-01.png)

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01.png)

![renpy-translator-01-02](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01-02.png)



![renpy-translator-01-03](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01-03.png)你会发现解包成功并且有也有rpy等其他文件

## 3. 生成翻译文件

在反编译翻rpyc后就可以进行生成翻译了，此工具现提供三种翻译模式：

官方抽、抽取翻译、运行抽取

### 3.1 抽取翻译

先说抽取翻译，点开工具的高级选项，找到抽取翻译，如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-03.png)



这里你需要手动去创建chinese才行，否则会生成在tl外面

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-04.png)

抽取完成以后你会发现有很多都是 0Kb，这是没有抽取到吗，其实不然。

这里是因为在游戏中并没有出现文本导致的，也就是说工具的抽取翻译并不会去翻译一些奇奇怪怪的文本。如果你觉得抽取翻译不好用可以使用工具的官方翻译。



### 3.2 官方抽取

官方抽取顾名思义是通过官方工具的抽取原理去翻译，你可以完全无视官方的工具去生成翻译(如果出现翻译错误多半是翻译引擎的问题跟抽取无关)。如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-05.png)

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-06.png)

这里发现没有存在 0kb的文件，如果你觉得抽取翻译好用就用抽取，官方抽取好用就用官方。

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-07.png)

### 3.3 运行抽取

运行抽取是直接通过游戏加载内存hook的模式去抽取，这种大部分是为了去补没有提取到的翻译，此功能需要去斟酌使用，一般是在翻译润色完成以后去校对使用的功能，这里不多做赘述。



## 4. 翻译

当操作完上面的步骤后就可以开始翻译了，如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-08.png)

这里需要注意两点，一点是目标是我们要生成的翻译，源是源游戏的语言。这是使用的是英文游戏。第二点是我们默认的翻译引擎是google，众所周知的缘故需要代理，所以在代理设置里面去设置才能使用(如果是calsh的话默认为 127.0.0.1:7890 )，否则无法翻译，翻译成功以后会有提示，如图所示。



![renpy-translator-01-04](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01-04.png)

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-09.png)



## 5. 添加语言入口

在之前的教程中我们是要手动在**screens.rpy**文件，在其中搜索 preferences()去设置语言入口，这里可以直接注入，打开工具的高级选项，找到添加更改语言入口，如图所示。

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-10.png)

如果出现**success**就代表注入成功


## 6. 替换字体

点开工具的高级选项,找到替换字体，你可以发现字体你可以任意替换的，如图所示。

![renpy-translator-01-05](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01-05.png)

![renpy-translator-01-06](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01-06.png)



你会发现字体是直接注入到tl上的，如果是直接翻译的源码出现口口字，你只需要在源码的gui.rpy上注入字体即可。



## 7. 游戏默认设置中文

打开高级选项，选择设置启动时的默认语言

你只需要把exe文件拖入其中，再将tl的名称输入进去，悬着设置启动时的默认语言即可，如图所示



![renpy-translator-01-09](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01-09.png)

![renpy-translator-01-10](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01-10.png)

![renpy-translator-01-11](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01-11.png)

我们会发现game目录中多了个文件，打开一看是通过python设置的默认语言，这跟以前在screens.rpy上设置的是不一样的，当然你也可以使用以前的方法注入到screens.rpy

```text
define config.language = "chinese"
```



## 8. 润色

打开高级选项中的编辑rpy，你会发现这个功能它是比较复杂的，因为他将本地润色和翻译都做到了里面，所以会有一个translator++既视感

把tl文件直接放在这里面，如图所示 

![renpy-translator-01-07](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01-07.png)

导入以后你会发现在界面中有一个目录你点击它即可(如果文件较多会加载一段时间)，然后即可在线翻译，其次你可以将翻译导出成excel，然后将里面需要润色的翻译放入其中，然后再点击翻译，如图所示

![renpy-translator-01-12](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01-12.png)



![renpy-translator-01-13](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01-13.png)

![renpy-translator-01-14](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01-14.png)

![renpy-translator-01-15](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01-15.png)

![renpy-translator-01-16](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01-16.png)

这样你就会发现润色成功，然后点击上方的保存到文件即可。





## 9. 真·一键翻译

你可以忽略以上6点直接跳到润色章节，因为它将解包、抽取、翻译、翻译设置、替换字体都集成在了一键翻译的功能上，你只需要去润色即可，这极大的加快了翻译进度。如果以上8点都用熟练即可使用此方法，不然一旦遇到错误会发现不知道在哪里入手

打开高级选项选择一键翻译，设置好文件和tl名称以后直接启动即可，如图所示

![renpy-translator-01-18](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01-18.png)




## 10. 打包rpa文件

打开工具的高级功能找到打包功能，如图所示，便可以重新打包rpa文件，可以忽略官方工具的打包功能直接使用此工具即可。比如我把tl文件给打包，如图所示。

![renpy-translator-01-19](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01-19.png)

![renpy-translator-01-20](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01-20.png)

会发现出现了tl.rpa文件，这时候你就可以删除tl文件夹直接使用此文件了。

## 11 利用html进行翻译(白嫖谷歌翻译)

如果你没有代理用不了google，你便可以用这个方法

打开高级选项，选择html转换，导入rpy文本，如图

![renpy-translator-01-21](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01-21.png)

![renpy-translator-01-22](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01-22.png)



然后再从rpy编辑中导入即可，如图所示

![renpy-translator-01-23](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01-23.png)

## 结语

此工具的教程就此完结，当然其中有很多不足也欢迎指正，可以fork这个文档进行更正。

下面我将写下对此工具的评价。

末法时代，在经历了汉化组的灭亡和机翻汉化组的诞生，从t++到翻译君，再到mtool以及renpy-thief。从翻译君的结束，到renpy-thief的谩骂声中逐渐被人遗忘。

有意之士会以此套壳加以倒卖，粗制滥造成为主流。这是不可避免的，正如文档开头那句话，如果人人都会汉化，那么机翻将无路可寻，这便是最初的初衷，也是写这个文档的初衷。

