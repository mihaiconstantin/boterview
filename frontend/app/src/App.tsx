// Main component structuring the application.
const App = () => {
    return (
        <main className="min-h-screen flex border-1 border-red-500">
            <div className="container w-[1024px] mx-auto border-1 border-red-500 p-6">
                <div className="h-full flex flex-col gap-6 border-1">

                    {/* Header. */}
                    <div className="w-full border-1 border-green-500">
                        Application header.
                    </div>

                    {/* Main content. */}
                    <div className="w-full border-1 border-green-500">
                        Application main content.
                    </div>

                    {/* Footer */}
                    <div className="w-full mt-auto border-1 border-black">
                        Application footer.
                    </div>
                </div>
            </div>
        </main>
    );
}

// Export the main component.
export default App;
