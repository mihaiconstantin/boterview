// Imports.
import { atom } from "jotai";
import Participant from "../types/Participant";


// Get the participant from the local storage if it exists.
const participant: Participant = JSON.parse(localStorage.getItem("participant") || "{}");

// If the participant exists set it, otherwise use defaults.
export const participantAtom = atom<Participant>(participant || {
    code: null,
    verified: false,
    consented: false
});
