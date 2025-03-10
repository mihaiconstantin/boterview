// Imports.
import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router";
import App from "./App.tsx";


//  Get the root element.
const root = document.getElementById("root");

// Check if the root element exists.
if (root == null) {
    // Throw.
    throw new Error("HTML `root` element not found.");
}

// Render the application.
ReactDOM.createRoot(root).render(
    <React.StrictMode>
        <BrowserRouter>
            <App />
        </BrowserRouter>
    </React.StrictMode>
);
