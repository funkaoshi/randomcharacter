# Random D&D Character Generator

By Ramanan Sivaranjan, 2012—

## Introduction

This is a small web application for generating random D&D characters. The
default is to create Basic (Moldvay) D&D characters, but it can generate a
variety of characters based on various systems similar to Basic D&D: Original
D&D, Holmes, etc.

## Supported Systems

- Abstract D&D Character
    - Basic D&D (Mentzer / Moldvay)
    - Holmes D&D
    - Little Brown Books (1974 Original D&D)
        - Carcosa
        - Masters of Carcosa! (my Carcosa game)
        - Apollyon
        - Pahvelorn
        - Delving Deeper
- Danger Time
- Adventure Game
- Fifth Edition D&D (Incomplete)

## Getting it Running

1. Install Flask (`pip install flask`). 
2. Run `python create.py`

## How It Works

This is a Flask web application. `create.py` is the flask app, which does all
the routing. `characterclass.py` contains data and tables about various D&D
systems and that sort of thing. `character.py` is where the magic happens. All
the generators live here. They are assembled by inheriting from more generic
chunks of code, mixing in features as needed. I'm still undecided if this is
the best way to do this or not. The project has sort of grown organically over
time, and I'm not sure I made the best choices. It has allowed me to make
several tweaked generators for friends for their particular house-ruled games,
which has been nice.

The generate for the fifth edition characters works slightly differently. It
takes a runs an incomplete character through a series of processors that add
more and more information to the character. I'm not sure this scheme works that
well either.

