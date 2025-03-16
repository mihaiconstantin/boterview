// Imports.
import React from 'react';
import StatusMessage from '../types/StatusMessage';
import Feedback from './Feedback';


// Toast notification component.
const Toast: React.FC<StatusMessage> = ({ status, message = {} }) => {
    // Render the toast component.
    return (
        <div className="absolute bottom-[29px] inline-block text-xs inset-x-10 text-center border-0">
            {/* The feedback. */}
            <Feedback status={status} message={message} />
        </div>
    );
}

// Export the toast component.
export default Toast;
