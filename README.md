# Restaurant Orders 🍽:
Restaurant Orders was a project made for study purpose.

## About:
In this project, I developed a tool to generate menus, considering possible dietary restrictions and ingredient availability in stock. Throughout this project, I built tests for already implemented classes. I also implemented a new class to map dishes and their respective recipes (ingredients and quantities), as well as a class that generates the menus to be displayed to the people who frequent the establishment, and another class that manages ingredient stock.

### Skills practiced:

- Applying the concept of Hashmaps using Python's Dict and Set data structures.
- Applying software testing knowledge.
- Applying object-oriented programming knowledge.

## Run locally:
- First clone the repository into your machine;
```
git clone git@github.com:GabiNamu/Tryunfo.git
```
- Go to the project directory:
```
cd restaurant-orders
```
 - Create the virtual environment for the project:
```
python3 -m venv .venv && source .venv/bin/activate
```
- Install dependencies;
```
python3 -m pip install -r dev-requirements.txt
```
### Main technologies:
- Python;
- Pytest;
- Flake8;

## Contributors: 
I made only:
 - src/menu_data.py;
 - src/menu_builder.py -> only the get_main_menu;
 - src/inventory_control.py -> only the check_recipe_availability and consume_recipe methods;

 - tests/ingredient/test_ingredient.py
 - tests/dish/test_dish.py
--------
the others files were made by trybe.

