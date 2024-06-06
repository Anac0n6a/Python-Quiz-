import tkinter as tk
import random

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.questions = self.read_questions("questions_and_answers.txt")
        self.selected_questions_indices = random.sample(range(len(self.questions)), 90)
        self.current_question_index = 0
        self.selected_answers = []

        self.question_label = tk.Label(master, text="", wraplength=400, justify=tk.LEFT, font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.answers_frame = tk.Frame(master)
        self.answers_frame.pack(pady=10)

        self.feedback_label = tk.Label(master, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=10)

        self.next_button = tk.Button(master, text="Next", command=self.next_question, font=("Arial", 12))
        self.next_button.pack(pady=10)

        self.answer_vars = []
        self.load_question()

    def read_questions(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            questions = []
            current_question = None
            ignore_lines = False
            for line in lines:
                if line.startswith("Question #"):
                    if current_question:
                        questions.append(current_question)
                    current_question = {"number": "", "text": "", "options": [], "correct_answer": ""}
                    ignore_lines = False
                elif line.startswith("Correct Answer"):
                    current_question["correct_answer"] = line.split(":")[1].strip()
                elif line.startswith("Community vote distribution"):
                    ignore_lines = True
                elif line.strip() and not ignore_lines:
                    if line[0] in "ABCDEFGHI" and line[1] == ".":
                        current_question["options"].append(line.strip())
                    else:
                        current_question["text"] += line
            if current_question:
                questions.append(current_question)
            return questions

    def load_question(self):
        question = self.questions[self.selected_questions_indices[self.current_question_index]]
        question_number = self.current_question_index + 1
        total_questions = len(self.selected_questions_indices)
        self.question_label.config(text=f"Question {question_number}/{total_questions}\n\n{question['text']}")

        # Remove previous answer buttons
        for widget in self.answers_frame.winfo_children():
            widget.destroy()

        self.answer_vars = []

        # Display answer options
        for option in question["options"]:
            var = tk.BooleanVar()
            self.answer_vars.append((option[0], var))  # (Option letter, Variable)
            answer_button = tk.Checkbutton(self.answers_frame, text=option, variable=var, wraplength=400, justify=tk.LEFT, font=("Arial", 12))
            answer_button.pack(anchor=tk.W)

        self.feedback_label.config(text="")

    def next_question(self):
        # Record the selected answers
        selected = ''.join(letter for letter, var in self.answer_vars if var.get())
        self.selected_answers.append(selected)

        # Provide feedback
        correct_answer = self.questions[self.selected_questions_indices[self.current_question_index]]["correct_answer"]
        if selected == correct_answer:
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text=f"Incorrect. The correct answer is {correct_answer}.", fg="red")

        if self.current_question_index < len(self.selected_questions_indices) - 1:
            self.current_question_index += 1
            self.master.after(1000, self.load_question)
        else:
            self.master.after(1000, self.show_results)

    def show_results(self):
        correct_count = sum(1 for i, answer in enumerate(self.selected_answers)
                            if answer == self.questions[self.selected_questions_indices[i]]["correct_answer"])
        total_questions = len(self.selected_questions_indices)
        score = (correct_count / total_questions) * 100

        result_text = f"You scored {correct_count} out of {total_questions} ({score:.2f}%)."
        self.question_label.config(text=result_text)
        for widget in self.answers_frame.winfo_children():
            widget.destroy()
        self.feedback_label.config(text="")
        self.next_button.pack_forget()

def main():
    root = tk.Tk()
    root.title("Quiz App")
    root.geometry("900x900")
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()