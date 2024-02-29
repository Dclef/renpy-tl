如果你只想单纯的提出问题请提交[issues](https://github.com/Dclef/renpy-tl/issues)即可，如果你本身有代码基础或者无基础想参与到本项目中并修改机翻的话，请看以下步骤。

## git 的安装与使用

下载[git](https://git-scm.com/downloads)，下载完成以后安装到本地(网上搜一下安装教程，这里就不多解释)。

安装完成后，在开始菜单里找到“Git”->“Git Bash”，弹一个类似命令行窗口的东西，就说明Git安装成功

接着需要设置一下信息，这台机器上的所有Git仓库都会使用这个配置 （步骤可以省略）

```
$ git config --global user.name "username"
$ git config --global user.email "email@example.com"
```

## vscode中git的使用

安装vscode，如果不会请[点击查看](https://github.com/dclef/renpy-tl#vscode)

默认你已经注册了github账号，请fork我的项目，为了便于理解，这里新创建了一个账号，如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/join_git_1.png)

fork完成以后，便会直接跳转到你的仓库，如图所示。

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/join_git_2.png)

注意：如果项目更新，你需要点击Fetch upstream来更新你的项目，如图所示。

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/join_git_3.png)

打开你的vscode，新建一个文件夹到你的工作区，选择要放入项目的文件夹中，右键在集成终端中打开，请输入git clone代码，如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/join_git_4.png)

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/join_git_5.png)

代码如下

```
git clone 你的git链接
```

clone完成以后，修改你想要汉化文本或添加你要翻译的文本文件。这里仅演示修改文件。

修改完以后请点击左侧第三个按钮，如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/join_git_6.png)

如果首次同步更改会让你去登陆github，如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/join_git_7.png)

会出现允许打开url，如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/join_git_8.png)

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/join_git_9.png)

打开并返回到vscode即可成功更新

## 在你的项目主页中提交request

如果你完成了很多代码修改，请提交一个request，请求合并，如图所示

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/join_git_10.png)

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/join_git_11.png)

![](https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/join_git_12.png)

::: warning 注意
标题以及内容请说明清楚，否则不会合并请求。
:::