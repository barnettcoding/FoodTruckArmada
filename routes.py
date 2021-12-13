from app import app
from flask import render_template
@app.route('/')
@app.route('/trucks')
def showtrucks():
    return render_template('trucks.html', trucks = 'trucks')

@app.route('/truck/<int:truck_id>/')
@app.route('/truck/<int:truck_id>/menu')
def showMenu(truck_id):
    return render_template('menu.html')

@app.route('/truck/<int:truck_id>/menu/new')
def newMenuItem(truck_id):
    return render_template('newMenuItem.html')

@app.route('/truck/<int:truck_id>/menu/<int:menu_id>/edit')
def editMenuItem(truck_id, menu_id):
    return render_template('editMenuItem.html')

@app.route('/truck/<int:truck_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(truck_id, menu_id):
    return render_template('deleteMenuItem.html')