// helper to extract the file name from response headers.
const getFilename = (response: Response): string => {
    // Get the content disposition.
    const contentDisposition = response.headers.get("Content-Disposition");

    // If the content disposition is missing.
    if (!contentDisposition) {
        // Throw an error.
        throw new Error(`"Content-Disposition" header is missing from the response.`);
    }

    // Get the file name.
    const filename = contentDisposition.split("filename=")[1];

    // Return the file name.
    return filename;
}

// Export the helper.
export default getFilename;
