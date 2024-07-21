module.exports = {
  plugins: [
    ['@vuepress/back-to-top', true],
    ['google-analytics-4', {
      gtag: 'G-Z5QTK2B6PL'
    }]
  ],
  // base: './',   // 部署的路径配置
  // dest: './dist',  // 设置输出目录
  title: 'renpy游戏汉化教程',
  description: '末法时代的汉化教程',
  themeConfig: {
    lastUpdated: 'Last Updated', // string | boolean
    smoothScroll: true,
    docsRepo: 'dclef/renpy-tl',
    // 假如文档不是放在仓库的根目录下：
    docsDir: 'docs',
    // 假如文档放在一个特定的分支下：
    // docsBranch: 'gh-pages',
    docsBranch: 'master',
    // 默认是 false, 设置为 true 来启用
    editLinks: true,
    // 默认为 "Edit this page"
    editLinkText: '如果有误请编辑此页',
    repo: 'dclef/renpy-tl',
    // 自定义仓库链接文字。默认从 `themeConfig.repo` 中自动推断为
    // "GitHub"/"GitLab"/"Bitbucket" 其中之一，或是 "Source"。
    repoLabel: 'Github',
    nextLinks: true,
    // 默认值是 true 。设置为 false 来禁用所有页面的 上一篇 链接
    prevLinks: true,
    nav: [
      {
        text: 'Guide',
        items: [
          { text: '简介', link: '/guide/' },
          { text: '快速开始', link: '/guide/quick_start' },
          { text: '进阶', link: '/guide/vscode.md' },
          { text: '8.0新特性', items:[
              {text:'新版本区别',link: '/guide/new_version.md' },
              {text: '制作安卓(壳子)',link: '/guide/android_make.md'}
            ]
          }
        ]
      },
      {
        text: '翻译工具',
        items: [
          { text: '介绍', link: '/util/' },
          { text: 'excel汉化(已过时)', link: '/util/excel' },
          { text: '自制脚本汉化(已过时)', link: '/util/trans' },
          { text: 'Translator++工具汉化(新手不推荐)', link: '/util/Translator' },
          { text: '自制工具箱汉化(推荐)', link: '/util/renpytool' },
          { text: 'renpy-translator(推荐)', link: '/util/renpy-translator' },
        ]
      },
      {
        text: 'FAQ',
        items: [
          { text: '提交方式', link: '/faq/' },
          { text: '问题汇总', link: '/faq/qa' }
        ]
      },
      { 
        text:'协同翻译',
        items:[
          {text: '使用git进行协同翻译', link: '/join/' },
          {text: '使用paratranz进行协同翻译', link: '/join/paratranz' }
        ]
      
      },
      { text: '支持', link: '/support/' }



    ],
    sidebar: {
      // '/guide/': [
      //     {
      //         title: '简介',
      //         path: '/guide/'
      //     }
      // ],
      '/guide/': [
        {
          title: '简介',
          children: [
            {
              title: '介绍',
              path: '/guide/'
            },
            {
              title: '开始',
              path: '/guide/quick_start'
            },
            {
              title: '进阶',
              path: '/guide/vscode'
            },
          ],
        },
        {
          title: '8.0新特性',
          children: [
            {
              title: '介绍',
              path: '/guide/new_version'
            },
              {
              title: '制作安卓壳子',
              path: '/guide/android_make'
              },
          ]
        }
      ],
      '/util/': [
        {
          title: '翻译工具使用',
          children: [
            {
              title: '介绍',
              path: '/util/'
            },
            {
              title: 'excel汉化(已过时)',
              path: '/util/excel'
            },
            {
              title: '自制脚本汉化(已过时)',
              path: '/util/trans'
            },
            {
              title: 'Translator++工具汉化(新手不推荐)',
              path: '/util/Translator'
            },
            {
              title: '自制工具箱汉化(推荐)',
              path: '/util/renpytool'
            }, 
            {
              title: 'renpy-translator(推荐)',
              path: '/util/renpy-translator'
            },

          ]
        }
      ],
      '/faq/': [
        {
          title: '常见问题',
          sidebarDepth: 2,
          children: [
            {
              title: '介绍',
              path: '/faq/'
            },
            {
              title: '问题汇总',
              path: '/faq/qa'
            },
          ]
        }
      ],
      '/join/': [
        {
          title: '协同翻译',
          children: [
            {
              title: '使用git进行协同翻译',
              path: '/join/'
            },
             {
              title: '使用paratranz进行协同翻译',
              path: '/join/paratranz'
            },
          ]
        }
      ],
      '/support/': [
        {
          title: '支持',
          children: [
            {
              title: '支持本教程',
              path: '/support/'
            }
          ]
        }
      ],
    }
    // sidebar: 'auto'
  }



}