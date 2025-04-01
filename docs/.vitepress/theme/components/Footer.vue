<!-- Script. -->
<script>
    export default {
        name: "Footer"
    };
</script>

<!-- Template. -->
<template>
    <footer
        id="footer"
        class="relative mt-16 mb-1 flex w-full flex-col items-center justify-center gap-[0.1rem] border-0 p-4 pt-6 text-center text-[0.8rem] font-normal"
    >
        <!-- Add a div containing a border top. -->
        <div
            class="absolute top-0 right-[25%] left-[25%] h-[1px] bg-gradient-to-r from-transparent via-[#cecccb] to-transparent dark:via-[#282b2e]"
        ></div>

        <div>
            Made with
            <span
                class="heart inline-block cursor-default text-[1.15rem] text-[#c41b1b] transition-all duration-500 hover:rotate-[360deg] dark:text-[#c56c6c]"
                >&#9829;</span
            >
            by
            <a
                class="!text-[#3451b2] !no-underline dark:!text-[#a8b1ff]"
                href="https://mihaiconstantin.com"
                target="_blank"
            >
                Mihai Constantin
            </a>
        </div>

        <div class="license-mit !no-underline">
            Software released under the
            <a href="https://opensource.org/license/mit" target="_blank">
                MIT license
            </a>
        </div>

        <div
            class="license-cc !no-underline"
            xmlns:cc="https://creativecommons.org/ns#"
            xmlns:dct="https://purl.org/dc/terms/"
        >
            All other
            <a
                property="dct:title"
                rel="cc:attributionURL"
                href="https://boterview.dev"
            >
                website content
            </a>
            is
            <a
                href="https://creativecommons.org/licenses/by/4.0/"
                target="_blank"
                rel="license noopener noreferrer"
            >
                CC BY 4.0 licensed
            </a>
        </div>
    </footer>
</template>
