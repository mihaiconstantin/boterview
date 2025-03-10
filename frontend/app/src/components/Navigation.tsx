// Imports.
import { Link } from 'react-router';


// Component props interface.
interface NavigationProps {
    display: boolean;
}


// Navigation component.
const Navigation: React.FC<NavigationProps> = ({ display }) => {
    return (
        // Display the component if the `display` prop is `true`.
        display && (
            <nav className="flex justify-center gap-x-6 border-0 border-blue-500">
                <Link to="/" className="text-md font-semibold text-boterview-text border-0">Welcome</Link>
                <Link to="/consent" className="text-md font-semibold text-boterview-text border-0">Consent</Link>
                <Link to="/stop" className="text-md font-semibold text-boterview-text border-0">Stop</Link>
                <Link to="/download" className="text-md font-semibold text-boterview-text border-0">Download</Link>
            </nav>
        )
    );
};


// Export the `Navigation` component.
export default Navigation;
