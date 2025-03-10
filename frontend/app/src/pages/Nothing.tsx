// Imports.
import React from "react";
import Box from "../components/Box";


// Nothing component.
const Nothing: React.FC = () => {
    return (
        <Box>
            {/* Heading. */}
            <h2 className="mx-auto text-center text-4xl font-light tracking-tight text-boterview-text border-0">
                404
            </h2>

            {/* Route content. */}
            <div className="flex flex-col text-center gap-6 mx-auto mt-10 max-w-2xl font-light text-boterview-text border-0">
                <p>Looks like you're looking for something that's not here!</p>
            </div>
        </Box>
    );
};

// Export the `Nothing` component.
export default Nothing;
