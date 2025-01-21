import gradio as gr

def openhands_demo(input_text):
    return f"You said: {input_text}. OpenHands is ready!"

app = gr.Interface(
    fn=openhands_demo,
    inputs=gr.Textbox(label="Enter something"),
    outputs=gr.Textbox(label="Response"),
    title="OpenHands Demo"
)

if __name__ == "__main__":
    app.launch()
