<!-- Template. -->
<template>
    <footer
        id="footer"
        class="relative mt-6 mb-1 flex w-full flex-col items-center justify-center gap-2 border-0 p-4 pt-5 text-center text-sm font-normal"
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
                class="!text-[var(--vp-c-brand-1)]"
                href="https://mihaiconstantin.com"
                target="_blank"
            >
                Mihai Constantin
            </a>
        </div>

        <div class="!text-decoration-none">
            <a href="https://opensource.org/license/mit/" target="_blank">
                MIT licensed
            </a>
        </div>
    </footer>
</template>

<!-- Script. -->
<script>
export default {
    name: "Footer"
};
</script>
