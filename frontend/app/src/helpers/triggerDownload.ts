// Helper to generate a download link and download a blob of data.
const triggerDownload = (data: Blob, filename: string) => {
    // Create a temporary URL for the blob.
    const url = URL.createObjectURL(data);

    // Create a link element.
    const link = document.createElement("a");

    // Set the link's `HTML` attributes.
    link.href = url;
    link.download = filename;

    // Append the link to the document body.
    document.body.appendChild(link);

    // Click the link to trigger the download.
    link.click();

    // Remove the link from the document body.
    document.body.removeChild(link);

    // Revoke the URL object.
    URL.revokeObjectURL(url);
}

// Export the helper.
export default triggerDownload;
