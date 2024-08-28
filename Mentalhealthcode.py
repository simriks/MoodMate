# Define the questions and suggestions for low scores
questions = {
    "How well are you sleeping? (1-10)": [
        "Consider establishing a consistent sleep routine, including a regular bedtime and wake-up time, to improve your sleep quality.",
        "Explore relaxation techniques before bed, such as reading, meditation, or avoiding screens, to help you wind down and fall asleep more easily."
    ],
    "How satisfied are you with your work-life balance? (1-10)": [
        "Set clear boundaries between work and personal time to ensure you have dedicated time for relaxation and activities outside of work.",
        "Evaluate your current workload and discuss possible adjustments with your supervisor to avoid overworking and to improve your work-life balance."
    ],
    "How often do you engage in physical activity? (1-10)": [
        "Try incorporating short, regular exercise sessions into your daily routine, such as a brisk walk or quick workout, to increase your physical activity levels.",
        "Join a local sports team or fitness class to make physical activity more enjoyable and social, which can help you stay motivated."
    ],
    "How connected do you feel with friends and family? (1-10)": [
        "Schedule regular catch-ups with friends and family through calls, video chats, or in-person visits to strengthen your connections.",
        "Engage in activities or join groups where you can meet new people and build meaningful relationships to enhance your social connections."
    ],
    "How often do you take breaks during work? (1-10)": [
        "Implement a structured break schedule, such as taking a 5-minute break every hour, to reduce fatigue and improve productivity.",
        "Use techniques like the Pomodoro Technique to manage work and break times effectively, helping you stay refreshed and focused."
    ],
    "How motivated do you feel about your work? (1-10)": [
        "Set specific, achievable goals for your work to help maintain motivation and track your progress.",
        "Seek feedback from colleagues or supervisors to identify areas for growth and recognize your accomplishments to boost motivation."
    ],
    "How often do you engage in hobbies or activities you enjoy? (1-10)": [
        "Dedicate regular time in your schedule for hobbies or activities you enjoy to ensure they remain a part of your routine.",
        "Explore new hobbies or interests to reignite your passion and add variety to your activities."
    ],
    "How calm and at ease do you feel on a daily basis? (1-10)": [
        "Practice mindfulness or meditation techniques daily to help manage stress and increase your sense of calm.",
        "Identify and address sources of stress in your life by implementing stress-reducing strategies, such as deep breathing exercises or time management techniques."
    ],
    "How would you rate your overall mental health? (1-10)": [
        "Consider seeking support from a mental health professional if you're struggling with your mental health to receive personalized guidance and support.",
        "Engage in self-care activities, such as regular exercise, healthy eating, and adequate sleep, to support your mental well-being."
    ],
    "How often do you feel content and optimistic? (1-10)": [
        "Practice gratitude by regularly acknowledging things you're thankful for to boost your contentment and optimism.",
        "Engage in positive thinking exercises or cognitive-behavioral techniques to help shift your perspective towards a more optimistic outlook."
    ],
    "How well have you been able to handle stress this week? (1-10)": [
        "Develop and implement stress management strategies, such as relaxation techniques or time management skills, to improve your stress handling.",
        "Reflect on stress triggers and work on addressing them to prevent future stress from becoming overwhelming."
    ],
    "How well have you been able to concentrate on tasks recently? (1-10)": [
        "Create a distraction-free work environment and use focus techniques, such as the Pomodoro Technique, to enhance your concentration.",
        "Break tasks into smaller, manageable steps to make them less overwhelming and easier to concentrate on."
    ],
    "How energized do you feel throughout the day? (1-10)": [
        "Ensure you are getting adequate rest and sleep to help maintain your energy levels throughout the day.",
        "Incorporate regular physical activity and healthy eating habits into your routine to boost and sustain your energy."
    ],
    "How often do you eat healthy, balanced meals? (1-10)": [
        "Plan and prepare meals ahead of time to ensure you have access to healthy and balanced options throughout the week.",
        "Consider consulting a nutritionist or dietitian to create a meal plan that meets your dietary needs and supports healthy eating habits."
    ],
    "How often do you spend time outdoors or in nature? (1-10)": [
        "Schedule regular outdoor activities or nature walks to increase your exposure to nature and enjoy its benefits.",
        "Incorporate nature into your daily routine, such as taking breaks outside or choosing outdoor settings for exercise or relaxation."
    ],
    "How often do you practice mindfulness or meditation? (1-10)": [
        "Set aside dedicated time each day for mindfulness or meditation practices to build consistency and reap the benefits.",
        "Explore different mindfulness techniques or meditation apps to find a practice that resonates with you and fits into your routine."
    ],
    "How well do you handle unexpected challenges or changes? (1-10)": [
        "Develop problem-solving skills and coping strategies to better manage unexpected challenges and adapt to changes.",
        "Practice flexibility and openness to change by gradually exposing yourself to new experiences and adjusting your mindset."
    ],
    "How well do you feel you are able to contain your emotions of anger and stress? (1-10)": [
        "Learn and practice emotion regulation techniques, such as deep breathing or mindfulness, to better manage your emotions.",
        "Consider seeking support from a mental health professional to develop strategies for managing anger and stress effectively."
    ],
    "How often do you feel a sense of purpose or fulfillment in your daily life? (1-10)": [
        "Set personal goals and engage in activities that align with your values and passions to increase your sense of purpose and fulfillment.",
        "Reflect on what gives you meaning and make time for those activities regularly to enhance your daily sense of purpose."
    ],
    "How often do you feel that you are able to express your emotions openly and honestly? (1-10)": [
        "Practice open communication with trusted friends or family members to build confidence in expressing your emotions.",
        "Work on developing emotional intelligence skills to better understand and articulate your feelings in various situations."
    ]
}


# Function to ask questions and collect responses
def ask_questions():
    responses = {}

    print("Please answer the following questions on a scale of 1-10:")

    for question in questions.keys():
        while True:
            try:
                response = int(input(question + " "))
                if 1 <= response <= 10:
                    responses[question] = response
                    break
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Please enter a valid number.")

    return responses

# Function to rate mental health based on the average score
def rate_mental_health(average_score):
    if average_score <= 4:
        return "bad"
    elif 4 < average_score <= 6:
        return "moderate"
    elif 6 < average_score <= 8:
        return "good"
    else:
        return "excellent"

# Function to provide suggestions for improvement
def provide_suggestions(low_score_questions, num_suggestions):
    print("\nBased on your responses, here are some targeted suggestions for improvement:")
    for question in low_score_questions:
        print(f"\nFor the question '{question}':")
        for suggestion in questions[question][:num_suggestions]:
            print("- " + suggestion)

# Main function to run the mental health assessment
def run_mental_health_assessment():
    print("Welcome to the Remote Work Wellness App!\n")
    responses = ask_questions()
    total_score = sum(responses.values())
    average_score = total_score / len(responses)

    # Determine the mental health rating
    mental_health_status = rate_mental_health(average_score)

    # Print the average score
    print(f"\nYour average score is: {average_score:.2f}")

    # Print the mental health rating
    print("\nYour mental health rating is:", mental_health_status.capitalize())

    # Determine the number of suggestions based on the rating
    if mental_health_status in ["good", "excellent"]:
        num_suggestions = 2
    else:
        low_score_questions = [q for q, score in responses.items() if score <= 4]
        if len(low_score_questions) >= 5:
            num_suggestions = 1
        else:
            num_suggestions = 2

    # Provide suggestions
    if num_suggestions > 0:
        low_score_questions = [q for q, score in responses.items() if score <= 4]
        provide_suggestions(low_score_questions, num_suggestions)
    else:
        print("Keep up the good work!")

    print("\nThank you for using the Remote Work Wellness App!")

# Run the mental health assessment
run_mental_health_assessment()