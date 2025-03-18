// Imports.
import { useEffect, useState } from "react";
import Status from "../types/Status";
import Endpoint from "../types/Endpoint";


// Hook to process the stop.
const useProcessLogout = () => {
    // Define the status state.
    const [status, setStatus] = useState<string>("");

    // Fetch the page data.
    useEffect(() => {
        // Define the fetch data function.
        async function processLogout() {
            // Try to issue the logout request.
            try {
                // Get the response.
                const response: Response = await fetch(Endpoint.api.logout, {
                    method: "POST",
                    credentials: "include",
                    headers: {
                        "Content-Type": "application/json"
                    }
                });

                // Parse the response.
                const data = await response.json();

                if (!response.ok || data.status !== "success") {
                    // Set the status.
                    setStatus(Status.reject);
                }

                // Set the status state.
                setStatus(Status.accept);

            // Catch any errors.
            } catch (error) {
                // Log the error.
                console.error(error);

                // Set the error state.
                setStatus(Status.error);
            }
        }

        // Fetch the data.
        processLogout();
    }, []);

    // Return the status.
    return status;
}

// Export the hook.
export default useProcessLogout;
