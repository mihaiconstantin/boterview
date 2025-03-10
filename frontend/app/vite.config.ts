// Imports.
import { defineConfig, loadEnv } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";


// See `https://vite.dev/config`.
export default defineConfig(({ mode }) => {
    // Load the environment variables in the current mode.
    const env = loadEnv(mode, ".", "BOTERVIEW_");

    // Return the configuration.
    return {
        // Enable plugins.
        plugins: [
            react(),
            tailwindcss()
        ],

        // Configure the development server.
        server: {
            // Frontend development server port.
            port: 5173,

            // Proxy.
            proxy: mode == "development" ? {
                '/api': {
                    target: env.BOTERVIEW_BACKEND_URL,
                    changeOrigin: true,
                    secure: false
                },
                '/chat': {
                    target: env.BOTERVIEW_BACKEND_URL,
                    changeOrigin: true,
                    secure: false,
                    ws: true
                }
            } : undefined
        }
    }
});
