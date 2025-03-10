// Imports.
import { Navigate, Outlet } from "react-router";
import { participantAtom } from "../atoms/participantAtoms";
import { useAtom } from "jotai";


// `ProtectedRoute` component.
const ProtectedRoute = () => {
    // Get the participant from the atom.
    const [participant] = useAtom(participantAtom);

    // If the participant is not verified, redirect to the index page.
    if (!participant.verified) {
        // Redirect.
        return <Navigate to="/" replace />;
    }

    // Otherwise, return the component for the navigated route.
    return <Outlet />;
};


// Export the `ProtectedRoute` component.
export default ProtectedRoute;
