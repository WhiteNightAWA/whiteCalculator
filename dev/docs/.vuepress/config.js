const { config } = require("vuepress-theme-hope");

module.exports = config({
    lang: "en-US",
    title: "White Calculator",
    description: "By WhiteNight",
    base: "/whiteCalculator/",
    icon: "/logo.svg",
    edEnhance: {
        enableAll: true,
    },
    themeConfig: {
        logo: "/logo.svg",
        darkMode: true,

// ========================================NAVBAR========================================
        editLink: false,
        nav: [
            { text: "HOME", link: "/", icon: "home" },
            { text: "GUIDE", link: "/guide/", icon: "creative" },
            { text: "DOCS", link: "/docs/", icon: "file" },
            { text: "GitHub", link: "https://github.com/WhiteNightAWA/whiteCalculator", icon: "github" },
            { text: "Pypi", link: "https://pypi.org/project/whiteCalculator", icon: "module" },
            { text: "Report bugs", link: "https://github.com/WhiteNightAWA/whiteCalculator/issues/new", icon: "debug" },
        ],
        search: true,
        searchMaxSuggestions: 10,
        searchPlaceholder: "Search about...",
        themeColor: false,
        darkmode: "switch",
        fullscreen: false,

// ========================================SIDEBAR========================================
        displayAllHeaders: true,
        activeHeaderLinks: false,
        sidebar: {
                "/guide/": [
                    {
                        title: "GUIDE",
                        icon: "creative",
                        path: "/guide/",
                        prefix: "/guide/",
                        collapsable: false,
                        children: [
                            "Introduction",
                            "Installation",
                            "QuickStart",
                        ],
                    }
                ],
                "/docs/": [
                    {
                        title: "Documentation",
                        icon: "file",
                        path: "/docs/",
                        prefix: "/docs/",
                        sidebarDepth: 2,
                        collapsable: false,
                        children: [
                            "Calculator",
                            "Formula",
                            "Others",
                        ],
                    }
                ]
            },
        },
// ========================================PLUGINS========================================
        plugins: [
            [
                "md-enhance",
                {
                    tex: true,
                    sub: true,
                    sup: true,
                },
            ],
        ],
    },
);