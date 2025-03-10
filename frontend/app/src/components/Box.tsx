// Imports.
import React from "react";


// Define box properties interface.
interface BoxProps {
    children: React.ReactNode;
}


// `Box` component.
const Box: React.FC<BoxProps> = ({ children }) => {
    return (
        <div className="box-wrapper">
            <div className="mx-auto">
                <div className="relative isolate overflow-hidden px-6 py-18 shadow-2xl rounded-3xl sm:px-18 border-0">
                    {/* The props. */}
                    {children}

                    {/* The gradient. */}
                    <svg viewBox="0 0 1024 1024" className="absolute top-1/3 left-1/2 -z-10 size-[84rem] -translate-x-1/2" aria-hidden="true">
                        <circle cx="512" cy="512" r="512" fill="url(#759c1415-0410-454c-8f7c-9a820de03641)" fillOpacity="0.7" />
                        <defs>
                            <radialGradient id="759c1415-0410-454c-8f7c-9a820de03641" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(512 512) rotate(90) scale(512)">
                                <stop stopColor="#DCD2CC" />
                                <stop offset="1" stopColor="#D97D5A" stopOpacity="0" />
                            </radialGradient>
                        </defs>
                    </svg>
                </div>
            </div>
        </div>
    );
}

export default Box;
