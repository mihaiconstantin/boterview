// Imports.
import { useAtomValue } from "jotai";
import { participantAtom } from "../atoms/participantAtoms";


// Hook to inject termination phrase into the text for the current participant.
const useInjectTermination = () => {
    // Access the participant object.
    const participant = useAtomValue(participantAtom);

    // Function to inject the termination phrase into the text.
    const injectTermination = (text: string): string => {
        // Determine the termination pattern.
        const pattern: RegExp = /\{\{\s*termination\s*\}\}/g;

        // Replace the termination pattern with the termination message.
        text = text.replace(pattern, `stop ${participant.code}`);

        // Return the text.
        return text;
    }

    // Return the injection function.
    return injectTermination;

}

// Export the hook.
export default useInjectTermination;
