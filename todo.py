import openai
from datetime import datetime

# Replace with your OpenAI API Key
OPENAI_API_KEY = "your_api_key_here"

# Function to prioritize tasks
def prioritize_tasks(tasks):
    prompt = "Here is a list of tasks with deadlines. Prioritize them based on urgency:\n"
    for task, deadline in tasks.items():
        prompt += f"- {task}, Deadline: {deadline}\n"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        api_key=OPENAI_API_KEY
    )
    
    return response["choices"][0]["message"]["content"]

# Main function
def main():
    tasks = {}
    while True:
        task = input("Enter task (or type 'done' to finish): ")
        if task.lower() == "done":
            break
        deadline = input(f"Enter deadline for '{task}' (YYYY-MM-DD): ")
        tasks[task] = deadline

    print("\nPrioritizing tasks...\n")
    prioritized_list = prioritize_tasks(tasks)
    print(prioritized_list)

if __name__ == "__main__":
    main()