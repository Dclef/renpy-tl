(window.webpackJsonp=window.webpackJsonp||[]).push([[11],{288:function(a,t,s){"use strict";s.r(t);var r=s(10),e=Object(r.a)({},(function(){var a=this,t=a._self._c;return t("ContentSlotsDistributor",{attrs:{"slot-key":a.$parent.slotKey}},[t("h1",{attrs:{id:"_8-0版本的安卓制作-壳子"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#_8-0版本的安卓制作-壳子"}},[a._v("#")]),a._v(" 8.0版本的安卓制作(壳子)")]),a._v(" "),t("p",[a._v("前言：这玩意其实在现在的时间已经有很多汉化者制作了这种类型的游戏，\n也就是一个100MB左右的游戏壳子和一个archive.rpa的大文件。将archive.rpa拖入到指定的目录在运行之前安装的游戏即可流程的运行游戏，不再像以前一样需要安装很长时间和打开闪退之类的。(早在21年renpy就有了这种安装模式，不过那时是末法时间，这里就不做赘述)")]),a._v(" "),t("p",[a._v("接下来就是制作安卓壳子教程。")]),a._v(" "),t("h2",{attrs:{id:"环境准备"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#环境准备"}},[a._v("#")]),a._v(" 环境准备")]),a._v(" "),t("p",[a._v("以下你需要准备以下工具")]),a._v(" "),t("p",[a._v("1.一个魔改版本的renpysdk (请加群获得)")]),a._v(" "),t("p",[a._v("2.一个反编译后的pc版renpy游戏(尽量是原版反编译)")]),a._v(" "),t("h2",{attrs:{id:"_1-整合archive-rpa"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#_1-整合archive-rpa"}},[a._v("#")]),a._v(" 1.整合archive.rpa")]),a._v(" "),t("p",[a._v("当你反编译完以后，进入game目录发现并没有archive.rpa这个东西，而是script.rpa或者是videos.rpa多个rpa文件，这时候你需要重新制作pc版本将其打包成一个archive.rpa文件。")]),a._v(" "),t("p",[t("img",{attrs:{src:"https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-01.png",alt:"image-20240721203359200"}})]),a._v(" "),t("h3",{attrs:{id:"_1-1-修改options-rpy"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#_1-1-修改options-rpy"}},[a._v("#")]),a._v(" 1.1 修改options.rpy")]),a._v(" "),t("p",[a._v("找到options.rpy这个文件，如果没有的话请用工具(如vs code)全局搜索这个代码")]),a._v(" "),t("div",{staticClass:"language- extra-class"},[t("pre",{pre:!0,attrs:{class:"language-text"}},[t("code",[a._v("build.archive\n")])])]),t("p",[a._v("找到以后你会发现有这些代码(每个游戏情况会不一样)")]),a._v(" "),t("p",[t("img",{attrs:{src:"https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-02.png",alt:"image-20240721203535111"}})]),a._v(" "),t("p",[a._v("将videos image gui script audio 全部删掉，替换成如图所示")]),a._v(" "),t("div",{staticClass:"language-python extra-class"},[t("pre",{pre:!0,attrs:{class:"language-python"}},[t("code",[a._v(" build"),t("span",{pre:!0,attrs:{class:"token punctuation"}},[a._v(".")]),a._v("archive"),t("span",{pre:!0,attrs:{class:"token punctuation"}},[a._v("(")]),t("span",{pre:!0,attrs:{class:"token string"}},[a._v("'archive'")]),t("span",{pre:!0,attrs:{class:"token punctuation"}},[a._v(",")]),t("span",{pre:!0,attrs:{class:"token string"}},[a._v("'all'")]),t("span",{pre:!0,attrs:{class:"token punctuation"}},[a._v(")")]),a._v("\n build"),t("span",{pre:!0,attrs:{class:"token punctuation"}},[a._v(".")]),a._v("classify"),t("span",{pre:!0,attrs:{class:"token punctuation"}},[a._v("(")]),t("span",{pre:!0,attrs:{class:"token string"}},[a._v("'game/**'")]),t("span",{pre:!0,attrs:{class:"token punctuation"}},[a._v(",")]),a._v(" "),t("span",{pre:!0,attrs:{class:"token string"}},[a._v("'archive'")]),t("span",{pre:!0,attrs:{class:"token punctuation"}},[a._v(")")]),a._v("\n")])])]),t("p",[t("img",{attrs:{src:"https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-03.png",alt:"image-20240721203810362"}})]),a._v(" "),t("p",[a._v("完成以后关闭并将之前的rpa全部删除(建议做备份)")]),a._v(" "),t("h3",{attrs:{id:"_1-2-制作archive-rpa"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#_1-2-制作archive-rpa"}},[a._v("#")]),a._v(" 1.2 制作archive.rpa")]),a._v(" "),t("p",[a._v("打开魔改版renpy-sdk，选择构建发行版,只勾选windows，然后选择构建,等待构建完毕。")]),a._v(" "),t("p",[a._v("你变会得到一个非常大的archive.rpa文件")]),a._v(" "),t("p",[t("img",{attrs:{src:"https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-04.png",alt:"image-20240721205728400"}})]),a._v(" "),t("h2",{attrs:{id:"_2-制作安卓壳子"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#_2-制作安卓壳子"}},[a._v("#")]),a._v(" 2.制作安卓壳子")]),a._v(" "),t("p",[a._v("打开原版游戏目录，将其中的audio  images video 目录以及exe等文件删除(每个游戏情况会不一样) 如图所示")]),a._v(" "),t("p",[t("img",{attrs:{src:"https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-05.png",alt:"image-20240721205439257"}}),a._v("然后打开打开魔改版renpy-sdk ,选择构建安卓版**(关于如何构建安卓版环境，这里不做赘述)**")]),a._v(" "),t("p",[a._v("在构建应用包名称时请输入你能识别这个游戏的名称(如果安卓上只有这款游戏可忽略)")]),a._v(" "),t("p",[t("img",{attrs:{src:"https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-06.png",alt:"image-20240721205602057"}})]),a._v(" "),t("p",[a._v("然后构建安装包，这时候你会发现安装包会非常小")]),a._v(" "),t("p",[t("img",{attrs:{src:"https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-07.png",alt:"image-20240721210207087"}})]),a._v(" "),t("h2",{attrs:{id:"_3-安装游戏"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#_3-安装游戏"}},[a._v("#")]),a._v(" 3. 安装游戏")]),a._v(" "),t("p",[a._v("将游戏安装后，必须要先运行一次，你会发现能运行，只是说没有图片。"),t("img",{attrs:{src:"https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-08.png",alt:"image-20240721210442537"}})]),a._v(" "),t("p",[a._v("然后退出，用文件管理其找到Documents/RenPy_Saves/ 这个目录")]),a._v(" "),t("p",[t("img",{attrs:{src:"https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-09.png",alt:"image-20240721210528353"}})]),a._v(" "),t("p",[a._v("你会发现安装的游戏就在这里，将archive.rpa丢进游戏的game目录里，如图")]),a._v(" "),t("p",[t("img",{attrs:{src:"https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-10.png",alt:"image-20240721210729076"}})]),a._v(" "),t("p",[a._v("然后再运行游戏你会发现图片回来了，这样就可以进行和PC一样画质的游玩体验，至此，本篇教程结束。")]),a._v(" "),t("p",[t("img",{attrs:{src:"https://cdn.jsdelivr.net/gh/dclef/CDN/img/android_make-11.png",alt:"image-20240721210856066"}})])])}),[],!1,null,null,null);t.default=e.exports}}]);