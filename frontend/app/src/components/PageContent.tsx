// Imports.
import React from "react";
import Markdown from "react-markdown";
import useInjectTermination from "../hooks/useInjectTermination";
import sanitizeHtml from "../helpers/sanitizeHtml";
import UIContent from "../types/UIContent";


// `PageContent` component.
const PageContent: React.FC<UIContent> = ({ heading, content, metadata }) => {
    // Get the termination injection function.
    const injectTermination = useInjectTermination();

    // Render the component.
    return (
        <div className="page-content text-boterview-text border-0">
            {/* Heading. */}
            <h2 className="mx-auto text-center text-4xl font-light tracking-tight border-0">
                { heading }
            </h2>

            {/* Route content. */}
            {
                // If the data is provided as `HTML`.
                metadata.html ? (
                    // Render the `HTML`.
                    <div
                        className="flex flex-col gap-6 mx-auto mt-10 max-w-2xl font-light border-0"
                        dangerouslySetInnerHTML={{ __html: injectTermination(sanitizeHtml(content as string)) }}
                    />
                // Otherwise.
                ) : (
                    <div className="flex flex-col gap-6 mx-auto mt-10 max-w-2xl font-light border-0">
                        {
                            // For each string in the content array.
                            (content as string[]).map((paragraph, index) => (
                                // Render a paragraph.
                                <Markdown key={index}>
                                    {injectTermination(paragraph)}
                                </Markdown>
                            ))
                        }
                    </div>
                )
            }
        </div>
    );
}

export default PageContent;
