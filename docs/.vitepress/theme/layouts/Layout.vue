<!-- Script. -->
<script setup>
//  Imports.
import DefaultTheme from "vitepress/theme";
import Hero from "../components/Hero.vue";
import Footer from "../components/Footer.vue";

// Extract the custom layout.
const { Layout } = DefaultTheme;
</script>

<!-- Template. -->
<template>
    <Layout>
        <!-- Insert a slot at the layout top location. -->
        <template #home-hero-before>
            <!-- Insert header. -->
            <Hero />
        </template>

        <!-- Insert a slot at the layout bottom location. -->
        <template #home-features-after>
            <!-- Insert footer. -->
            <Footer />
        </template>
    </Layout>
</template>
