This application generates a number of random maths equations, allows user input, checks whether the user input (answer) is correct and responds with displayed feedback.

This program is ideal for anyone wanting to practice basic math.

---

## User Documentation

### Features

- Random math equations 
- Interactive input field for user
- Submit button to submit response
- Response to whether the input is correct or incorrect
- An overall score after the final question

### How to Use

1. **Start the App**  
   Open the program (either in a browser for the web version, or run it in Python for the desktop version).

2. **View the Equation**  
   You will see a simple math equation displayed (e.g., `5 × x = 20`) .

3. **Enter Your Answer**  
   Type your answer in the provided input box.

4. **Submit Your Answer**  
   Click the **Submit** button.

5. **Get Feedback**  
   - If your answer is **correct**, a green success message is shown.
   - If your answer is **incorrect**, a red error message appears with the correct solution.

6. **Next Question**  
   A new equation will appear for you to solve.

---

## Technical Documentation

### Overview

The application follows an easy and logical flow:

1. **Generate Equation**: The application generates a random maths equation using a numbers at random.
2. **Input Handling**: Uses an entry widget for the user to submit their answerr.
3. **Answer Validation**: The users response will then be checked agsint the correct answer.
4. **Feedback Display**: Response recieved, correct or incorrect.

### Components

#### Equation Generator
- Picks two numeric integers `a` and `b`
- Calculates the result (e.g., `a × x = b`)
- Holds the correct answer within the generator

#### Input Field
- Numeric input must be entered
- Returns 'Please Enter A Valid Number' in response to non numeric input.

#### Submit Button
- Triggers validation logic
- Temporarily disables user input within the feedback process.

#### Feedback System
- Success message "That's Correct, Well Done!" in green for correct answers
- "Incorrect! The Correct Answer Is" Error message in red for incorrect answers