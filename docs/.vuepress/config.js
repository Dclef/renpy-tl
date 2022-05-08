module.exports = {
 // base: './',   // 部署的路径配置
 // dest: './dist',  // 设置输出目录
  title: 'renpy游戏汉化教程',
  description: '末法时代的汉化教程',
  themeConfig: {
    docsRepo: 'dclef/renpy-tl',
    // 假如文档不是放在仓库的根目录下：
    docsDir: 'docs',
    // 假如文档放在一个特定的分支下：
    docsBranch: 'master',
    // 默认是 false, 设置为 true 来启用
    editLinks: true,
    // 默认为 "Edit this page"
    editLinkText: '编辑此页',
    repo: 'dclef/renpy-tl',
    // 自定义仓库链接文字。默认从 `themeConfig.repo` 中自动推断为
    // "GitHub"/"GitLab"/"Bitbucket" 其中之一，或是 "Source"。
    repoLabel: 'Github',
    lastUpdated: 'Last Updated', // string | boolean
    nextLinks: true,
    // 默认值是 true 。设置为 false 来禁用所有页面的 上一篇 链接
    prevLinks: true,
    nav: [
        { 
          text: 'Guide',
          items: [
          { text: '简介', link: '/guide/' },
          { text: '快速开始', link: '/guide/quick_start' },
          { text: '进阶', link: '/guide/vscode.md' }
        ]
      }, 
      { 
        text: '翻译工具',
        items: [
        { text: '介绍', link: '/util/' },
        { text: 'excel汉化', link: '/util/excel' },
        { text: 'Translator++工具汉化', link: '/util/Translator' },
        { text: '自制脚本汉化', link: '/util/trans' },
      ]
    }, 
      { 
          text: 'FAQ',
          items: [
          { text: '提交方式', link: '/faq/' },
          { text: '问题汇总', link: '/faq/qa' }
        ]
      },
      { text: '参与', link: '/join/' },
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
                    title: 'excel汉化',
                    path: '/util/excel'
                }, 
                {
                    title: 'Translator++工具汉化',
                    path: '/util/Translator'
                }, 
                {
                    title: '自制脚本汉化',
                    path: '/util/trans'
                }
            
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
            title: '参与',
            children: [
              {
                  title: '参与本项目',
                  path: '/join/'
              }
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