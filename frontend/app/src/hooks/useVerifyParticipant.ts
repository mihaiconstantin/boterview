// Imports.
import { useAtom } from "jotai";
import { participantAtom } from "../atoms/participantAtoms";
import Status from "../types/Status";
import Endpoint from "../types/Endpoint";


// Hook to verify the participant code.
const useVerifyParticipantCode = () => {
    // Access the participant code setter function.
    const [participant, setParticipant] = useAtom(participantAtom);

    // Verify the participant code.
    const verifyParticipantCode = async (code: string): Promise<Status> => {
        // Define the response variable.
        let response: Response;

        // Attempt to verify the participant code.
        try {
            // Send a `POST` request to the verification endpoint.
            response = await fetch(Endpoint.api.verify, {
                method: "POST",
                credentials: "include",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ "code": code })
            });
        // In case of a network error, return an error.
        } catch (error) {
            // Log the error.
            console.error(error);

            // Return on-verification error.
            return Status.error;
        }

        // Parse the response.
        const data = await response.json();

        // If the response is successful, set the participant code.
        if (response.ok && data.status == "success") {
            // Update the participant.
            setParticipant({ ...participant, code: code, verified: true });

            // Also store to the local storage.
            localStorage.setItem("participant", JSON.stringify({ ...participant, code: code, verified: true }));

            // Return valid verification.
            return Status.accept;
        }

        // Otherwise, return invalid verification.
        return Status.reject;
    }

    // Return the verification function.
    return verifyParticipantCode;
}

// Export the hook.
export default useVerifyParticipantCode;
