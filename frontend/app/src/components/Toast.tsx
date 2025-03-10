// Imports.
import React from 'react';
import StatusMessage from '../types/StatusMessage';
import Feedback from './Feedback';


// Toast notification component.
const Toast: React.FC<StatusMessage> = ({ status, message = {} }) => {
    // Render the toast component.
    return (
        <div className="absolute bottom-[29px] left-1/2 transform -translate-x-1/2 text-xs border-0">
            {/* The feedback. */}
            <Feedback status={status} message={message} />
        </div>
    );
}

// Export the toast component.
export default Toast;
