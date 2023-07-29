# pythagorean-3d-solver

A script to find solutions to the Pythagorean theorem in three dimensions using SMT solving.

More precisely, this script determines all integer solutions to the equation
*-t*<sup>2</sup> + *x*<sup>2</sup> + *y*<sup>2</sup> = 1 within given bounds and prints them to the console.
Additionally, it writes a CSV file called `solutions.csv` containing a list of all determined solutions.

## Usage

After cloning the repository, make sure that all dependencies are installed. This can be done by running the following
command:

```bash
pip install -r requirements.txt
```

*Note that it is a best practice to do this in a virtual environment.*

Run the script:

```
python3 main.py
```

If you wish to change the bounds for the variables *x*, *y*, and *t*, you can do so by changing the values of the
constants `X_MIN`/`X_MAX`, `Y_MIN`/`Y_MAX`, and `T_MIN`/`T_MAX` in the file `main.py`. To change the number of obtained
solutions, change the value of the constant `MAX_SOLUTIONS` in the same file.
