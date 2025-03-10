// Imports.
import Status from "./Status";


// Interface for the status message.
export default interface StatusMessage {
    status: Status;
    message?: {
        accept?: string;
        reject?: string;
        error?: string;
    }
}
