// Imports.
import { useSetAtom } from "jotai";
import { participantAtom } from "../atoms/participantAtoms";
import Participant from "../types/Participant";


// Hook to invalidate the participant in memory and local storage.
const useInvalidateParticipant = () => {
    // Access the participant object in memory.
    const setParticipant = useSetAtom(participantAtom);

    // Define the function to invalidate the participant.
    const invalidateParticipant = () => {
        // Create an empty participant object.
        const participant: Participant = {
            code: null,
            verified: false,
            consented: false
        };

        // Invalidate the participant in memory.
        setParticipant(participant);

        // Also invalidate in the local storage.
        localStorage.setItem("participant", JSON.stringify(participant));
    };

    // Return the function to invalidate the participant.
    return invalidateParticipant;
};

// Export the hook.
export default useInvalidateParticipant;
