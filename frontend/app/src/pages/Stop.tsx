// Imports.
import React, { useEffect, useState } from "react";
import useFetchContent from "../hooks/useFetchContent";
import useProcessLogout from "../hooks/useProcessLogout";
import useInvalidateParticipant from "../hooks/useInvalidateParticipant";
import Status from "../types/Status";
import Box from "../components/Box";
import PageLoading from "../components/PageLoading";
import PageError from "../components/PageError";
import PageContent from "../components/PageContent";


// Stop component.
const Stop: React.FC = () => {
    // Fetch the stop page data.
    const { data, loading, error } = useFetchContent("stop");

    // Define the counter state.
    const [counter, setCounter] = useState<number>(10);

    // Set the counter from the metadata.
    useEffect(() => {
        // If any data is available.
        if (data?.metadata?.timeout !== undefined) {
            // Set the counter to the value from the metadata.
            setCounter(data.metadata.timeout as number);
        }
    }, [data]);

    // Process the backend logout.
    useProcessLogout();

    // Get the function for the frontend logout.
    const invalidateParticipant = useInvalidateParticipant();

    // Decrement the counter second by second.
    useEffect(() => {
        // If the counter is greater than zero.
        if (counter > 0) {
            // Decrement the counter.
            const timer: number = setTimeout(() => setCounter(counter - 1), 1000);

            // Clear the timer on unmount.
            return () => clearTimeout(timer);

        // When the time is up.
        } else {
            // Invalidate the participant.
            invalidateParticipant();
        }
    }, [counter, invalidateParticipant]);

    // If the page is loading.
    if (loading) {
        // Render the loading page.
        return <PageLoading />;
    }

    // If there is an error.
    if (error !== Status.accept) {
        // Render the error page.
        return <PageError status={error} />;
    }

    // If the data is available.
    if (data) {
        // Render the component.
        return (
            <Box>
                {/* The page data. */}
                <PageContent {...data} />

                {/* Redirect information. */}
                <p className="mx-auto mt-10 max-w-xl text-center font-light text-sm text-boterview-text border-0">
                    You will soon be redirected to the welcome page ({ counter }).
                </p>
            </Box>
        );
    }
};

// Export the `Stop` component.
export default Stop;
