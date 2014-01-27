from flask import Flask, request, url_for, render_template, redirect
from random import randrange

app = Flask(__name__)
d = {}

@app.route("/", methods = ["POST", "GET"])
def index():
   return render_template("home.html")
   
@app.route("/appetizer", methods = ["POST", "GET"])
def appetizer():
   global d
   if request.method=="GET":
      return render_template("appetizer.html")
   else:
      button = request.form['button']
      if button=="Go Back":
         return redirect(url_for('index'))
      else:
         if ('gender' in request.form and 'veg' in request.form and 'thirst' in request.form and 'digestion' in request.form and 'boldness' in request.form):
            d = {'gender':int(request.form['gender']),
                 'vegetarian':int(request.form['veg']),
                 'thirst':int(request.form['thirst']),
                 'digestion':int(request.form['digestion']),
                 'boldness': int(request.form['boldness'])}
            return process()
         else:
            return "Please answer all questions!<br>" + render_template("appetizer.html")
   
def process():
   global d
   
   calorieCount = 0

   maleOptionsV = [ ["Why are you a male vegetarian???", 0] ]
   femaleOptionsV = [ ["Falafel", 300], ["Mixed veggies", 150] ]
   maleOptionsNV = femaleOptionsNV = [ ["Chicken", 300], ["Lamb", 350], ["A chicken-falafel combo", 350], ["A chicken-lamb combo", 450], ["A chicken-lamb-falafel combo",500], ["Fish",250], ["Philly cheese steak", 450], ["A cheeseburger", 600] ]
   isVeg = [maleOptionsV, femaleOptionsV]   
   isNotVeg = [maleOptionsNV, femaleOptionsNV]   
   possibilities = [ isVeg, isNotVeg ]
   

   yes = [ [", and a Snapple.", 190], [", and a Sprite.",140], [", and a Coke.",140], [", and a Nestea.", 120], [", and a Bottle of Water.", 0] ]
   no = [ [". And if you're not thirsty yet, you will be.", 0] ]
   thirst = [yes, no]
   

   boldness = [ [" in a salad ", 30], [" in a pita ", 200], [" over rice ", 350] ]
   
   notConcerned = [ [" with white sauce, hot sauce, and BBQ sauce", 125] ]
   someConcern = [ [" with white sauce", 50], [" with white sauce and BBQ sauce", 100] ]
   veryConcerned = [ [" (no sauce)", 0] ]
   concern = [notConcerned, someConcern, veryConcerned]
   
   dishOptions = possibilities[d['vegetarian']][d['gender']]
   dish = dishOptions[randrange(0, len(dishOptions))]
   typeOfDish = dish[0]
   calorieCount += int(dish[1])


   typeOfFormat = boldness[d['boldness']][0]
   if (typeOfDish != 'A cheeseburger'): 
      calorieCount += int(boldness[d['boldness']][1])

   sauceOptions = concern[d['digestion']]
   sauce = sauceOptions[randrange(0, len(sauceOptions))]
   typeOfSauce = sauce[0]
   if (typeOfDish != 'A cheeseburger'):
      calorieCount += int(sauce[1])

   drinkOptions = thirst[d['thirst']]
   drink = drinkOptions[randrange(0, len(drinkOptions))]
   typeOfDrink = drink[0]
   calorieCount += int(drink[1])

   if (typeOfDish == "Why are you a male vegetarian???"):
      return render_template("MVresults.html",insult=typeOfDish);
   elif (typeOfDish != 'A cheeseburger'):
      return render_template("results.html", typeOfDish=typeOfDish, typeOfFormat=typeOfFormat, typeOfSauce=typeOfSauce, typeOfDrink=typeOfDrink,calorieCount=calorieCount)
   else:
      return render_template("results.html", typeOfDish=typeOfDish, typeOfFormat=typeOfFormat, typeOfSauce=typeOfSauce, typeOfDrink=typeOfDrink, calorieCount=calorieCount)

if __name__ == "__main__":
   app.debug = True
   app.run(host="0.0.0.0",port=5000)
