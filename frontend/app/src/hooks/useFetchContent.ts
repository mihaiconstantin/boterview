// Imports.
import { useEffect, useState } from "react";
import Status from "../types/Status";
import Endpoint from "../types/Endpoint";
import UIContent from "../types/UIContent";


// Hook to fetch UI content.
const useFetchContent = (name: keyof typeof Endpoint.api.ui) => {
    // Define the data state.
    const [data, setData] = useState<UIContent | null>(null);

    // Define the loading state.
    const [loading, setLoading] = useState<boolean>(true);

    // Define the error state.
    const [error, setError] = useState<Status>(Status.unknown);

    // Fetch the UI data.
    useEffect(() => {
        // Define the fetch data function.
        async function fetchContent() {
            // Set the loading.
            setLoading(true);

            // Try to fetch the UI data.
            try {
                // Get the response.
                const response: Response = await fetch(Endpoint.api.ui[name], {
                    method: "GET",
                    credentials: "include",
                    headers: {
                        "Content-Type": "application/json"
                    }
                });

                // If the response is not okay.
                if (!response.ok) {
                    // Switch on the response status.
                    switch (response.status) {
                        // If the response status is `401 Unauthorized`.
                        case 401:
                            // Log the error.
                            console.error("Unauthorized access.");

                            // Set the error state.
                            setError(Status.reject);

                            // Exit the switch.
                            break;

                        // If the response status is `404 Not Found`.
                        case 404:
                            // Log the error.
                            console.error("Resource not found.");

                            // Set the error state.
                            setError(Status.reject);

                            // Exit the switch.
                            break;

                        // Otherwise, log any other kind of error.
                        default:
                            console.error(`Failed to fetch the content: ${response.status}.`);

                            // Set the error state.
                            setError(Status.error);

                            // Exit the switch.
                            break;
                    }
                // Otherwise, if the response is okay.
                } else {
                    // Parse the response as JSON.
                    const json = await response.json();

                    // Set the data state.
                    setData({ ...json.data as UIContent });

                    // Set the error state.
                    setError(Status.accept);
                }

            // Catch any network errors.
            } catch (error) {
                // Log the error.
                console.error(error);

                // Set the error state.
                setError(Status.error);

            // At the end.
            } finally {
                // Set the loading state.
                setLoading(false);
            }
        }

        // Fetch the data.
        fetchContent();
    }, [name]);

    // Return the data, loading, and error states.
    return { data, loading, error };
}

// Export the hook.
export default useFetchContent;
