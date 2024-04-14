# 使用[renpy-translator](https://github.com/anonymousException/renpy-translator/tree/main)进行翻译

该工具是一款完全开源的翻译工具(完全打renpy-thief的脸)

下载地址：https://github.com/anonymousException/renpy-translator

如果github下载慢，可关注微信公众号老猫的杂货铺直接下载

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

原理其实是通过Unren的工具实现，这里也自带了，点开工具的高级选项，找到解压游戏包，你只需要把game.exe放进去即可进行解包

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



## 5 注入翻译设置

在之前的教程中我们是要手动在**screens.rpy**文件，在其中搜索 preferences()去设置翻译入口，这里可以直接注入，打开工具的高级选项，找到添加更改语言入口，如图所示。

![](https://cdn.jsdelivr.net/gh/dclef/CDN/img/renpy-translator-10.png)

如果出现success就代表注入成功
