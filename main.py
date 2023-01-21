from tkinter import Canvas  # For type hint
import numpy as np 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from matplotlib.figure import Figure
from matplotlib.axes._subplots import Subplot  # For type hint
import PySimpleGUI as sg 


def get_datapoints(k1: int, k2: int) -> tuple[np.ndarray, np.ndarray]:
    '''Returns the datapoints for the graph creation.'''

    t = np.linspace(0.001, 10, 1000)
    
    x = np.sin(t*k1)
    y = np.sin(t*k2)
    return x, y


def draw_figure(canvas: Canvas, figure: Figure) -> FigureCanvasTkAgg:
    '''Draws the figure on the canvas element, returning the tkinter agg canvas.'''

    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def initialize_fig() -> tuple[Subplot, Figure]:
    '''Returns the subplot and the figure after setting the initial parameters and visual elements.'''

    fig = Figure((6,6))
    ax = fig.add_subplot(111)
    ax.set_xlabel("x = sint")
    ax.set_ylabel("y = sin2t")
    ax.grid()
    x, y = get_datapoints(1,2)
    ax.set_title("Parametric curve, 1 to 2")
    ax.plot(x, y)
    return ax, fig

def main():
    layout = [
        [sg.Canvas(size=(600, 600), key='-CANVAS-')],
        [sg.Frame("Parameters", [
            [sg.Text("k1:"), sg.Push(), sg.Slider(range=(1, 20), default_value=1, size=(60, 10), orientation='h', key='-SLIDER1-', enable_events=True)],
            [sg.HorizontalSeparator()],
            [sg.Text("k2:"), sg.Push(), sg.Slider(range=(1, 20), default_value=2, size=(60, 10), orientation='h', key='-SLIDER2-', enable_events=True)]
        ], expand_x=True)],
        [sg.Button("Save"), sg.Push(), sg.Button('Quit')]
    ]

    window = sg.Window('Parametric Curves', layout, finalize=True, element_justification='center')

    canvas = window['-CANVAS-'].tk_canvas

    ax, fig = initialize_fig()

    fig_agg = draw_figure(canvas, fig)

    while True:
        event, values = window.read()
        match event:
            case sg.WIN_CLOSED | "Quit":
                break
            case '-SLIDER1-' | '-SLIDER2-':
                k1 = values['-SLIDER1-']
                k2 = values['-SLIDER2-']
                ax.cla()
                ax.set_xlabel(f"x = sin{int(k1)}t")
                ax.set_ylabel(f"y = sin{int(k2)}t")
                ax.grid() 
                x, y = get_datapoints(k1, k2)
                ax.set_title(f"Parametric curve, {int(k1)} to {int(k2)}")
                ax.plot(x, y)
                fig_agg.draw()
            case "Save":
                k1 = values['-SLIDER1-']
                k2 = values['-SLIDER2-']
                fig.savefig(f"{int(k1)}_to_{int(k2)}_parametric.png")
    window.close()

if __name__ == "__main__":
    main()