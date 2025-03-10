// Imports.
import React, { useState } from "react";
import { useNavigate } from "react-router";
import useFetchContent from "../hooks/useFetchContent";
import useProcessConsent from "../hooks/useProcessConsent";
import Status from "../types/Status";
import Endpoint from "../types/Endpoint";
import Box from "../components/Box";
import Toast from "../components/Toast";
import PageLoading from "../components/PageLoading";
import PageError from "../components/PageError";
import PageContent from "../components/PageContent";


// Consent component.
const Consent: React.FC = () => {
    // Fetch the consent page data.
    const { data, loading, error } = useFetchContent("consent");

    // Define the consent processing status state.
    const [status, setStatus] = useState<Status>(Status.unknown);

    // Get the navigate function from the hook.
    const navigate = useNavigate();

    // Get the function to process the consent.
    const processConsent = useProcessConsent();

    // Handle the consent processing.
    const handleConsent = async () => {
        // Process the consent.
        const status: Status = await processConsent();

        // Set the status.
        setStatus(status);

        // If the consent is successful, navigate to the chat server.
        if (status === Status.accept) {
            // Replace the current URL with the chat server URL.
            window.location.replace(Endpoint.chat);
        }
    }

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

                {/* Consent buttons. */}
                <div className="mx-auto mt-10 flex justify-center gap-x-6 border-0">
                    <button
                        type="submit" className="flex-none rounded-md bg-boterview-text px-3.5 py-2.5 text-sm font-semibold text-white shadow-xs hover:bg-boterview-text/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white"
                        onClick={() => navigate("/stop")}
                    >
                        Stop
                    </button>
                    <button
                        type="submit"
                        className="flex-none rounded-md bg-boterview-orange px-3.5 py-2.5 text-sm font-semibold text-white shadow-xs hover:bg-boterview-orange/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white"
                        onClick={handleConsent}
                    >
                        Continue
                    </button>
                </div>

                {/* The consent status. */}
                <Toast status={status} message={{
                    accept: "",
                    reject: "Consent not processed. Please try again."
                }} />
            </Box>
        );
    }
};

// Export the `Consent` component.
export default Consent;
