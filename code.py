import openai

# Set your OpenAI API key here
openai.api_key = 'your_openai_api_key_here'

def get_openai_response(user_input):
    """
    Send user input to OpenAI API and get the response for dialogue generation.
    
    :param user_input: Text input from the user.
    :return: A string containing the OpenAI-generated response.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=150,
            temperature=0.7,
            stop=None,
            n=1
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error in generating response: {e}")
        return "Sorry, I'm having trouble understanding that right now."

# Example of processing a user input
user_input = "I want to check my account balance."
response = get_openai_response(user_input)
print("Bot response:", response)
