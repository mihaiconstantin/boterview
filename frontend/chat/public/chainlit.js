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
