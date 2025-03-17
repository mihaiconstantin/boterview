// Imports.
import React from "react";
import sanitizeHtml from "../helpers/sanitizeHtml";
import useFetchContent from "../hooks/useFetchContent";


// The `Footer` component.
const Footer: React.FC = () => {
    // Fetch the footer data.
    const { data, loading } = useFetchContent("footer");

    // Render the component
    return (
        <footer className="flex flex-col items-center text-center justify-center pt-8 mt-6 gap-2 w-full py-4 text-sm font-normal text-boterview-text border-t border-[#e9ecef] border-0">

            {/* Authors. */}
            {
                loading ? (
                    // While the request is processing.
                    <div className="border-0">Loading...</div>
                ) : (
                    // If the data is available.
                    data ? (
                        // If the data is provided as `HTML`.
                        data.metadata.html ? (
                            // Render the `HTML`.
                            <div
                                className="authors flex flex-col gap-2 border-0"
                                dangerouslySetInnerHTML={{ __html: sanitizeHtml(data.content as string) }}
                            />
                        // Otherwise.
                        ) : (
                            // Render the paragraphs.
                            <div className="authors flex flex-col gap-2 border-0">
                                {
                                    // For each string in the content array.
                                    (data.content as string[]).map((paragraph, index) => (
                                        // Render a div.
                                        <div key={index}>{paragraph}</div>
                                    ))
                                }
                            </div>
                        )
                    // If no data is available
                    ) : (
                        // Render the default footer.
                        <div>
                            Made with <span className="heart inline-block cursor-default transition-all duration-500 hover:rotate-[360deg] text-[1.15rem] text-[#c41b1b]">&#9829;</span> by <a className="text-decoration-none text-blue-900" href="https://mihaiconstantin.com" target="_blank"> Mihai Constantin</a> and <a className="text-decoration-none text-blue-900" href="mailto:e.e.c.gielens@tilburguniversity.edu" target="_blank">Erwin Gielens</a>
                        </div>
                    )
                )
            }

            {/* License. */}
            <div className="license border-0">
                MIT licensed
            </div>

            {/* GitHub link. */}
            <div className="github hover:text-black border-0">
                <a href="https://github.com/mihaiconstantin/boterview" className="text-decoration-none">
                    <svg
                        xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" className="bi bi-github" viewBox="0 0 16 16">
                        <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z" />
                    </svg>
                </a>
            </div>

        </footer>
    );
};

// Export the `Footer` component.
export default Footer;
