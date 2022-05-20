import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def objects_delete(parent):
    children = parent.winfo_children()
    children[-1].destroy()
    children[-2].destroy()


def plot(parent, formula, data):
    # the figure that will contain the plot
    fig = Figure(figsize=(5, 5), dpi=100)

    # adding the subplot
    plt = fig.add_subplot(111)
    plt.set_xlabel("x")
    plt.set_ylabel("y(x)")
    plt.set_title(f'Function Graph y(x)={formula}')
    plt.plot(data,  marker="o")

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,  master=parent)
    canvas.draw()

    # Create back button
    plot_button = tk.Button(master=parent, command=lambda: objects_delete(parent), text="<-")
    plot_button.grid(row=0, column=0, sticky=tk.NW)

    # placing the canvas on the Tkinter root
    canvas.get_tk_widget().grid(row=0, column=0)


def formula_handling(formula):
    return formula.strip().replace('^', '**').replace('X', 'x')


def get_result(x_min, x_max, formula):
    formula = formula_handling(formula)
    return [eval(formula) for x in range(x_min, x_max)]


def show_result(root, x_min_var, x_max_var, formula_var):
    try:
        x_min = int(x_min_var.get())
        x_max = int(x_max_var.get())
        formula = formula_handling(formula_var.get())
        results = get_result(x_min, x_max, formula)
        plot(root, formula_var.get(), results)
    except Exception as e:
        tk.messagebox.showerror(e.__class__.__name__, e)


def main():
    # Basic Configuration
    root = tk.Tk()
    root.title('Function Plotter')
    root.geometry("500x500")
    root.resizable(False, False)

    # Labels Section
    label1 = tk.Label(root, text="X Min:").grid(row=1, column=0)
    label2 = tk.Label(root, text="X Max:").grid(row=2, column=0)
    label3 = tk.Label(root, text="Formula:").grid(row=3, column=0)

    # Variable Section
    x_min_var = tk.StringVar()
    x_max_var = tk.StringVar()
    formula_var = tk.StringVar()

    # Entry Section
    x_min_entry = tk.Entry(root, textvariable=x_min_var).grid(row=1, column=2)
    x_max_entry = tk.Entry(root, textvariable=x_max_var).grid(row=2, column=2)
    formula_entry = tk.Entry(root, textvariable=formula_var).grid(row=3, column=2)

    # Button Section
    plot_button = tk.Button(master=root, command=lambda: show_result(root, x_min_var, x_max_var, formula_var),
                            text="Plot")
    plot_button.grid(row=4, column=2, sticky=tk.E)

    root.mainloop()


if __name__ == '__main__':
    main()
