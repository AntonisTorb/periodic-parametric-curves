# Periodic Parametric Curves
A small GUI application showcasing the different parametric curves of the `sin(kt)` function, with the ability to modify the paramenter for each axis, as well as save the resulting graph.

## WARNING!
This application used PySimpleGUI for the GUI frontend. PySimpleGUI has recently become closed source in a disappointing decision, thus I would advise you to use the PySimpleGUI version specified in the `requirements.txt` file. For any future versions, I can guarantee neither the integrity nor the security of the package.

## How to run
Open the command line in the directory containing the `main.py` file and run the commmands: 
- `pip install -r requirements.txt `
- `python main.py`

The application should run, allowing you to modify the parameters and save the resulting graph:

<img src="https://raw.githubusercontent.com/AntonisTorb/periodic-parametric-curves/main/demo.jpg" alt="demo image" style="width:50%; height:50%;"/>

## Testing different functions
If you would like to use functions other than `sin`, you can specify them `get_datapoints` function. By setting `x = t` you can also plot any single function defined as `y`.
