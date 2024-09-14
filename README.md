# Microorganism Metabolic Potential Estimation Algorithm

## DESCRIPTION

This program estimates how much the value of a given objective function can change for a specific genome and determines the extent to which the inhibition of particular reactions influences this change.

The input to the program is a model containing a list of biochemical reactions, constraints, metabolites, and genes. For this model, the extreme value of the objective function is computed. The objective function can be customized.

During the execution of the program, genes are sequentially deactivated, leading to the cessation of the corresponding biochemical reactions, which affects the genome of the original microorganism. For each resulting genome, a new value of the objective function is calculated and compared to the original value. The output is a list of inhibited reactions and their impact on the change in the objective function, expressed as a percentage.


## TEST MODEL

As a test model, we consider the whole-genome model iCGB21FR of the bacterium *Corynebacterium glutamicum* ATCC 13032, provided by Maria Fedorovna Trofimova, a 4th-year student of the Faculty of Natural Sciences at Novosibirsk State University (supervised by Fyodor Vladimirovich Kazantsev, PhD, senior researcher at ICIG SB RAS). 

This model contains 1539 reactions, 1042 metabolites, and 805 genes. The objective function is set to be the pseudo-reaction for bacterial growth.


## REQUIREMENTS

The program is written in Python 3.9 and uses the following libraries:
- `numpy`
- `cobrapy`

## HOW TO RUN

To run the program, download the files `main_with_cobra.py` and `model.json`.

Install the required libraries:
```
pip install cobrapy
pip install numpy
```
To execute the program, run:
```
python main_with_cobra.py
```
## CHANGING THE MODEL

The `model.json` file contains all the information about the model, including the set of biochemical reactions, constraints, metabolites, and genes.

To change the model, modify the path in the program. See the example below.

## Example
```
from main_with_cobra import FBA

path_to_cobra_model_json = 'your_model_name.json'
model = FBA(path_to_cobra_model_json)
list_value_opt = model.algorithm()  # List of inhibited reactions
                                    # and their impact on the objective function in percentage terms.
```                                    

## MUTANTS OUTPUT

To output the mutants, use 
```print(list_value_opt)```

The file `mutants.txt` contains information about all inhibited reactions and their impact on the objective function when the program is run on the test model. Reactions are sorted in descending order of their influence on the growth of the objective function.


## COBRAPY DOCUMENTATION
For more information on how to use the cobrapy library, refer to the official documentation: [COBRApy Documentation](https://cobrapy.readthedocs.io/en/latest/index.html)
