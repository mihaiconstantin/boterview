// Imports.
import React from 'react';
import Box from './Box';


// Loading component.
const PageLoading: React.FC = () => {
    return (
        <Box>
            <div className="mx-auto text-center text-sm text-boterview-text border-0">
                Loading...
            </div>
        </Box>
    );
}

// Export the loading component.
export default PageLoading;
