// Imports.
import { Routes, Route } from 'react-router';
import Header from './components/Header';
import Welcome from './pages/Welcome';
import Consent from './pages/Consent';
import Stop from './pages/Stop';
import Download from './pages/Download';
import Nothing from './pages/Nothing';
import ProtectedRoute from './components/ProtectedRoute';
import Footer from './components/Footer';


// Main component structuring the application.
const App = () => {
    return (
        <main className="min-h-screen flex select-none border-0 border-red-500">
            <div className="container w-[1024px] mx-auto border-0 border-red-500 p-6">
                <div className="h-full flex flex-col gap-6 border-0">

                    {/* Header. */}
                    <div className="w-full border-0 border-green-500">
                        <Header />
                    </div>

                    {/* Main content. */}
                    <div className="w-full border-0 border-green-500">
                        <Routes>
                            <Route index element={<Welcome />} />
                            <Route element={<ProtectedRoute />}>
                                <Route path="/consent" element = { <Consent /> } />
                                <Route path="/stop" element = { <Stop /> } />
                            </Route>
                            <Route path="/download" element = { <Download /> } />
                            <Route path="*" element = { <Nothing /> } />
                        </Routes>
                    </div>

                    {/* Footer */}
                    <div className="w-full mt-auto border-0 border-black">
                        <Footer />
                    </div>
                </div>
            </div>
        </main>
    );
}

// Export the main component.
export default App;
