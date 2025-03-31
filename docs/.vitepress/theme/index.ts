// Imports.
import DefaultTheme from "vitepress/theme";

// Import the custom theme layout.
import Layout from './layouts/Layout.vue';

// Import custom `css`.
import "../assets/css/styles.css";


// Export the custom theme.
export default {
    extends: DefaultTheme,

    // Provide a custom with possible slots overrides.
    Layout: Layout
}
