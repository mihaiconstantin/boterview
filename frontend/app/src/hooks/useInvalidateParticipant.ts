// Imports.
import { useCallback } from "react";
import { useSetAtom } from "jotai";
import { participantAtom } from "../atoms/participantAtoms";
import Participant from "../types/Participant";


// Define the possible locations to invalidate the participant.
type Where = "memory" | "local";


// Hook to invalidate the participant in memory and local storage.
const useInvalidateParticipant = () => {
    // Access the participant object in memory.
    const setParticipant = useSetAtom(participantAtom);

    // Define the function to invalidate the participant.
    const invalidateParticipant = useCallback((where: Where) => {
        // Create an empty participant object.
        const participant: Participant = {
            code: null,
            verified: false,
            consented: false
        };

        // If the participant is to be invalidated in memory.
        if (where === "memory") {
            // Invalidate the participant in memory.
            setParticipant(participant);

            // Return.
            return;
        }

        // Otherwise, invalidate the participant in local storage.
        localStorage.setItem("participant", JSON.stringify(participant));
    }, [setParticipant]);

    // Return the function to invalidate the participant.
    return invalidateParticipant;
};

// Export the hook.
export default useInvalidateParticipant;
