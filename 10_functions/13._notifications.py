# https://judge.softuni.org/Contests/Practice/Index/1063#12


def underline_message(message):
    return f"{'=' * len(message)}"


def show_success_message(operation, message):
    opr = f"Successfully executed {operation}."
    print(opr)
    print(underline_message(opr))
    msg = f"{message}."
    print(msg)


def show_warning_message(operation):
    opr = f"Warning: {operation}."
    print(opr)
    print(underline_message(opr))


def show_error_message(operation, message, error_code):
    opr = f"Error: Failed to execute {operation}."
    print(opr)
    print(underline_message(opr))
    msg = f"Reason: {message}."
    print(msg)
    err = f"Error code: {error_code}."
    print(err)


def read_and_process_message(message_type):
    if message_type == "success":
        operation = input()
        message = input()
        show_success_message(operation, message)
    elif message_type == "warning":
        operation = input()
        show_warning_message(operation)
    elif message_type == "error":
        operation = input()
        message = input()
        error_code = input()
        show_error_message(operation, message, error_code)


# main
n = int(input())

for _ in range(n):
    msg_type = input()
    read_and_process_message(msg_type)
    print()
