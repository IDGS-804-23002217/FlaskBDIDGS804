from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask_migrate import Migrate #agregar referencia de migracion
from flask import g
import forms
from models import db
from models import Alumnos

app= Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate=Migrate(app,db) #migracion a db
csrf= CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

@app.route("/",methods=['GET','POST'])
@app.route("/index")
def index():
	create_form=forms.UserForm(request.form)
	#tem = Alunos.query('select * from alumnos')
	alumno=Alumnos.query.all()
	return render_template("index.html",form=create_form,alumno=alumno)

@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
    alumno_class=forms.UserForm(request.form)
    if request.method=='POST':
        alum=Alumnos(nombre=alumno_class.nombre.data,
        			apellidos=alumno_class.apellidos.data,
        			email=alumno_class.email.data,
					telefono=alumno_class.telefono.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("Alumnos.html", form=alumno_class)
 
@app.route("/detalles", methods=['GET','POST'])
def detalles():
	create_form=forms.UserForm(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		# select * from alumnos where id == id 
		alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
		id=request.args.get('id')
		nombre=alum1.nombre
		apellidos=alum1.nombre
		email=alum1.email
		telefono=alum1.telefono

	return render_template('detalles.html', id=id, nombre=nombre, apellidos=apellidos, email=email, telefono=telefono)

@app.route('/modificar', methods=['GET','POST'])
def modificar():
	create_form=forms.UserForm(request.form)
	if request.method == 'GET':
		id=request.args.get('id')
		#Select * from alunos where id = id
		alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
		create_form.id.data=alum1.id
		create_form.nombre.data=alum1.nombre
		create_form.apellidos.data=alum1.apellidos
		create_form.email.data=alum1.email
		create_form.telefono.data=alum1.telefono
	
	if request.method == 'POST':
		id=create_form.id.data
		#Select * from alunos where id = id
		alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
		#id=create_form.id.data
		alum1.id=create_form.id.data
		alum1.nombre=create_form.nombre.data
		alum1.apellidos=create_form.apellidos.data
		alum1.email=create_form.email.data
		alum1.telefono=create_form.telefono.data
		db.session.add(alum1)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("modificar.html", form=create_form)


@app.route('/eliminar', methods= ['GET', 'POST'])
def eliminar():
	create_form=forms.UserForm(request.form)
	if request.method == 'GET':
		id=request.args.get('id')
		#Select * from alunos where id = id
		alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
		create_form.id.data=request.args.get('id')
		create_form.nombre.data=alum1.nombre
		create_form.apellidos.data=alum1.apellidos
		create_form.email.data=alum1.email
		create_form.telefono.data=alum1.telefono

	if request.method == 'POST':
		id=create_form.id.data
		alum = Alumnos.query.get(id)
		#delete from alumnos where id = id
		db.session.delete(alum)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("eliminar.html", form=create_form)
		

if __name__ == '__main__':
	csrf.init_app(app)
	
	with app.app_context():
		db.create_all()
	
	app.run()
