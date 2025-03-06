# Imports.
from typing import Any, Dict


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
                        "value": "ui/welcome.md"
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
                        "value": "ui/consent.md"
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
                        "value": "ui/stop.md"
                    },
                    "html": {
                        "comment": "Whether the content should be treated as `HTML`. Styling via Tailwind `CSS` is supported.",
                        "value": True
                    },
                    "timeout": {
                        "comment": "The timeout for the stop page. If omitted, the default timeout will be used.",
                        "value": 60
                    }
                }
            },
            "footer": {
                "comment": "The footer settings. If omitted, the default footer will be used.",
                "value": {
                    "content": {
                        "comment": "The file containing the content for the footer. The default is not to use `HTML` and instead each chunk separated by an empty line will be rendered as a `div`.",
                        "value": "ui/footer.md"
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
                "value": "The interview will being momentarily."
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
                        "value": "A Condition Name"
                    },
                    "prompt": {
                        "comment": "The file containing the prompt for the condition.",
                        "value": "prompt.md"
                    },
                    "protocol": {
                        "comment": "The file containing the interview protocol for the condition. When `protocol_process` is set to `True`, each question should be separated by the `protocol_question_separator`. The first line should be the question, and the following lines ar considered question notes.",
                        "value": "protocol.md"
                    },
                    "guide": {
                        "comment": "The file containing the interview guide for the condition. If omitted, it will not be included in the interview document.",
                        "value": "guide.md"
                    },
                    "introduction": {
                        "comment": "The file containing the interview introduction for the condition. If omitted, it will not be included in the interview document.",
                        "value": "introduction.md"
                    },
                    "closing": {
                        "comment": "The file containing the interview closing for the condition. If omitted, it will not be included in the interview document.",
                        "value": "closing.md"
                    }
                }
            }
        }
    }
}
