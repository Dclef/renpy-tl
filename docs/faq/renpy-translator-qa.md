# renpy-translator QA

来源于[官方的文档](https://github.com/anonymousException/renpy-translator/blob/main/README_zh.md)，这里再总结一次

### 翻译全都被跳过了

[![skip](https://github.com/anonymousException/renpy-translator/raw/main/docs/img/translation_all_skip.png)](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/translation_all_skip.png)

确保在官方抽取环节, 对于 "Generate Translations" (生成翻译) 选项, 不要勾选 "Generate empty strings for translations"(为翻译生成空子串)

翻译只会在满足下面格式时生效:

```
# game/script.rpy:553
translate schinese naming_0f7b6e71:
	# r "Do name yourself like that and I'll break your face..."
	r "Do name yourself like that and I'll break your face..."
```

or

```
    # game/script.rpy:30886
    old "Win or Lose?"
    new "Win or Lose?"
```

注意原始文本(在 # 或 old 后) 应该和未翻译的文本(在非 # 或 new 后)**完全一样**



### 有些错误导致某些行无法被翻译

你可能会遇到像这样的错误 :

```
2024-01-30 14:55:19 D:\Download\Nova-Pasta\SunshineLoveCH2-1.01-pc\game\tl\Portugues/10_week10_00.rpy Error in line:1320
It’s [s_name]. And [y_name].
It’s [0] . And [1] .
É [0] . E 1] .
Error
```

这取决于翻译的结果，为了跳过翻译特殊符号像 '[]' '{}' '<>' , 这个工具将用按顺序的数字替换特殊字符 举个例子: "It’s [s_name]. And [y_name]." 将会被替换为 "It’s [0] . And [1] ."

通常来说，这种格式将不会被翻译且会保留 '[0]' 和 '[1]' ，并且这个工具将会根据这个有序数字还原原本的内容

然而，有时这种格式会在翻译后被破坏，正如前面提到的： "É [0] . E 1] ." 你会发现 '[' 丢了，所以本工具无法还原原本的内容，因此这行文本不会被翻译 你可能需要手动修正这些行 幸运的是这种情况很少发生，你不会花费很多时间在修正这些行上

目前谷歌是用来翻译这些包含特殊符号内容的最好的选择 , 你可以用谷歌重新翻译这些内容

### 杀毒软件报毒



~~这个软件是用 pyinstaller 打包的，且因为有文件操作(打开 读 写) ，因此可能会有误检测~~

~~如果你对此表示担忧，你可以自己下载源码并运行~~

Pyinstaller 构建的版本很容易被误检测为病毒

如果你对此表示担忧 , 可以尝试 Nuitka 构建的版本(Nuitka.Build 或 RenpyTranslatorInstaller)

### 运行翻译后的游戏报错



当你翻译完游戏运行后可以会遇到类似下面的报错

[![error_after_translation](https://github.com/anonymousException/renpy-translator/raw/main/docs/img/error_after_translation.png)](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/error_after_translation.png)

[![error_after_translation_source](https://github.com/anonymousException/renpy-translator/raw/main/docs/img/error_after_translation_source.png)](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/error_after_translation_source.png)

不难发现在翻译过后 "[[XXXX]" 被翻译成了"[ [XXXX]" , 多了个空格 (你遇到的可能是其它形式的错误，但重点在于在翻译后**特殊符号的结构被破坏**了)

这个结果是翻译引擎翻译导致的 , 有时翻译引擎对特殊符号像 '[]' '<>' ... **不太友好** 特别是当特殊符号叠加使用时

但仍然有个好消息 , 通常这种情况不会很频繁发生，你只需要手动处理这些错误的句子 (对于我在上面提到的这个案例 , 只需要删除多余的空格即可)

### 有些句子在翻译过后好像没生效

#### tooltip

对于在 **tooltip** 里的特殊文本，明明翻译了却没生效

原始的代码看起来像这样 :

```
tooltip "this is a tooltip"
```

只需要打开 rpy 文件 (随便一个在 tl 文件夹底下的或你可以自己创一个) 并添加以下代码

```
#如果是自己创建的话，需要补上下面这行去掉 # , tl_name 填 tl 目录下的文件夹名称如 schinese
#translate tl_name strings:
    old "[tooltip]"
    new "[tooltip!t]"
```

#### notify

对于在 **notify** 里的特殊文本 ，明明翻译了却没生效

你需要定位没被翻译的句子在原本代码里的位置 (不是在翻译的 tl 文件夹下)

你将会找到看起来像这样的原始代码 :

```
show screen notify(_("Find old Man Gibson"), None)
```

------

替换为

```
show screen notify(__("Find old Man Gibson"), None)
```

操作只是在notify( 后添加 '_'

很简单对吧? 然后翻译就能生效了

### 其它

可能会有其它情况，有些句子在翻译后仍然没生效

这取决于原始的代码，抽取可能不能完全覆盖如果原始代码写得不是那么得对翻译友好

为了避免多余的无效抽取，本工具的抽取功能不会抽取满足以下格式的句子：

句子长度小于 8 (空格和特殊符号长度被记为 0)

举个例子 :

```
"I know [special symbol]"
```

实际有效的内容是：

```
Iknow
```

长度只有 5 , 所以它不会被本工具的抽取功能抽取

### 在抽取后生成的奇怪内容

在抽取后你会看到类似下面的内容

```
old "old:1709016761.706834_0.8853030081254853"
new "new:1709016761.706834_0.8853030081254853"
```



这是一个不重复的时间戳用来标记你抽取的时间，格式是 时间戳_随机数(随机数是为了确保生成的内容不重复否则会引起错误)

你可以转换在 '_' 前的部分 (本例是1709016761.706834) 为可读的时间通过 https://www.epochconverter.com/ 或其它能转换时间戳的网站

### OpenAI



你可以在 : [rate-limits](https://platform.openai.com/account/rate-limits) 查看速率限制并设置一个合理的限制

如果是 OpenAI 新用户，每分钟请求数最多 3 个，基本无法使用

默认设置就是针对这种情况 ，如果你不在意多花点时间 ,你可以使用默认设置

对于更高权限的用户 , 推荐提高配置 推荐配置如下

| 参数                       | 推荐                                                         |
| -------------------------- | ------------------------------------------------------------ |
| RPM(requests per minute)   | 250                                                          |
| RPS(requests per second)   | 10                                                           |
| TPM(requests token limits) | [rate-limits](https://platform.openai.com/account/rate-limits) |
| model                      | gpt-3.5-turbo \| gpt-4 (更智能但更贵)                        |

#### 有些错误导致某些行无法被翻译

OpenAI 似乎对像 '{}' '[]' 的特殊符号不太友好 ,你可以用谷歌翻译重新翻译这些错误的行 (已经被翻译过的行将会被**自动跳过**，只需要重新翻译之前翻译过的整个目录或文件即可)

(谷歌翻译会对这些特殊符号更友好但仍然可能留下一点点错误)

最后你需要手动处理剩下的一点点错误

除此之外如果你在使用 openai 时遇到 traceback 错误 ， 尝试禁用 Multi-Translate 选项，并重新翻译 (更稳定但会慢一些)

### JSONDecodeError

你可能遇到如下错误:

```
2024-02-22 11:18:28	Traceback (most recent call last):
  File "openai_translate.py", line 180, in translate_limit
  File "json\__init__.py", line 346, in loads
  File "json\decoder.py", line 337, in decode
  File "json\decoder.py", line 353, in raw_decode
json.decoder.JSONDecodeError: Unterminated string starting at: line 1 column 1613 (char 1612)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "openai_translate.py", line 187, in translate_limit
Exception: Unterminated string starting at: line 1 column 1613 (char 1612)
```



这是由于 openai 返回了错误的数据格式 , 幸运的是这并不会频繁发生并且只会导致一个文件部分内容未被成功翻译，你可以用其它翻译引擎像谷歌翻译来重新翻译这些未被翻译的行

### 不匹配的翻译结果



你可能会遇到如下报错：

```
2024-02-23 10:19:34 translated result can not match the untranslated contents
```

原因在于 open-ai 可能会偶然把多个翻译结果混合成一个 , 例如 :

```
#untranslated
["Hello","Good"]
#translated
["こんにちは,良い"]
```



这会导致翻译结果的不匹配 ， 因此这部分内容的翻译不会生效 , 你可能需要用其它翻译引擎翻译这些未翻译的内容

### ConnectError

你可能会遇到如下报错：

```
2024-02-23 10:19:34	Another non-200-range status code was received:400 <Response [400 Bad Request]>
2024-02-23 10:19:34	Error code: 400 - {'error': {'message': 'Connection error (request id: 20240223101928248984704uoEfBgvh)', 'type': '', 'param': '', 'code': 'connection_error'}}
2024-02-23 10:19:34	['untranslated1','untranslated2','....']
```



这取决于你的网络环境，重新翻译可能就可以了