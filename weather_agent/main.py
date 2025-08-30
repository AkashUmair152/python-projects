import chainlit as cl
from agents import Runner
from weather_agent import weather_agent

@cl.on_chat_start
def chat_start():
    cl.user_session.set("conversion history", [])

@cl.on_message
async def main(message: cl.message):
    history = cl.user_session.get("conversion history", [])
    history.append({"role": "user", "content": message.content})
    cl.Message("Thank you for your message!").send()
    result = await Runner.run(
        weather_agent,
        history
    )
    history.append({"role": "user", "content": result.final_output})
    await cl.Message(result.final_output).send()
