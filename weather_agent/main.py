# main.py

import chainlit as cl
from agents import Runner
from weather_agent import weather_agent

@cl.on_chat_start
def chat_start():
    cl.user_session.set("conversation history", [])

@cl.on_message
async def main(message: cl.Message):
    # Get and update history
    history = cl.user_session.get("conversation history", [])
    history.append({"role": "user", "content": message.content})

    # Log for debug
    print(f"📌 Running agent | History length: {len(history)}")
    for msg in history:
        print(f"   {msg['role']}: {msg['content']}")

    # Thinking message
    await cl.Message("Checking...").send()

    try:
        # ✅ Only one call — no 'messages=' keyword
        result = await Runner.run(weather_agent, history)

        # Extract response
        if hasattr(result, "final_output") and result.final_output:
            response = result.final_output
        else:
            response = "I couldn't get a valid response."
    except Exception as e:
        print(f"💥 ERROR: {type(e).__name__}: {e}")
        response = f"Sorry, an error occurred: {str(e)}"

    # Send response
    await cl.Message(response).send()

    # Save to history
    history.append({"role": "assistant", "content": response})