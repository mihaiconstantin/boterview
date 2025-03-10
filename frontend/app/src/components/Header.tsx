// Imports.
import React from 'react';
import logo from '../assets/images/boterview-logo.png';
import Navigation from './Navigation.tsx';


// Header component.
const Header: React.FC = () => {
    return (
        <header className="flex flex-col items-center border-0 border-blue-500">
            {/* Logo. */}
            <div className="p-6 border-0 border-red-500">
                <img className="w-40 rounded-3xl shadow-xl drag" src={logo} alt="boterview logo" draggable="false"/>
            </div>

            {/* Development navigation. */}
            <Navigation display={false} />
        </header>
    );
};

// Export the `Header` component.
export default Header;
