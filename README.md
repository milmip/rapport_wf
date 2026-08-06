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

1. Ensure you've `source venv/bin/activate`.
2. Run `cp figures/exemple.py figures/FigureXX.py`.
3. Edit.
4. Run `python3.11 figures/exemple.py -d 0`.
5. Go step 3 if you're not happy.
6. Save your figure, run `make figures` (`make clean_figures` to delete all).

### Dealing with latex preview

If you've got `localleaf`, just run :
```
localleaf -m latex/master.tex ./ -- --outdir=build/ --auxdir=aux/
```

then launch your favourite pdf viewer (zathura) on `build/master.pdf`. It will be 
automatically be refreshed.

### Classic Workflow

Once you've initialized all you need. It's a classic git workflow, note one things : 

In case the push of the `main` branch fails : 

1. Run `git checkout -b my_version && git push origin my_version`.
2. Go to GitHub.
3. Do a Pull Request.
4. Resolve conflicts.
5. Merge. 
6. Delete your branch. 

### You write in your shitty Overleaf web interface ? Here are the instructions

#### Initialize

On the web interface, do : 
1. `New project > (import) GitHub repo`
2. Chose the project, normally you would have been added to a GitHub project previously.
3. Done.

#### Workflow
You might be writing at the same time that your wise collegues using their own 
local editor. Don't worry, mabe one day you would. For the moment you must know one things:
```
(one the left) Integration > GitHub 
```

Then 3 cases: 
- `pull`, if you need a newer version from GitHub.
- `push`, the inverse.
- `! Your changes in Overleaf and GitHub could not be automatically merged.`, it says that you and the version from GitHub is overlapping each other.
    1. Let the popup open.
    2. Go to GitHub.
    3. A `overleaf-xxxx-xx-xx-xxxx` branch will pop.
    4. Do a Pull Request.
    5. Resolve conflicts.
    6. Merge. 
    7. Delete the OL branch. 
    8. Return on OL and continue.

