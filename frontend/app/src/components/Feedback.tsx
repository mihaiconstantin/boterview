// Imports.
import React from "react";
import Status from "../types/Status";
import StatusMessage from "../types/StatusMessage";


// Status message component.
const Feedback: React.FC<StatusMessage> = ({ status, message = {} }) => {
    // Define the default message.
    const defaultMessage = {
        accept: "Operation performed successfully.",
        reject: "Failed to perform the requested operation.",
        error: "An error occurred. Please try again."
    }

    // Merge the default message with the provided message.
    message = { ...defaultMessage, ...message };

    // Render the feedback message component.
    return (
        // Add a fragment to wrap the content without DOM elements.
        <>
            {/* Accept status message. */}
            {status === Status.accept && (
                <span className="text-green-800">{message.accept}</span>
            )}

            {/* Reject status message. */}
            {status === Status.reject && (
                <span className="text-red-800">{message.reject}</span>
            )}

            {/* Error status message. */}
            {status === Status.error && (
                <span className="text-red-800">{message.error}</span>
            )}
        </>
    );
};

export default Feedback;
