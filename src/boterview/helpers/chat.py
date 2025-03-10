# Define function to check if the chat should be stopped.
def should_stop_chatting(message: str, user_code: str) -> bool:
    # Check if the message contains the stop command.
    stop: bool = "stop" in message.lower() and user_code.lower() in message.lower()

    # Return.
    return stop
