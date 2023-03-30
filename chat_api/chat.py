import openai

openai.api_key = "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"

messages = []
system_msg = input("What type of chatbot do you want to create?: \n")
messages.append({"role": "user", "content": system_msg})
print("Your new assistent is ready!")
while input != "quit":
    message = input("")
    if message == "history":
        for i in messages : print(i)
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content" : reply})
    print(f'\n {reply} \n')





