from flask import render_template ,url_for,flash,redirect,request
from FoodIngredients import app
from FoodIngredients.output import output
from FoodIngredients.buy import buyItems
# from flask import redirect, url_for


import os


@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/',methods=['POST','GET'])
def predict():
    imagefile=request.files['imagefile']
    image_path=os.path.join(app.root_path,'static\\images\\demo_imgs',imagefile.filename)
    imagefile.save(image_path)
    img="/images/demo_imgs/"+imagefile.filename
    title,ingredients,recipe = output(image_path)
    print("image_path:predict",image_path)
    return render_template('predict.html',title=title,ingredients=ingredients,recipe=recipe,img=img)

@app.route('/<samplefoodname>')
def predictsample(samplefoodname):
    imagefile=os.path.join(app.root_path,'static\\images',str(samplefoodname)+".jpg")
    img="/images/"+str(samplefoodname)+".jpg"
    title,ingredients,recipe = output(imagefile)
    return render_template('predict.html',title=title,ingredients=ingredients,recipe=recipe,img=img)

@app.route('/buy', methods=['POST'])
def buy():
    ingredients = request.form.get('ingredients')
    ingredients_list = ingredients.split(", ")
    buyItems(ingredients_list)
    return redirect(url_for('home'))
    # add your code here to buy the grocery items
    # return 'Grocery items purchased successfully!' + ingredients
    # return render_template('')