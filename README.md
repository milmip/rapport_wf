# Paper template for EPFL

## Workflow

### Initialize the environement
Required : `tkinter` (you might have to run `apt install python3-tk`)

Run the following :
```
git clone https://github.com/milmip/rapport_wf.git
cd rapport_wf
make venv
make mpl-template
source venv/bin/activate
make build_mpt-env
```

### Create a *mpl figure*

To create a plot with `matplotlib`, go to the root project directory and : 
1. Run `cp figures/exemple.py figures/FigureXX.py`
2. Edit
3. Run `python3.11 figures/exemple.py -d 0`
4. Go step 2 if you're not happy
5. Save youre figure, run `make generate_figures` (`make clean_figures` to delete all)


