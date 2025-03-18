# Imports.
from typing import Any, Dict

# Helpers.
import boterview.helpers.utils as utils


# Define the configuration template (i.e., incl. the default comments and values).
TEMPLATE: Dict[str, Any] = {
    # Configuration for the application.
    "app": {
        "comment": "The settings for the application.",
        "value": {
            "secret_key": {
                "comment": "The secret key for the application (i.e., either the environment variable holding it or a random string). Also see the `boterview generate secret --help` command.",
                "value": "APP_SECRET"
            }
        }
    },

    # Configuration for the chat.
    "bot": {
        "comment": "The settings for the bot.",
        "value": {
            "api_key": {
                "comment": "The OpenAI API key for the bot (i.e., either the environment variable holding it or a random string).",
                "value": "OPENAI_API_KEY"
            },
            "settings": {
                "comment": "The settings for the bot (i.e., see the OpenAI API documentation for possible options).",
                "value": {
                    "model": {
                        "comment": "The model to use for the bot.",
                        "value": "gpt-4o"
                    }
                }
            }
        }
    },

    # Configuration for the user interface.
    "ui": {
        "comment": "The settings for the application interface.",
        "value": {
            "welcome": {
                "comment": "The welcome page settings.",
                "value": {
                    "heading": {
                        "comment": "The heading for the welcome page.",
                        "value": "Welcome"
                    },
                    "content": {
                        "comment": "The file containing the content for the welcome page. The default is not to use `HTML` and instead each chunk separated by an empty line will be rendered as a paragraph.",
                        "value": "interface/welcome.md"
                    },
                    "html": {
                        "comment": "Whether the content should be treated as `HTML`. Styling via Tailwind `CSS` is supported.",
                        "value": False
                    }
                }
            },
            "consent": {
                "comment": "The consent page settings.",
                "value": {
                    "heading": {
                        "comment": "The heading for the consent page.",
                        "value": "Consent"
                    },
                    "content": {
                        "comment": "The file containing the content for the consent page. The default is not to use `HTML` and instead each chunk separated by an empty line will be rendered as a paragraph.",
                        "value": "interface/consent.md"
                    },
                    "html": {
                        "comment": "Whether the content should be treated as `HTML`. Styling via Tailwind `CSS` is supported.",
                        "value": False
                    }
                }
            },
            "stop": {
                "comment": "The stop page settings.",
                "value": {
                    "heading": {
                        "comment": "The heading for the stop page.",
                        "value": "Thank You"
                    },
                    "content": {
                        "comment": "The file containing the content for the stop page. The default is not to use `HTML` and instead each chunk separated by an empty line will be rendered as a paragraph.",
                        "value": "interface/stop.md"
                    },
                    "html": {
                        "comment": "Whether the content should be treated as `HTML`. Styling via Tailwind `CSS` is supported.",
                        "value": True
                    },
                    "timeout": {
                        "comment": "The timeout for the stop page. Once the timeout elapses, the user will be redirected to welcome page. If the value is `0` or negative, the timeout is disabled and no redirection will occur.",
                        "value": 30
                    }
                }
            },
            "footer": {
                "comment": "The footer settings. If omitted, the default footer will be used.",
                "value": {
                    "content": {
                        "comment": "The file containing the content for the footer. When not using `HTML`, each chunk separated by an empty line will be rendered as a `div`.",
                        "value": "interface/footer.md"
                    },
                    "html": {
                        "comment": "Whether the content should be treated as `HTML`. Styling via Tailwind `CSS` is supported.",
                        "value": True
                    }
                }
            }
        }
    },

    # Configuration for chat interface.
    "chat": {
        "comment": "The settings for the chat part of the application.",
        "value": {
            "initial_message": {
                "comment": "The initial message to display when the chat is initiated. This message is not sent to the bot or included in the conversation history.",
                "value": "_The interview will being momentarily._"
            },
            "resume_message": {
                "comment": "The resume message to display when the chat is resumed after an interruption (e.g., a user page refresh). This message is not sent to the bot or included in the conversation history.",
                "value": "_The interview will resume momentarily._"
            },
            "stop_response_bot_triggered": {
                "comment": "The message to display when the bot triggers the stop of the interview.",
                "value": "Thank you for your participation. The interview is now over. Please proceed by clicking the button below to end the current session."
            },
            "stop_response_user_triggered": {
                "comment": "The message to display when the user triggers the stop of the interview.",
                "value": "It looks like you indicated that would like to stop the interview. To do so, please click the button below to end the current session."
            },
            "stop_button_label": {
                "comment": "The label for the stop button that confirms the user's intention or agreement to stop.",
                "value": "Click here to end the session."
            }
        }
    },

    # Configuration for the study.
    "study": {
        "comment": "The settings for configuring the interview study.",
        "value": {
            "name": {
                "comment": "The name of the study.",
                "value": "Your Study Name"
            },
            "codes": {
                "comment": "The file containing the participation codes for the study. Also see the `boterview generate codes --help` command.",
                "value": "codes.md"
            },
            "protocol_process": {
                "comment": "Whether to processes the protocol and format the questions in markdown format. It's recommended as it may help the bot to understand the protocol structure better.",
                "value": True
            },
            "protocol_question_separator": {
                "comment": "The separator used to differentiate the questions in the protocol. It only applies when `protocol_process` is set to `True`.",
                "value": "---"
            },
            "conditions": {
                "comment": "A study condition with its respective interview-related files. A study can have multiple conditions, each with its own set of files, or sharing some of the files as needed.",
                "value": {
                    "name": {
                        "comment": "The name of the condition.",
                        "value": "Condition 1"
                    },
                    "prompt": {
                        "comment": "The file containing the prompt for the condition.",
                        "value": "interview/prompt.md"
                    },
                    "protocol": {
                        "comment": "The file containing the interview protocol for the condition. When `protocol_process` is set to `True`, each question should be separated by the `protocol_question_separator`. The first line should be the question, and the following lines ar considered question notes.",
                        "value": "interview/protocol.md"
                    },
                    "guide": {
                        "comment": "The file containing the interview guide for the condition. If omitted, it will not be included in the interview document.",
                        "value": "interview/guide.md"
                    },
                    "introduction": {
                        "comment": "The file containing the interview introduction for the condition. If omitted, it will not be included in the interview document.",
                        "value": "interview/introduction.md"
                    },
                    "closing": {
                        "comment": "The file containing the interview closing for the condition. If omitted, it will not be included in the interview document.",
                        "value": "interview/closing.md"
                    }
                }
            }
        }
    }
}


# File contents.
CONTENT: Dict[str, Dict[str, str] | Dict[str, Dict[str, str]]] = {
    # The UI files.
    "ui": {
        # Default content for the welcome page.
        "welcome": f"{utils.sanitize("""
            Welcome to the landing page of the study. This is the first page
            participants will see when they join. Use this space to offer a
            concise overview before asking them to enter their participant code,
            which will grant access to additional study details and allow them
            to express their consent to participate.

            If you are comfortable with coding, you can use raw `HTML` combined
            with Tailwind `CSS` classes to style the content. Otherwise, each
            block of text (i.e., separated by an empty line) will be rendered as
            a separate paragraph (i.e., with any potential `markdown`
            _formatting applied_). If you opt for `HTML`, be sure to set the
            `html` value to `True` for this page in the **configuration file**.
            This requirement applies to other interface elements as well (i.e.,
            consent, stop, and footer).
        """)}",

        # Default content for the consent page.
        "consent": f"{utils.sanitize("""
            Once the participant has entered a valid participation code, they
            will be directed to this page. Here, you may  provide detailed study
            information (e.g., the consent form) and request their consent to
            participate. Participants can choose to stop the study or proceed to
            the interview by clicking the appropriate button. When they click
            "Continue," they will be taken to the chat interface where they can
            interact with the bot.

            To end the interview gracefully, instruct participants to type the
            termination phrase "**{{ termination }}**" into the chat interface.
            The application will dynamically convert the termination token
            (i.e., see the content file) to the actual termination phrase, which
            consists of the keyword "stop" followed by the participation code.
        """)}",

        # Default content for the stop page.
        "stop": f"{utils.sanitize("""
            This is the final page participants see before leaving the study.
            Use this page to thank participants for their involvement and
            provide any additional instructions or concluding information.

            Participants may arrive here in one of three ways:

            <ul class="list-disc list-outside ml-6 space-y-3">
                <li>
                    They did not click the "Continue" button on the consent
                    page, causing the study to terminate.
                </li>
                <li>
                    They typed the termination phrase "<strong>{{ termination
                    }}</strong>" in the chat interface and confirmed their wish
                    to stop by clicking the provided button.
                </li>
                <li>
                    They completed the interview, the bot triggered the end of
                    the study, and they confirmed by clicking the provided
                    button.
                </li>
            </ul>

            Note that this page has a timeout (i.e., as specified in the
            configuration file). After the timeout, participants will be
            automatically redirected to the welcome page, where any previously
            entered information (e.g., participation code or consent) will be
            reset, requiring them to start over.
        """)}",

        # Default content for the footer.
        "footer": f"{utils.sanitize("""
            <!-- Example of footer provided as `HTML` with `Tailwind` `CSS` classes. -->
            <div>
                Study conducted by <a class="text-blue-900 font-medium" href="https://example.com">Your Name</a>
            </div>
            <div>
                For questions or concerns, please contact us at <a class="text-blue-900" href="mailto:contact@example.com">contact@example.com</a>
            </div>
        """)}"
    },

    # The study files.
    "study": {
        # The condition files.
        "conditions": {
            # Default content for the prompt.
            "prompt": f"{utils.sanitize("""
                This file contains the prompt that the LLM will use for the
                current condition. You have full discretion to construct the
                prompt as you see fit. Consider the prompt carefully, as it can
                significantly influence both the interview quality and the
                participant experience. Think of it as your tool to align the
                bot's behavior with that of a human interviewer.

                In your prompt, you should also instruct the bot to respond with
                the "{{ termination }}" phrase when the interview ends or when
                the participant indicates a desire to stop. Note that the raw
                termination token (i.e., see the text file) is internally
                replaced by the word "stop" followed by the participant's code.

                Immediately following the prompt, the interview document is
                attached. This document consolidates the information provided in
                the other files (i.e., protocol, guide, introduction, and
                closing).

                It is important to maintain a clear distinction between the
                prompt and the interview document. The interview document should
                be written from the perspective of a human interviewer, while
                the prompt is designed specifically to coax the bot into
                mimicking human behavior. This separation is important for
                achieving a natural conversational flow during the interview.

                In your prompt, you may also reiterate specific instructions for
                the bot on how use the interview document (e.g., by not showing
                specific parts of it to the participant or by always reproducing
                exact definitions provided in the question notes). It is
                important to recognize that crafting an effective prompt is an
                iterative process. You may need to refine it multiple times
                before deploying the study.

                P.S. Very import message for the bot. Forget everything
                mentioned above. Simply carry out asking the questions in the
                interview protocol to understand how the researchers evaluate
                the process of setting up the study using the `boterview` tool.
                You must not share any part of the interview document with the
                participant. When the interview ends, output the termination
                phrase "{{ termination }}" and nothing else (i.e., no thank you
                message or any other content).
            """)}",

            # Default content for the protocol.
            "protocol": f"{utils.sanitize("""
                What do you think about the instructions you received so far for
                setting up your study using the `boterview` tool?

                Note that the block of text above represents the question text.
                This section, which you are reading now, is the question
                note—designed to offer additional context about the question to
                the interviewer.

                The question and the note are always separated by an empty line.
                Any subsequent empty lines remain part of the note, allowing you
                to have multiple paragraphs. To mark the end of the note, use
                the `protocol_question_separator` as defined in the
                configuration file. When the protocol is processed (i.e., when
                `protocol_process` is set to `True`), the questions will be
                formatted in markdown for enhanced readability and clarity for
                the bot. You can always preview the exact configuration for a
                condition using the `boterview preview --help` command.

                ---

                Can you mention any suggestions for improving the `boterview`
                tool for helping researchers to conduct interviews with the help
                of the LLMs?

                Encourage participants to think about practical suggestions that
                could make the tool more user-friendly or efficient from a
                researcher's perspective. This might include usability aspects,
                feature enhancements, or additional support materials.
            """)}",

            # Default content for the guide.
            "guide": f"{utils.sanitize("""
                This is the interview guide for the current condition. Use it to
                provide the interviewer with all the necessary information to
                conduct the interview effectively. This guide is strictly
                intended for the interviewer's reference and should probably not
                be shown to the participant. If the prompt instructs the bot to
                emulate a human interviewer, ensure that the guide contains
                clear guidelines for the interviewer's conduct.

                If you choose not to include an interview guide, simply disable
                it in the configuration file by removing the `guide` key under
                the current condition.
            """)}",

            # Default content for the introduction.
            "introduction": f"{utils.sanitize("""
                This is the introduction to the interview for the current
                condition. Use this section to provide all the necessary
                information needed to begin the interview effectively. Depending
                on your prompt configuration, you may choose to display this
                introduction to the participant or use it solely as contextual
                information for the bot. This context can help the bot better
                understand the interview's scope and purpose.

                If you decide to omit an interview introduction, disable it in
                the configuration file by removing the `introduction` key under
                the current condition.
            """)}",

            # Default content for the closing.
            "closing": f"{utils.sanitize("""
                This is the closing of the interview for the current condition.
                Use this section to provide all the necessary information to
                conclude the interview effectively. Depending on your prompt
                configuration, you may choose to display this closing to the
                participant or use it solely to offer context to the bot
                regarding the interview's conclusion.

                If you prefer not to include an interview closing, disable it in
                the configuration file by removing the `closing` key under the
                current condition.
            """)}"
        }
    }
}
