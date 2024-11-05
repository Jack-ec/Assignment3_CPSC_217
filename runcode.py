# This code sets up a function for use in CPSC 217 only
# By Richard Zhao
# This file should not be edited in any way
# Your code should be created in a new, separate file called support_functions.py

import sys
import io

# The run function takes a parameter code, which is a list that represents lines of Python code
# The function runs the code in Python, and returns the output of the code
def run(code):
    output_capture = io.StringIO()
    original_stdout = sys.stdout
    sys.stdout = output_capture

    try:
        # Execute the code
        exec('\n'.join(code))
    except Exception as err:
        error_response = "Error: " + str(err)
        return error_response
    finally:
        sys.stdout = original_stdout

    # Return the output as a string
    return output_capture.getvalue()
