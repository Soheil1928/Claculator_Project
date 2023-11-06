import tkinter as tk
import math

SMALL_FONT_STYLE = ("Arial", 18)
LARGE_FONT_STYLE = ("Arial", 40, "bold")
DIGIT_FONT_STYLE = ("Arial",30, "bold")
SMALL_FONT_STYLE_2 = ("Arial", 18, "bold")


class Calculator:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Calculator')
        self.window.geometry('500x700')
        self.window.resizable(width=False, height=False)

        self.current_expression = ''
        self.total_expression = ''
        self.digits = {7:(2,1), 8:(2,2), 9:(2,3),
                       4:(3,1), 5:(3,2), 6:(3,3),
                       1:(4,1), 2:(4,2), 3:(4,3), 0:(5,2), '.':(5,3)}
        self.operators = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.display_frame = self.create_display_frame()
        self.button_frame = self.create_button_frame()
        self.button_frame.rowconfigure(index=5, weight=1)
        for i in range(0,5):
            self.button_frame.rowconfigure(index=i, weight=1)
            self.button_frame.columnconfigure(index=i, weight=1)

        self.total_label, self.current_label = self.create_display_label()
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.equal_button()
        self.clear_button()
        self.delete_button()
        self.fatorial_button()
        self.bracket_button()
        self.pi_number_button()
        self.sqrt_button()
        self.reverse_number_button()
        self.square_button()
        self.cube_button()
        self.power_x_button()
        self.sin_operator_button()
        self.cos_operator_button()
        self.tan_operator_button()
        
        


    def create_display_frame(self):
        frame = tk.Frame(self.window, height=100)
        frame.pack(expand=True, fill='both')
        return frame
    

    def create_button_frame(self):
        fram = tk.Frame(self.window)
        fram.pack(expand=True, fill='both')
        return fram
    

    def create_display_label(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, font=SMALL_FONT_STYLE, bg='Ivory', anchor=tk.E)
        total_label.pack(expand=True, fill='both')
        current_label = tk.Label(self.display_frame, text=self.current_expression, font=LARGE_FONT_STYLE, bg='Ivory', anchor=tk.E)
        current_label.pack(expand=True, fill='both')
        return total_label, current_label


    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            if digit == '.':
                button = tk.Button(self.button_frame, text=digit, font=DIGIT_FONT_STYLE, command=lambda x=digit: self.digit_import(x), 
                                   borderwidth=0, bg='silver')
                button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
            else:
                button = tk.Button(self.button_frame, text=digit, font=DIGIT_FONT_STYLE, command=lambda x=digit: self.digit_import(x), 
                                   borderwidth=0, bg='gray', fg='white')
                button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
    

    def create_operator_buttons(self):
        i = 1
        for operator, symbol in self.operators.items():
            button = tk.Button(self.button_frame, text=symbol, font=DIGIT_FONT_STYLE, command=lambda x=operator: self.operator_import(x), 
                               borderwidth=0, bg='silver')
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1


    def digit_import(self, value):
        self.current_expression += str(value)
        self.update_current_label()


    def operator_import(self, value):
        self.current_expression += str(value)
        if len(self.total_expression) == 0:
            self.total_expression += self.current_expression
        elif len(self.total_expression) != 0 and self.total_expression[-1] != self.current_expression:
            self.total_expression += self.current_expression
        else:
            self.total_expression += ''

        self.current_expression = ''
        self.update_total_label()
        self.update_current_label()

        
    def clear_button(self):
        button = tk.Button(self.button_frame, text='C', font=DIGIT_FONT_STYLE, command=self.clear, borderwidth=0, bg='red')
        button.grid(row=0, column=0, sticky=tk.NSEW)
    

    def clear(self):
        self.current_expression = ''
        self.total_expression = ''
        self.update_current_label()
        self.update_total_label()


    def delete_button(self):
        button = tk.Button(self.button_frame, text='DEL', font=SMALL_FONT_STYLE_2, command=self.delete, borderwidth=0, bg='silver')
        button.grid(row=0, column=4, sticky=tk.NSEW)
    

    def delete(self):
        if self.current_expression == '':
            self.current_expression = ''
        else:
            self.current_expression = self.current_expression.replace(self.current_expression[-1], '', 1)
        self.update_current_label()


    def fatorial_button(self):
        button = tk.Button(self.button_frame, text='n!', font=DIGIT_FONT_STYLE, 
                           command=self.fatorial_func , borderwidth=0, bg='silver')
        button.grid(row=3, column=0, sticky=tk.NSEW)
    

    def fatorial_func(self): 
        try:
            value = int(self.current_expression)
            self.total_expression += str(math.factorial(value))
            self.update_total_label()
            self.current_expression = ''
        except Exception:
            self.current_expression = 'Error'
        finally:
            self.update_current_label()


    def pi_number_button(self):
        button = tk.Button(self.button_frame, text='\u03C0', font=DIGIT_FONT_STYLE, command=self.pi_number , borderwidth=0, bg='silver')
        button.grid(row=4, column=0, sticky=tk.NSEW)

    
    def pi_number(self):
        self.current_expression += str(math.pi)
        self.update_current_label()


    def bracket_button(self):
        button = tk.Button(self.button_frame, text=')', font=DIGIT_FONT_STYLE, command=self.bracket_right, borderwidth=0, bg='silver')
        button.grid(row=5, column=1, sticky=tk.NSEW)
        button = tk.Button(self.button_frame, text='(', font=DIGIT_FONT_STYLE, command=self.bracket_left, borderwidth=0, bg='silver')
        button.grid(row=5, column=0, sticky=tk.NSEW)


    def bracket_left(self):
        self.current_expression += '('
        self.update_current_label()
    

    def bracket_right(self):
        if self.current_expression == '':
            self.current_expression = ''
        else:
            self.current_expression += ')'
        self.update_current_label()
    
    
    def sqrt_button(self):
        button = tk.Button(self.button_frame, text='\u221A', font=DIGIT_FONT_STYLE, command=self.sqrt, borderwidth=0, bg='silver')
        button.grid(row=2, column=0, sticky=tk.NSEW)
    

    def sqrt(self):
        self.current_expression = str(f'{eval(self.current_expression)**0.5}')
        self.update_current_label()
    

    def reverse_number_button(self):
        button = tk.Button(self.button_frame, text='\u215Fx', font=DIGIT_FONT_STYLE, command=self.reverse_number, borderwidth=0, bg='silver')
        button.grid(row=1, column=0, sticky=tk.NSEW)
    

    def reverse_number(self):
        try:
            self.current_expression = str(f'{eval(self.current_expression)**(-1)}')
        except Exception:
            self.current_expression = 'Error'
        finally:
            self.update_current_label()
    

    def square_button(self):
        button = tk.Button(self.button_frame, text='x\u00B2', font= DIGIT_FONT_STYLE, command=self.square, borderwidth=0, bg='silver')
        button.grid(row=1, column=1, sticky=tk.NSEW)


    def square(self):
        self.current_expression = str(f'{eval(self.current_expression)**2}')
        self.update_current_label()

    def cube_button(self):
        button = tk.Button(self.button_frame, text='x\u00B3', font= DIGIT_FONT_STYLE, command=self.cube, borderwidth=0, bg='silver')
        button.grid(row=1, column=2, sticky=tk.NSEW)


    def cube(self):
        self.current_expression = str(f'{eval(self.current_expression)**3}')
        self.update_current_label()


    def power_x_button(self):
        button = tk.Button(self.button_frame, text='x\u02b8', font= DIGIT_FONT_STYLE, 
                           command=lambda x='^': self.power_x(x), borderwidth=0, bg='silver')
        button.grid(row=1, column=3, sticky=tk.NSEW)
    

    def power_x(self, value):
        self.current_expression += value
        if len(self.total_expression) == 0:
            self.total_expression += self.current_expression
        elif len(self.total_expression) != 0 and self.total_expression[-1] != self.current_expression:
            self.total_expression += self.current_expression
        else:
            self.total_expression += ''

        self.current_expression = ''
        self.update_total_label()
        self.update_current_label()


    def sin_operator_button(self):
        button = tk.Button(self.button_frame, text='Sin(x)', font= SMALL_FONT_STYLE_2, command=self.sin_operator, borderwidth=0, bg='silver')
        button.grid(row=0, column=1, sticky=tk.NSEW)

    
    def sin_operator(self):
        self.total_expression += str(math.sin(int(self.current_expression)*math.pi/180))
        self.current_expression = ''
        self.update_current_label()
        self.update_total_label()


    def cos_operator_button(self):
        button = tk.Button(self.button_frame, text='Cos(x)', font= SMALL_FONT_STYLE_2, command=self.cos_operator, borderwidth=0, bg='silver')
        button.grid(row=0, column=2, sticky=tk.NSEW)

    
    def cos_operator(self):
        self.total_expression += str(math.cos(int(self.current_expression)*math.pi/180))
        self.current_expression = ''
        self.update_current_label()
        self.update_total_label()


    def tan_operator_button(self):
        button = tk.Button(self.button_frame, text='Tan(x)', font= SMALL_FONT_STYLE_2, command=self.tan_operator, borderwidth=0, bg='silver')
        button.grid(row=0, column=3, sticky=tk.NSEW)

    
    def tan_operator(self):
        self.total_expression += str(math.tan(int(self.current_expression)*math.pi/180))
        self.current_expression = ''
        self.update_current_label()
        self.update_total_label()



    def equal_button(self):
        button = tk.Button(self.button_frame, text='=', font=DIGIT_FONT_STYLE, command=self.evaluate, borderwidth=0, bg='LightSeaGreen')
        button.grid(row=5, column=4, sticky=tk.NSEW)


    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.total_expression = self.total_expression.replace('^', '**')
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ''
        except Exception:
            self.current_expression = 'Error'
        finally:
            self.update_current_label()


    def update_current_label(self):
        self.current_label.config(text=self.current_expression[:15])
    

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operators.items():
            expression = expression.replace(operator, f'{symbol}')
        self.total_label.config(text=expression)


    def run(self):
        self.window.mainloop()
    


if __name__ == '__main__':
    calc = Calculator()
    calc.run()
