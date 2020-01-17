# What is it?

Ok, in Brazil we have a name for this: **GAMBIARRA**. If you look for translations, you will find something like "workaround", but this is not completely correct. Gambiarra is an expression of art. A good Gambiarra is an epitome of creative minds solving problems.

## From LucidChart to Styleguidist

I have a giant chart for documenting a ReactJS project, with components connected by arrows which indicate imports.

LucidChart can export its diagrams into a CSV file, where each row is an element. If it's an arrow, the row contains the if of both connected elements by this arrow.

All what I did is a Python script that read this CSV and write some document fragments that I'll later paste on my project. Those fragments, if placed on right places, are recognizable by Styleguidist.

## Use

This is a Gambiarra, made to be a fast solution, so do not expect a well-over solution.

Python guys usually set a [virtual env](https://docs.python.org/3/library/venv.html) to do things, do as you wish; Python guys don't rule you.

To use this, you will need [Pandas](https://pandas.pydata.org/), so, dunno, maybe this:

```bash
pip install pandas
```

And then, just go on this project directory and do the things happen.

```bash
python main.py
```

If it do not work, well... I'm sorry, I tried.

If the things work well, you will have a `list.md` file with a list of child and parents of components. The actual file is in Portuguese, cause, y'know, it's a Brazillian documentation. If you want this in, dunno, maybe Esperanto, line 65 is where you'll find the string bases.

You alse will have a `docs/` folder with a lot of `componentName.md` files with some boilerplate for writting examples in Styleguidist.

## Things that would be nice to have, but I don't have cause this is supposed to be a fast solution, and I don't even know why am I writting a so big Readme...

- It would be nice if the snippets from `list.md` could be actually pasted directly on the `component.js` file.

- The boilerplate does not list any props. Some gambiarra to find the required props and just write `<Component prop=''>` would be nice too.