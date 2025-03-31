<!-- Template. -->
<template>
    <div
        id="hero"
        class="mt-16 mb-16 border-0 px-[24px] min-[640px]:px-[48px] min-[960px]:mt-20 min-[960px]:mb-21 min-[960px]:px-[64px]"
    >
        <div class="mx-auto max-w-[1152px] border-0">
            <!-- Main hero content. -->
            <div
                class="flex flex-col-reverse items-center gap-10 border-0 min-[960px]:flex-row min-[960px]:gap-25"
            >
                <!-- Hero title and description. -->
                <div
                    class="flex flex-col items-center border-0 text-center min-[960px]:w-[570px] min-[960px]:items-start min-[960px]:text-left"
                >
                    <!-- Title. -->
                    <h1
                        class="title font-boterview from-boterview-500 dark:from-boterview-400 !mb-[6px] bg-gradient-to-r from-[50px] to-[var(--vp-c-text-1)] to-[80px] bg-clip-text !text-5xl !font-bold text-transparent"
                    >
                        boterview
                    </h1>

                    <!-- Text. -->
                    <div
                        class="mb-3 border-0 text-3xl leading-10 font-light max-[960px]:w-[500px] min-[460px]:w-[400px] min-[960px]:w-full min-[960px]:text-5xl min-[960px]:leading-14"
                    >
                        Large Language Model Interview Toolkit
                    </div>

                    <!-- Tagline. -->
                    <div
                        class="border-0 text-lg leading-8 font-light text-[var(--vp-c-text-2)] max-[960px]:w-[500px] min-[460px]:w-[400px] min-[960px]:w-full min-[960px]:text-2xl min-[960px]:leading-9"
                    >
                        The premise is simple—from
                        <span
                            class="text-boterview-500 dark:text-boterview-400 italic"
                            >your</span
                        >
                        interview protocol to data generation in moments.
                    </div>

                    <!-- Action button. -->
                    <div class="mt-6 border-0">
                        <button
                            class="!bg-boterview-500 hover:!bg-boterview-600 active:!bg-boterview-700 rounded-3xl !px-5 !py-2 text-sm font-[600] !text-[var(--vp-button-brand-text)] transition-colors duration-250"
                        >
                            Get Started
                        </button>
                    </div>
                </div>

                <!-- Hero image. -->
                <div
                    class="logo relative w-[210px] -rotate-3 border-0 min-[960px]:w-[250px]"
                >
                    <div
                        class="logo-background absolute inset-10 -z-10 border-1 bg-[linear-gradient(-45deg,var(--color-boterview-200)_10%,var(--color-boterview-400)_10%)] blur-[45px] dark:inset-8 dark:blur-[70px]"
                    ></div>
                    <img
                        class="mx-auto w-[320px] max-w-[320px] rounded-[2rem] shadow-2xl select-none dark:shadow-xl"
                        src="../../assets/images/boterview-logo.png"
                        alt="boterview logo"
                        draggable="false"
                    />
                </div>
            </div>
        </div>
    </div>
</template>

<!-- Script. -->
<script>
export default {
    name: "Hero"
};
</script>
