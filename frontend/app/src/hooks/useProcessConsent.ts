// Imports.
import { useAtom } from "jotai";
import { participantAtom } from "../atoms/participantAtoms";
import Endpoint from "../types/Endpoint";
import Status from "../types/Status";


// Hook to redirect to chat server.
const useProcessConsent = () => {
    // Access the participant object.
    const [participant, setParticipant] = useAtom(participantAtom);

    // Process the consent.
    const processConsent = async (): Promise<Status>  => {
        // Update the participant consent.
        participant.consented = true;

        // Define the response variable.
        let response: Response;

        // Attempt to process the consent.
        try {
            // Send a `POST` request to the consent endpoint.
            response = await fetch(Endpoint.api.consent, {
                method: "POST",
                credentials: "include",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(participant)
            });
        // In case of a network error, return an error.
        } catch (error) {
            // Log the error.
            console.error(error);

            // Return on-consent-processing error.
            return Status.error;
        }

        // Parse the response.
        const data = await response.json();

        // If the response is successful, return valid.
        if (response.ok && data.status == "success") {
            // Update the participant object in memory.
            setParticipant(participant);

            // Also update the local storage.
            localStorage.setItem("participant", JSON.stringify(participant));

            // Return valid consent.
            return Status.accept;
        }

        // Otherwise, return invalid consent.
        return Status.reject;
    }

    // Return the consent function.
    return processConsent;
}

// Export the hook.
export default useProcessConsent;
