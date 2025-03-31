// Imports.
import { defineConfig, type DefaultTheme } from "vitepress";


// Define the website description string.
const description = "boterview is a Large Language Model Interview Toolkit. The premise is simple—from your interview protocol to data generation in moments.";

// https://vitepress.dev/reference/site-config
export default defineConfig({
    // Site configuration.
    title: "boterview",
    lang: "en-US",
    description: description,
    srcDir: "content",
    lastUpdated: true,
    cleanUrls: true,
    metaChunk: true,
    head: [
        // Icons links.
        ["link", { rel: "apple-touch-icon", sizes: "57x57", href: "/apple-icon-57x57.png" }],
        ["link", { rel: "apple-touch-icon", sizes: "60x60", href: "/apple-icon-60x60.png" }],
        ["link", { rel: "apple-touch-icon", sizes: "72x72", href: "/apple-icon-72x72.png" }],
        ["link", { rel: "apple-touch-icon", sizes: "76x76", href: "/apple-icon-76x76.png" }],
        ["link", { rel: "apple-touch-icon", sizes: "114x114", href: "/apple-icon-114x114.png" }],
        ["link", { rel: "apple-touch-icon", sizes: "120x120", href: "/apple-icon-120x120.png" }],
        ["link", { rel: "apple-touch-icon", sizes: "144x144", href: "/apple-icon-144x144.png" }],
        ["link", { rel: "apple-touch-icon", sizes: "152x152", href: "/apple-icon-152x152.png" }],
        ["link", { rel: "apple-touch-icon", sizes: "180x180", href: "/apple-icon-180x180.png" }],
        ["link", { rel: "icon", type: "image/png", sizes: "192x192", href: "/android-icon-192x192.png" }],
        ["link", { rel: "icon", type: "image/png", sizes: "32x32", href: "/favicon-32x32.png" }],
        ["link", { rel: "icon", type: "image/png", sizes: "96x96", href: "/favicon-96x96.png" }],
        ["link", { rel: "icon", type: "image/png", sizes: "16x16", href: "/favicon-16x16.png" }],
        ["link", { rel: "manifest", href: "/manifest.json" }],
        ["meta", { name: "msapplication-TileColor", content: "#ffffff" }],
        ["meta", { name: "msapplication-TileImage", content: "/ms-icon-144x144.png" }],
        ["meta", { name: "theme-color", content: "#ffffff" }],

        // Social media links.
        ["meta", { property: "og:site_name", content: "boterview" }],
        ["meta", { property: "og:description", content: description }],
        ["meta", { property: "og:image", content: "/images/boterview-og-light.png" }],
        ["meta", { property: "og:url", content: "https://boterview.dev" }],
        ["meta", { property: "og:type", content: "website" }],
        ["meta", { name: "twitter:card", content: "summary_large_image" }],
        ["meta", { name: "twitter:title", content: "boterview" }],
        ["meta", { name: "twitter:description", content: description }],
        ["meta", { name: "twitter:image", content: "/images/boterview-og-light.png" }],
    ],

    // Theme configuration.
    themeConfig: {
        logo: {
            src: "/images/boterview-logo-square-small.png", width: 24, height: 24, draggable: false,
        },
        socialLinks: [
            { icon: "github", link: "https://github.com/mihaiconstantin/boterview" }
        ],
        nav: [
            { text: "Guide", link: "/guide/what-is-boterview" },
            { text: "Reference", link: "/reference/study-config" },
        ],
        editLink: {
            pattern:
                "https://github.com/mihaiconstantin/boterview/edit/main/docs/:path",
            text: "Edit this page on GitHub",
        }
    }
});
