// Define a function that intercepts fetch requests.
const interceptRequest = (pathname, method, callback) => {
    // Capture the original fetch function.
    const originalFetch = window.fetch;

    // Override the global fetch function.
    window.fetch = (...args) => {
        // Extract the url
        const url = args[0];

        // Extract the options (if provided).
        const options = args[1] || {};

        // Create the interception condition.
        const request_conditions = (
            // The `URL` is a string.
            typeof url === "string" &&

            // The pathname includes the desired path to intercept.
            new URL(url).pathname === pathname &&

            // The method key exists.
            options.method &&

            // The request method matches the desired method.
            options.method.toUpperCase() === method.toUpperCase()
        );

        // If this the request conditions are fulfilled.
        if (request_conditions) {
            // Call the original fetch and process the response.
            return originalFetch.apply(this, args).then((response) => {
                // If the response is not okay.
                if (!response.ok) {
                    // Log the error.
                    console.error(`Error with intercepted response from '${response.url}'. Status: ${response.status}`);

                    // Return the original response to not interrupt the flow.
                    return response;
                }

                // Handle the response (i.e., the callback must return a response).
                return callback(response);
            });
        }

        // Otherwise, use the original fetch function.
        return originalFetch.apply(this, args);
    }
}


// Intercept the `/action` endpoint.
interceptRequest("/chat/project/action", "POST", (response) => {
    // Clone the response.
    const clonedResponse = response.clone();

    // Parse the cloned response.
    clonedResponse.json().then((data) => {
        // If the response meets the criteria.
        if (data && data.success && data.response === "stop") {
            // Get the origin of the response.
            const origin = new URL(clonedResponse.url).origin;

            // Send a request to the `API` to stop the session.
            fetch(`${origin}/api/action`, {
                method: "POST",
                credentials: "include",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    "action": "stop"
                })
            // Process the stop response.
            }).then((actionResponse) => {
                if (!actionResponse.ok) {
                    // Log the error.
                    console.error(`Error with action response from '${actionResponse.url}'. Status: ${actionResponse.status}`);

                    // Return the stop response as is.
                    return actionResponse;
                }

                // Since the response is okay, parse it.
                actionResponse.json().then((stopData) => {
                    // If the response meets the criteria.
                    if (stopData.status === "success" && stopData.url) {
                        // Change the location to the redirect location.
                        window.location.replace(stopData.url);

                    // Otherwise
                    } else {
                        // Log the error.
                        console.error("The response for the 'stop' action does not match to expected format.");
                    }
                });
            });
        }
    });

    // Return the original response.
    return response;
});
