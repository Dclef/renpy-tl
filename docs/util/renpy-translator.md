# 使用renpy-translator进行翻译

该工具是一款完全开源的翻译工具(完全打renpy-thief的脸)

下载地址：https://github.com/anonymousException/renpy-translator

如果github下载慢，可关注微信公众号老猫的杂货铺搜索renpy-translator直接下载

::: tip

注意： 此工具完全免费开源，且功能非常完全，完全可以无视我之前教程的任何内容（除了QA），且用且珍惜。

:::

## 优势

这款工具有以下优势:

1.支持翻译引擎API(可AI翻译，代理)

2.支持一键解包(替代unren)

3.支持生成翻译(替代官方工具的生成翻译)

4支持一键翻译(多文件翻译，可跳过重复翻译)

5.支持替换字体(可直接注入翻译设置无需自行添加代码)

6.支持在线润色(支持excel导入导出)

7.可打包游戏

8.项目持续更新中。。。

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

你只需要根据官网去申请API即可使用，这里可以看之前申请百度的API教程

当然如果你觉得麻烦可以用免费的API，不过容易被封IP，这里可以使用代理去解决。

当然该工具还提供了本地AI翻译，不过此功能比较鸡肋这里将不再赘述。

## 2. 解包

原理其实是通过 hook 游戏加载 rpa 包后的节点，将内存中的数据 dump 出来，但解出来的脚本是 rpyc ，

需要再结合 unren 反编译（会自动调用），点开工具的高级选项，找到解压游戏包，你只需要把game.exe放进去即可进行解包

自动关闭选项是用来针对某些不在初始化时就加载所有 rpa 包的游戏，需要等相关 rpa 被游戏加载后再关闭

这里又拿老朋友jump来测试了 如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-01.png)

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-02.png)



这里翻译后发现只有rpyc文件，这时候需要unren文件去反编译，文件可在文档QA中获取。

## 3. 生成翻译文件

在反编译翻rpyc后就可以进行生成翻译了，此工具现提供三种翻译模式：

官方抽、抽取翻译、运行抽取

### 3.1 抽取翻译

先说抽取翻译，点开工具的高级选项，找到抽取翻译，如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-03.png)



这里你需要手动去创建chinese才行，否则会生成在tl外面

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-04.png)

抽取完成以后你会发现有很多斗数0Kb，这是没有抽取到吗，其实不然。

这里是因为在游戏中并没有出现文本导致的，也就是说工具的抽取翻译并不会去翻译一些奇奇怪怪的文本。如果你觉得抽取翻译不好用可以使用工具的官方翻译。



### 3.2 官方抽取

官方抽取顾名思义是通过官方工具的抽取原理去翻译，你可以完全无视官方的工具去生成翻译(如果出现翻译错误多半是翻译引擎的问题跟抽取无关)。如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-05.png)

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-06.png)

这里发现没有存在okb的文件，而且生成的模式规则是跟官方的一样，所以如果你觉得抽取翻译好用就用抽取，官方抽取好用就用官方。

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-07.png)

### 3.3 运行抽取

运行抽取是直接通过游戏加载内存hook的模式去抽取，这种大部分是为了去补没有提取到的翻译，此功能需要去斟酌使用，是在翻译润色完成以后去校对使用的功能，这里不再赘述。



## 4. 翻译

当操作完上面的步骤后就可以开始翻译了，如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-08.png)

这里需要注意两点，一点是目标是我们要生成的翻译，源是源游戏的语言。这是使用的是英文游戏。第二点是我们默认的翻译引擎是google，众所周知的缘故需要代理，所以在代理设置里面去设置才能使用(如果是猫的话默认为 127.0.0.1:7890 )，否则无法翻译，翻译成功以后会有提示，如图所示。

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-09.png)



## 5. 注入翻译设置

在之前的教程中我们是要手动在**screens.rpy**文件，在其中搜索 preferences()去设置翻译入口，这里可以直接注入，打开工具的高级选项，找到添加更改语言入口，如图所示。

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-10.png)

如果出现success就代表注入成功


## 6. 替换字体

点开工具的高级选项,找到替换字体，你可以发现字体你可以任意替换的，如图所示。

image

但是它是外部注入的，所以对于报错来讲，你看见的字体还是口口字，这点不必担心。


## 7. 润色

这里要提示一下，对于这个工具的润色功能是只提供润色，但对于机翻报错来讲还是需要通过编程工具(比如vscode)去修改，这点可能会在后续的更新中去解决, 打开高级选项点击编辑rpy,如图所示

你会发现这个功能它是比较复杂的，因为他将本地润色和翻译都做到了里面，所以会有一个translator++既视感(当然也比较像翻译君)。

你只要把tl文件直接放在这里面，如图所示 

导入以后你会发现在界面中有一个目录你点击它即可，然后即可在线翻译，其次你可以将翻译导出成excel，然后将里面需要润色的翻译放入其中，
如图所示。然后点击翻译你会发现润色成功

## 8. 真·一键翻译

你可以忽略以上6点直接跳到润色章节，因为它将解包、抽取、翻译、翻译设置、替换字体都集成在了一键翻译的功能上，你只需要去润色即可，这极大的加快了翻译进度。可谓上乘功能。


## 9. 打包

打开工具的高级功能找到打包功能，如图所示，便可以重新打包一个新游戏，可以忽略官方工具的打包功能直接使用此工具即可。

## 10. 结语

这个简单的工具的教程就此告一段落了，当然其中有很多不足也欢迎指正，可以fork这个文档进行更正。下面我将写下对此工具的评价。

末法时代，在经历了汉化组的灭亡和机翻汉化组的诞生，从t++到翻译君，再到mtool以及renpy-thief。到翻译君的结束，renpy-thief的谩骂声中逐渐被人遗忘。

但互联网之初的开源精神永不磨灭，正因为这样，才会让科技更加进步

当然有意之士会以此套壳加以倒卖，粗制滥造成为主流。这是不可避免的，正如文档开头那句话，如果人人都会汉化，那么机翻将无路可寻，这便是最初的初衷，也是写这个文档的初衷。

:::

持续更新中。。。。。。。。。。
