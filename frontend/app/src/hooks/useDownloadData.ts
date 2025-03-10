// Imports.
import Status from "../types/Status";
import Endpoint from "../types/Endpoint";
import triggerDownload from "../helpers/triggerDownload";
import getFilename from "../helpers/getFilename";


// Hook to download the study data.
const useDownloadData = () => {
    // Verify the secret and get the data.
    const downloadData = async (secret: string): Promise<Status> => {
        // Define the response variable.
        let response: Response;

        // Attempt to verify the secret and retrieve the data stream.
        try {
            // Send a `POST` request to the download endpoint.
            response = await fetch(Endpoint.api.download, {
                method: "POST",
                credentials: "include",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ "secret": secret })
            });

            // If the response is not okay.
            if (!response.ok) {
                // If the response status is `401 Unauthorized`.
                if (response.status === 401) {
                    // Log the error.
                    console.error("Unauthorized access.");

                    // Return the unauthorized status.
                    return Status.reject;
                }

                // Otherwise, log any other download error.
                console.error(`Failed to download the data: ${response.status}.`);

                // Return the error status.
                return Status.error;
            }

            // Parse the response as blob.
            const data: Blob = await response.blob();

            // Get the file name.
            const filename = getFilename(response);

            // Trigger the download.
            triggerDownload(data, filename);

            // Return the accept status.
            return Status.accept;

        // In case of error.
        } catch (error) {
            // Log the error.
            console.error(error);

            // Return the error status.
            return Status.error;
        }
    }

    // Return the verification function.
    return downloadData;
}

// Export the hook.
export default useDownloadData;
