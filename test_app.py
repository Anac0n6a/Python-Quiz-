import tkinter as tk
import random

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.questions = self.read_questions("questions_and_answers.txt")
        self.selected_questions_indices = random.sample(range(len(self.questions)), 90)
        self.current_question_index = 0
        self.selected_answers = []

        self.question_label = tk.Label(master, text="", wraplength=400, justify=tk.LEFT)
        self.question_label.pack()

        self.answers_frame = tk.Frame(master)
        self.answers_frame.pack()

        self.next_button = tk.Button(master, text="Next", command=self.next_question)
        self.next_button.pack()

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
                    current_question["number"] = line.strip()
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
        self.question_label.config(text=question["number"] + "\n" + question["text"])

        # Remove previous answer buttons
        for widget in self.answers_frame.winfo_children():
            widget.destroy()

        self.answer_vars = []

        # Display answer options
        for option in question["options"]:
            var = tk.BooleanVar()
            self.answer_vars.append((option[0], var))  # (Option letter, Variable)
            answer_button = tk.Checkbutton(self.answers_frame, text=option, variable=var, wraplength=400, justify=tk.LEFT)
            answer_button.pack(anchor=tk.W)

    def next_question(self):
        # Record the selected answers
        selected = ''.join(letter for letter, var in self.answer_vars if var.get())
        self.selected_answers.append(selected)

        if self.current_question_index < len(self.selected_questions_indices) - 1:
            self.current_question_index += 1
            self.load_question()
        else:
            self.show_results()

    def show_results(self):
        correct_count = sum(1 for i, answer in enumerate(self.selected_answers)
                            if answer == self.questions[self.selected_questions_indices[i]]["correct_answer"])
        total_questions = len(self.selected_questions_indices)
        score = (correct_count / total_questions) * 100

        result_text = f"You scored {correct_count} out of {total_questions} ({score:.2f}%)."
        self.question_label.config(text=result_text)
        for widget in self.answers_frame.winfo_children():
            widget.destroy()
        self.next_button.pack_forget()

def main():
    root = tk.Tk()
    root.title("Quiz App")
    root.geometry("600x400")
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()