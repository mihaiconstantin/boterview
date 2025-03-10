// Imports.
import React from 'react';
import Box from './Box';
import StatusMessage from '../types/StatusMessage';
import Feedback from './Feedback';


// Error component.
const PageError: React.FC<StatusMessage> = ({ status, message = {} }) => {
    // Render the page error component.
    return (
        <Box>
            <div className="mx-auto text-center font-light text-sm text-red-700 border-0">
                {/* The feedback. */}
                <Feedback status={status} message={{
                    ...{
                        reject: "Failed to load the requested page data."
                    }, ...message
                }} />
            </div>
        </Box>
    );
}

// Export the error component.
export default PageError;
