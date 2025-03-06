import streamlit as st
import random

class QuizGenerator:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Berlin", "Paris", "Madrid"],
                "correct_answer": "Paris",
                "marks": 2
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                "correct_answer": "Mars",
                "marks": 2
            },
            {
                "question": "What is 7 × 8?",
                "options": ["54", "56", "62", "64"],
                "correct_answer": "56",
                "marks": 1
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["Van Gogh", "Picasso", "Leonardo da Vinci", "Michelangelo"],
                "correct_answer": "Leonardo da Vinci",
                "marks": 3
            },
            {
                "question": "What is the largest mammal in the world?",
                "options": ["Elephant", "Blue Whale", "Giraffe", "Great White Shark"],
                "correct_answer": "Blue Whale",
                "marks": 2
            },
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Ag", "Fe", "Au", "Cu"],
                "correct_answer": "Au",
                "marks": 2
            },
            {
                "question": "Which country is home to the Great Barrier Reef?",
                "options": ["Brazil", "Australia", "Indonesia", "Mexico"],
                "correct_answer": "Australia",
                "marks": 3
            },
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Brain", "Liver", "Skin"],
                "correct_answer": "Skin",
                "marks": 2
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
                "correct_answer": "William Shakespeare",
                "marks": 3
            },
            {
                "question": "What is the smallest prime number?",
                "options": ["0", "1", "2", "3"],
                "correct_answer": "2",
                "marks": 1
            }
        ]

    def generate_random_quiz(self, num_questions=5):
        return random.sample(self.questions, num_questions)

def main():
    st.title("🧠 Quiz Generator")
    
    quiz_generator = QuizGenerator()
    
    # Initialize session state for tracking quiz state
    if 'quiz_started' not in st.session_state:
        st.session_state.quiz_started = False
        st.session_state.quiz_questions = []
        st.session_state.user_answers = {}
        st.session_state.total_marks = 0

    # Start Quiz Button
    if not st.session_state.quiz_started:
        if st.button("Start Quiz"):
            st.session_state.quiz_started = True
            st.session_state.quiz_questions = quiz_generator.generate_random_quiz()
            st.session_state.user_answers = {}
            st.session_state.total_marks = 0

    # Quiz Interface
    if st.session_state.quiz_started:
        for idx, question in enumerate(st.session_state.quiz_questions, 1):
            st.subheader(f"Question {idx} (Marks: {question['marks']})")
            st.write(question['question'])
            
            # User Answer Selection
            user_answer = st.radio(
                "Select Your Answer", 
                question['options'], 
                key=f"q_{idx}",
                index=None  # No default selection
            )
            
            # Store user's answer
            st.session_state.user_answers[idx-1] = user_answer

        # Submit Quiz Button
        if st.button("Submit Quiz"):
            st.session_state.total_marks = 0
            for idx, question in enumerate(st.session_state.quiz_questions):
                user_answer = st.session_state.user_answers.get(idx)
                
                if user_answer == question['correct_answer']:
                    st.session_state.total_marks += question['marks']
                    st.success(f"Q{idx+1}: Correct! +{question['marks']} marks")
                elif user_answer is None:
                    st.warning(f"Q{idx+1}: Not answered")
                else:
                    st.error(f"Q{idx+1}: Incorrect. Correct answer was: {question['correct_answer']}")
            
            # Final Results
            st.header("Quiz Results")
            st.write(f"Total Marks Scored: {st.session_state.total_marks}")
            
            # Reset Quiz
            if st.button("Take Another Quiz"):
                st.session_state.quiz_started = False

if __name__ == "__main__":
    main()