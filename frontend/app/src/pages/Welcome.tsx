// Imports.
import React, { useState } from "react";
import { useNavigate } from "react-router";
import useFetchContent from "../hooks/useFetchContent";
import useVerifyParticipantCode from "../hooks/useVerifyParticipant";
import Status from "../types/Status";
import Box from "../components/Box";
import Toast from "../components/Toast";
import PageLoading from "../components/PageLoading";
import PageError from "../components/PageError";
import PageContent from "../components/PageContent";


// Welcome component.
const Welcome: React.FC = () => {
    // Fetch the welcome page data.
    const { data, loading, error } = useFetchContent("welcome");

    // Define the validation status state.
    const [status, setStatus] = useState<Status>(Status.unknown);

    // Get the navigate function.
    const navigate = useNavigate();

    // Get the function to verify the participant code.
    const verifyParticipantCode = useVerifyParticipantCode();

    // Handle code submission.
    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        // Prevent the default form submission.
        event.preventDefault();

        // Capture the form.
        const form = event.currentTarget;

        // Extract the form data.
        const formData = new FormData(form);

        // Extract the participant code.
        const participantCode = formData.get("participant-code");

        // Verify the participant code.
        const status: Status = await verifyParticipantCode(participantCode as string);

        // Set the status.
        setStatus(status);

        // Clear the form.
        form.reset();

        // If the verification is successful, navigate to the consent page.
        if (status === Status.accept) {
            // Navigate to the consent page.
            navigate("/consent");
        }
    };

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

                {/* Code verification form. */}
                <form className="mx-auto mt-10 max-w-sm border-0" autoComplete="off" onSubmit={handleSubmit}>
                    <div className="flex gap-x-6">
                        <label htmlFor="participant-code" className="sr-only">Participant code</label>
                        <input id="participant-code" name="participant-code" type="text" required
                            className="min-w-0 flex-auto rounded-md bg-boterview-text/5 px-3.5 py-2 text-sm/6 text-boterview-text outline-1 -outline-offset-1 outline-boterview-text/10 placeholder:text-boterview-text/40 focus:outline-2 focus:-outline-offset-2 focus:outline-boterview-text/20"
                            placeholder="Enter your participant code"
                        />
                        <button
                            type="submit"
                            className="flex-none rounded-md bg-boterview-orange px-3.5 py-2.5 text-sm font-semibold text-white shadow-xs hover:bg-boterview-orange/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white"
                        >
                            Continue
                        </button>
                    </div>

                    {/* The verification status. */}
                    <Toast status={status} message={{
                        accept: "",
                        reject: "Invalid participant code. Please try again."
                    }} />
                </form>
            </Box>
        );
    }
};

// Export the `Welcome` component.
export default Welcome;
