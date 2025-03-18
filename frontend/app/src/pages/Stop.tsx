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

    // Define the timer state.
    const [timer, setTimer] = useState<number | undefined>(undefined);

    // Define the display timer status state.
    const [renderTimer, setRenderTimer] = useState<boolean>(false);

    // Get the function for the frontend logout.
    const invalidateParticipant = useInvalidateParticipant();

    // Set the counter from the metadata.
    useEffect(() => {
        // If any data is available.
        if (data?.metadata?.timeout !== undefined) {
            // Get the timeout value from the metadata.
            const value: number = data.metadata.timeout as number;

            // Set the counter to the value from the metadata.
            setTimer(value);

            // Decide whether the configuration requested to display the timer.
            setRenderTimer(value > 0);
        }
    }, [data]);

    // Process the backend logout (i.e., remove the cookies).
    useProcessLogout();

    // Just this once...
    useEffect(() => {
        // ...invalidate the participant in the local storage.
        invalidateParticipant("local");
    }, [invalidateParticipant]);


    // Decrement the counter second by second.
    useEffect(() => {
        // If a timer was not requested to be displayed.
        if (!renderTimer) {
            // Do nothing.
            return;
        }

        // Otherwise, if the timer value is still being retrieved from the API.
        if (timer === undefined) {
            // Do nothing.
            return;
        }

        // Finally, if the timer value is available and greater than zero.
        if (timer > 0) {
            // Decrement a counter.
            const counter: number = setTimeout(() => setTimer(timer - 1), 1000);

            // Clear the counter on unmount.
            return () => clearTimeout(counter);

        // When the time is up.
        } else {
            // Hide the timer.
            setRenderTimer(false);

            // Invalidate the participant (i.e., which redirects to the welcome page).
            invalidateParticipant("memory");
        }
    }, [renderTimer, timer, invalidateParticipant]);

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

                {/* Timer information. */}
                {renderTimer && (
                    <p className="mx-auto mt-10 max-w-xl text-center font-light text-sm text-boterview-text border-0">
                        You will soon be redirected to the welcome page ({ timer }).
                    </p>
                )}

            </Box>
        );
    }
};

// Export the `Stop` component.
export default Stop;
