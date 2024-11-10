import google.generativeai as genai
def call_ai(ques:str):
    genai.configure(api_key="AIzaSyByWYnaz8iPtve4b_Ew7j32G4FwjyR-tu4")
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 5000,
    "response_mime_type": "text/plain",
    }
    model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction=f"回答我提供的問題")
    chat_session = model.start_chat(
    history=[]
    )
    response = chat_session.send_message(f"{ques}")
    return response.text
x=input()
print(call_ai(x))