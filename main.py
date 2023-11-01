import chainlit as cl
import openai

# Set your OpenAI API key
openai.api_key = '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'

@cl.on_message

#This is a decorator for the main function. It tells ChainLit that the main function should be called every time a user inputs a message in the UI. The message parameter is expected to be of type cl.Message, which represents a message sent in the UI.

async def main(message: cl.Message):
    user_message = message.content # extract the content of the message object, which represents the user's input message

    # Create a chat conversation with the system message and user input
    conversation = [
        {"role": "system", "content": "your name is ravi and full name is ravinder your suranme is negi  , you love maths and very obsessed with food"},
        {"role": "user", "content": user_message}
    ]

    # Generate a response using OpenAI's GPT-3.5 Turbo
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0.7,  # You can adjust the temperature for more randomness or determinism.
        max_tokens=150,   # You can set an appropriate max_tokens value based on your requirements.
    )

    response_text = response.choices[0].message["content"]
    # Send the generated response as an intermediate message
    #use cl.Message to send the generated response as an intermediate message
    await cl.Message(
        author="ChatGPT",
        content=response_text,
        parent_id=message.id
    ).send()


    # Send the final answer.
    await cl.Message(content=response_text).send()
    #This final step sends a simple text message as the "final answer" to the UI
