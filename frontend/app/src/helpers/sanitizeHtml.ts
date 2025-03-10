// Imports.
import DOMPurify from "dompurify";


// Function to render sanitized `HTML`.
const sanitizeHtml = (html: string): string => {
    // Sanitize the `HTML`.
    const sanitizedHtml: string = DOMPurify.sanitize(html);

    // Return the sanitized `HTML`.
    return sanitizedHtml;
};

// Export the function.
export default sanitizeHtml;
