import ollama

print("Connection Test")

response = ollama.chat(
        model="llama3.1:8b",
        messages=[
            {
                "role": "user",
                "content": "Say hello and confirm that you are working"
            }
        ]
)

print(response["message"]["content"])
print("\nOllama test completed successfully")