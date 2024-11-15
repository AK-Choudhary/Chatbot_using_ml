import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
file_path = 'C:\\Users\\ENVY\\Documents\\StudentsPerformance.csv'
df = pd.read_csv(file_path)

# Define the sliding window size
WINDOW_SIZE = 3  # Adjust this as needed

# Initialize the sliding window
conversation_window = []

def plot_class_distribution(df):
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='race/ethnicity')
    plt.title('Distribution of Students by Race/Ethnicity')
    plt.xlabel('Race/Ethnicity')
    plt.ylabel('Number of Students')
    plt.show()

def plot_scores_by_gender(df):
    plt.figure(figsize=(10, 6))
    df.groupby('gender')[['math score', 'reading score', 'writing score']].mean().plot(kind='bar')
    plt.title('Average Scores by Gender')
    plt.ylabel('Average Score')
    plt.xlabel('Gender')
    plt.xticks(rotation=0)
    plt.show()

def plot_parental_education_vs_scores(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='parental level of education', y='math score')
    plt.title('Math Scores by Parental Level of Education')
    plt.xticks(rotation=45)
    plt.show()

def plot_test_preparation_vs_scores(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='test preparation course', y='writing score')
    plt.title('Writing Scores by Test Preparation Course')
    plt.xticks(rotation=0)
    plt.show()

def get_student_performance_response(user_input):
    user_input = user_input.lower()
    response = ""

    if "average score" in user_input:
        average_scores = df[['math score', 'reading score', 'writing score']].mean()
        response = f"The average scores are: Math: {average_scores['math score']:.2f}, Reading: {average_scores['reading score']:.2f}, Writing: {average_scores['writing score']:.2f}."

    elif "total students" in user_input or "total student" in user_input:
        total_students = df.shape[0]
        response = f"There are a total of {total_students} students in the dataset."

    elif "gender performance" in user_input:
        gender_performance = df.groupby('gender')[['math score', 'reading score', 'writing score']].mean()
        response = gender_performance.to_string()
        plot_scores_by_gender(df)

    elif "highest score in math" in user_input:
        top_student = df.loc[df['math score'].idxmax()]
        response = f"The student with the highest math score is {top_student['gender']} with a score of {top_student['math score']}."

    elif "lowest score in writing" in user_input:
        bottom_student = df.loc[df['writing score'].idxmin()]
        response = f"The student with the lowest writing score is {bottom_student['gender']} with a score of {bottom_student['writing score']}."

    elif "average reading score by gender" in user_input:
        average_reading = df.groupby('gender')['reading score'].mean()
        response = f"Average reading scores: Male: {average_reading['male']:.2f}, Female: {average_reading['female']:.2f}."
        plot_scores_by_gender(df)

    elif "math score distribution" in user_input:
        plt.figure(figsize=(8, 6))
        sns.histplot(df['math score'], bins=10, kde=True)
        plt.title('Distribution of Math Scores')
        plt.xlabel('Math Score')
        plt.ylabel('Frequency')
        plt.show()
        response = "Here is the distribution of math scores."

    elif "class visualization" in user_input:
        plot_class_distribution(df)
        response = "Here is the class distribution of students plotted."

    elif "parental education vs math scores" in user_input:
        plot_parental_education_vs_scores(df)
        response = "Here is the box plot of math scores by parental level of education."

    elif "test preparation vs writing scores" in user_input:
        plot_test_preparation_vs_scores(df)
        response = "Here is the box plot of writing scores by test preparation course."

    else:
        response = "I'm sorry, I can't help with that. Please ask about average scores, total students, gender performance, class visualization, or other specific questions."

    return response

def chatbot():
    print("Welcome to the Student Performance Chatbot!")
    print("You can ask me about the following topics:")
    print("1. Average scores")
    print("2. Total students")
    print("3. Gender performance")
    print("4. Highest score in math")
    print("5. Lowest score in writing")
    print("6. Average reading score by gender")
    print("7. Math score distribution")
    print("8. Class visualization")
    print("9. Parental education vs math scores")
    print("10. Test preparation vs writing scores")
    print("Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Thank you for chatting! Goodbye!")
            break

        # Add the user input to the conversation window
        conversation_window.append(user_input)

        # Limit the conversation window to the specified size
        if len(conversation_window) > WINDOW_SIZE:
            conversation_window.pop(0)  # Remove the oldest message

        # Get the response from the bot
        response = get_student_performance_response(user_input)

        # Display the bot's response
        print("Chatbot:", response)

        # Optionally, print the conversation window for context
        print("Conversation History:", conversation_window)

# Start the chatbot
if __name__ == "__main__":
    chatbot()
