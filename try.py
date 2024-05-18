import openai

# Initialize the OpenAI API key
openai.api_key = 'sk-proj-2z1MK2mH1SWNkUdPpa2fT3BlbkFJsCU1sooUdnjFs3UMPK6k'

def generate_course_name(prompt="Generate a creative course name for a tech course"):
    response = openai.Completion.create(
      engine="text-davinci-003",  # You can choose different models
      prompt=prompt,
      max_tokens=10,
      n=1,
      stop=None,
      temperature=0.7,
    )

    course_name = response.choices[0].text.strip()
    return course_name

# Generate and print multiple course names
for _ in range(5):
    print(generate_course_name())
