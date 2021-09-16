module.exports = {
  lang: "en",
  title: "White Calculator",
  description: "By WhiteNight",
  darkMode: true,
  themeConfig: {
    // logo: "https://i.ibb.co/wgvwXKY/logo.png",
    navbar: [
      { text: "GUIDE", link: "/GUIDE/Installation.md" },
      {
        text: "DOCS", children: [
          { text: "Calculator", link: "/DOCS/Calculator" }
        ]
      },
      { text: "Github", link: "https://github.com/WhiteNightAWA/whiteCalculator" },
      { text: "Pypi", link: "https://pypi.org/project/whiteCalculator" }
    ],
    sidebar: {
      "/GUIDE/": [
        { text: "GUIDE", children: [
            // "/GUIDE/Introduction.md", "/GUIDE/Installation.md.md", "/GUIDE/IQuickStart.md"
            { text: "Introduction", link: "/GUIDE/Introduction.md" },
            { text: "Installation", link: "/GUIDE/Installation.md" },
            { text: "Quick Start", link: "/GUIDE/QuickStart.md", children: [
                { text: "Calculator", link: "/GUIDE/QuickStart.md#calculator" },
                { text: "Formula", link: "/GUIDE/QuickStart.md#formula" }
              ]
            },
          ]
        }
      ]
    },
  },
  plugins: [
    [
      '@vuepress/plugin-search',
      {
        locales: {
          '/': {
            placeholder: 'Search',
          },
        },
      },
    ],
  ],
}