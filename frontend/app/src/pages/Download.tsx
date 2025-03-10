// Imports.
import React, { useState } from "react";
import useDownloadData from "../hooks/useDownloadData";
import Status from "../types/Status";
import Box from "../components/Box";
import Toast from "../components/Toast";


// Welcome component.
const Download: React.FC = () => {
    // Define the validation status state.
    const [status, setStatus] = useState<Status>(Status.unknown);

    // Get the function to verify the application secret.
    const downloadData = useDownloadData();

    // Handle code submission.
    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        // Prevent the default form submission.
        event.preventDefault();

        // Extract the form.
        const form = event.currentTarget;

        // Extract the form data.
        const formData = new FormData(form);

        // Extract the application secret
        const secret = formData.get("secret") as string;

        // Verify the secret.
        const status: Status = await downloadData(secret);

        // Set the status.
        setStatus(status);

        // Clear the form.
        form.reset();
    };

    // Render the component.
    return (
        <Box>
            {/* Heading. */}
            <h2 className="mx-auto text-center text-4xl font-light tracking-tight text-boterview-text border-0">
                Download
            </h2>

            {/* Route content. */}
            <div className="flex flex-col gap-6 mx-auto mt-10 max-w-2xl font-light text-boterview-text border-0">
                <p>
                    To download the data, enter the application <span className="font-medium text-boterview-orange">secret key</span> { }
                    used during the study setup. This is the long string of characters found in your <code>.toml</code> { }
                    <span className="font-medium text-boterview-orange">configuration file</span>, without quotation marks.
                    It is perhaps a sensible idea to <span className="italic">paste</span> the key rather than typing it manually.
                </p>
                <p>
                    Provided the secret key is correct, clicking the download button will retrieve all data recorded in the database
                    thus far and compile it into a <span className="italic">Markdown</span> (i.e., <code>.md</code>) file.
                </p>
            </div>

            {/* Code verification form. */}
            <form className="mx-auto mt-10 max-w-sm border-0" autoComplete="off" onSubmit={handleSubmit}>
                <div className="flex gap-x-6">
                    <label htmlFor="secret" className="sr-only">Application secret</label>
                    <input
                        id="secret"
                        name="secret"
                        type="password"
                        autoComplete="off"
                        required
                        className="min-w-0 flex-auto rounded-md bg-boterview-text/5 px-3.5 py-2 text-sm/6 text-boterview-text outline-1 -outline-offset-1 outline-boterview-text/10 placeholder:text-boterview-text/40 focus:outline-2 focus:-outline-offset-2 focus:outline-boterview-text/20"
                        placeholder="Enter your application secret"
                    />
                    <button
                        type="submit"
                        className="flex-none rounded-md bg-boterview-orange px-3.5 py-2.5 text-sm font-semibold text-white shadow-xs hover:bg-boterview-orange/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white"
                    >
                        Download
                    </button>
                </div>

                {/* The verification status. */}
                <Toast status={status} message={{
                    accept: "Data download completed successfully.",
                    reject: "Invalid application secret. Please try again."
                }} />
            </form>
        </Box>
    );
};

// Export the `Welcome` component.
export default Download;
