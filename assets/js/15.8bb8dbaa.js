(window.webpackJsonp=window.webpackJsonp||[]).push([[15],{293:function(t,a,r){"use strict";r.r(a);var _=r(10),s=Object(_.a)({},(function(){var t=this,a=t._self._c;return a("ContentSlotsDistributor",{attrs:{"slot-key":t.$parent.slotKey}},[a("h1",{attrs:{id:"paratranz的使用"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#paratranz的使用"}},[t._v("#")]),t._v(" paratranz的使用")]),t._v(" "),a("h2",{attrs:{id:"介绍"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#介绍"}},[t._v("#")]),t._v(" 介绍")]),t._v(" "),a("p",[t._v("顾名思义是指主打P社四萌的云翻译平台，相对于GitHub 作为协作平台，用 git 管理翻译项目，并通过分支来合并翻译来讲。这种操作对于非程序员十分不友好，所以使用paratranz这个云翻译平台会大大降低协作翻译的学习成本。")]),t._v(" "),a("h2",{attrs:{id:"环境准备"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#环境准备"}},[t._v("#")]),t._v(" 环境准备")]),t._v(" "),a("p",[t._v("一个github账号(如果没有请在"),a("a",{attrs:{href:"https://github.com/join",target:"_blank",rel:"noopener noreferrer"}},[t._v("https://github.com/join"),a("OutboundLink")],1),t._v("中创建GitHub账号)")]),t._v(" "),a("p",[t._v("一个生成tl翻译文件夹的renpy游戏")]),t._v(" "),a("p",[t._v("paratranz网站 (https://paratranz.cn/projects)")]),t._v(" "),a("h2",{attrs:{id:"使用方法"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#使用方法"}},[t._v("#")]),t._v(" 使用方法")]),t._v(" "),a("h3",{attrs:{id:"创建项目"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#创建项目"}},[t._v("#")]),t._v(" 创建项目")]),t._v(" "),a("p",[t._v("登录好paratranz网站后点击右上角创建项目将会来到以下界面")]),t._v(" "),a("p",[a("img",{attrs:{src:"https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/Snipaste_2023-01-08_22-01-45.png",alt:""}})]),t._v(" "),a("p",[t._v("这里只需要注意一点的就是请将所属游戏更换成Ren'py Engine 不然导入文件时会显示不支持rpy格式的文件，其余可以酌情选择。")]),t._v(" "),a("h3",{attrs:{id:"文件管理"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#文件管理"}},[t._v("#")]),t._v(" 文件管理")]),t._v(" "),a("p",[t._v("当然，创建完项目以后接下来就得导入文件，在该页面中管理可以添加、更新、删除与重命名文件，也可从汉化的文件中批量导入译文。如图")]),t._v(" "),a("p",[a("img",{attrs:{src:"https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/renpy_paratranz_02.png",alt:""}})]),t._v(" "),a("p",[t._v("首先选择“新建文件夹”新建和本地文件名字相同的文件夹，点击进入该文件夹并选择“添加文件”，在文件管理器中选中所有对应的rpy文件即可进行文件的上传。")]),t._v(" "),a("p",[t._v("::⚠️")]),t._v(" "),a("p",[t._v("注意：导入时由于平台的限制或生成tl的rpy文件中首行有空行以及键值对不能大写等因素(这里指的是出现有大写的情况例如：translate chinese previousELabel_b1c5a88a:)会出现导入不进去的问题。导入时如果出现这些问题请自行查看有问题的文件并根据以上的描述去解决。")]),t._v(" "),a("p",[t._v(":::")]),t._v(" "),a("h3",{attrs:{id:"翻译"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#翻译"}},[t._v("#")]),t._v(" 翻译")]),t._v(" "),a("p",[t._v("导入完成以后返回到首页点击文件，左侧会显示该文件内的词条，默认只显示未翻译的词条，如果你想查看已翻译的或全部词条，请点击右边的按钮，并选择相应的筛选条件，右下角可以调整每页显示的词条数量。如图")]),t._v(" "),a("p",[a("img",{attrs:{src:"https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/renpy_paratranz_03.png",alt:""}})]),t._v(" "),a("p",[t._v("接下来是主要翻译部分，从上到下分别是词条状态、原文、译文、键值、所在文件以及功能按钮。其中的键值指的是rpy文件中的翻译事件对应的键值对，例如translate chinese previousELabel_b1c5a88a:。")]),t._v(" "),a("p",[t._v("在译文框中输入译文后，可按保存按钮（快捷键Ctrl+S）保存，如果感觉此条翻译中存在问题，可其标为有疑问（快捷键Ctrl+D）。")]),t._v(" "),a("p",[t._v("再向下看你可以看到一系列翻译建议，这玩意就真是建议，请不要直接复制粘贴，还是要根据语境判断翻译是否合理。")]),t._v(" "),a("p",[t._v("右边栏分历史、术语、注释三栏。")]),t._v(" "),a("p",[t._v("历史栏显示该词条的导入与编辑历史。")]),t._v(" "),a("p",[t._v("术语栏为本项目或其他公开项目的术语。")]),t._v(" "),a("p",[t._v("注释栏为翻译人员对本词条的注释。")]),t._v(" "),a("p",[t._v("事实上对于renpy所做的游戏来讲，不会涉及太深的俚语以及历史因素来源，所以这三个可以当作不存在，用此功能只会浪费时间。")]),t._v(" "),a("p",[t._v("以下是注释图")]),t._v(" "),a("p",[a("img",{attrs:{src:"https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/renpy_paratranz_04.png",alt:""}})]),t._v(" "),a("h3",{attrs:{id:"校对"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#校对"}},[t._v("#")]),t._v(" 校对")]),t._v(" "),a("p",[t._v("翻译完成以后接下来就是校对，也就是所谓的审核。如果在翻译时就已经将机翻变为手动翻译等一系列操作完成以后这步其实可以省略。审核完成以后会在项目界面中添加个标签显示为已完成。")]),t._v(" "),a("h3",{attrs:{id:"下载翻译文件"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#下载翻译文件"}},[t._v("#")]),t._v(" 下载翻译文件")]),t._v(" "),a("p",[t._v("翻译校对完成就是下载该文件了，点击项目主页选择下载选项，如果是刚翻译完成以后请使用重新生成压缩包，此平台是在在词条有修改的情况下每一小时更新一次，所以如果没有重新生成下载的会是没有翻译过的文件。如图")]),t._v(" "),a("p",[a("img",{attrs:{src:"https://cdn.jsdelivr.net/gh/dclef/CDN/renpy/renpy_paratranz_05.png",alt:""}})])])}),[],!1,null,null,null);a.default=s.exports}}]);