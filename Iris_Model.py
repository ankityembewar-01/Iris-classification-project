#Import basic modules 
import pandas as pd
from sklearn.linear_model import LogisticRegression
from tkinter import*
from PIL import Image, ImageTk
root = Tk()
root.geometry("800x480")
root.resizable(0,0)
root.title("Iris Classifier")
root.configure(background='black')

#import icon
photo=PhotoImage(file="C:\ml project\iris_1.png")
root.iconphoto(False,photo)

# creating model
df = pd.read_csv(r"C:\ml project\iris.csv",index_col=0)
from sklearn.preprocessing import LabelEncoder
label = LabelEncoder()
df['Species'] = label.fit_transform(df['Species'])

x = df.iloc[:,:-1]
y = df.iloc[:,-1]
model = LogisticRegression(max_iter=2000)
model.fit(x,y)

# geting input 
sl = DoubleVar()
sw = DoubleVar()
pl = DoubleVar()
pw = DoubleVar()
z = StringVar()

#creating function
def show():
    a = sl.get()
    b = sw.get()
    c = pl.get()
    d = pw.get()
    e = [[a,b,c,d]]
    prediction = model.predict(e)[0]
    if prediction == 0:
        z.set("Iris classified as Setosa")
        load = Image.open("C:\\ml project\\setosa.jpeg")
        render = ImageTk.PhotoImage(load)
        img = Label(root, image=render)
        img.image = render
        img.place(x=490, y=88)
    elif prediction == 1:
        z.set("Iris classified as Versicolor")
        load = Image.open("C:\\ml project\\versicolor.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(root, image=render)
        img.image = render
        img.place(x=490, y=88)
    else:
        z.set("Iris classified as Verginica")
        load = Image.open("C:\\ml project\\verginca.jfif")
        render = ImageTk.PhotoImage(load)
        img = Label(root, image=render)
        img.image = render
        img.place(x=490, y=88)


#building frontend
l0 = Label(root,text="Iris Classification",font=("Arial Black",30,UNDERLINE),fg="cyan2",background='black')
l0.place(x=200,y=5)

l1 = Label(root,text="Sepal Length (in cm):",font=("Times New Roman",20,'bold'),fg="OliveDrab1",background='black')
l1.place(x=30,y=82)
e1 = Entry(root,font=("Arial Black",15),width="10",textvariable=sl,justify='center')
e1.place(x=300,y=88)

l2 = Label(root,text="Sepal Width (in cm):",font=("Times New Roman",20,'bold'),fg="OliveDrab1",background='black')
l2.place(x=30,y=152)
e2 = Entry(root,font=("Arial Black",15),width="10",textvariable=sw,justify='center')
e2.place(x=300,y=158)

l3 = Label(root,text="Petal Length (in cm):",font=("Times New Roman",'20','bold'),fg="OliveDrab1",background='black')
l3.place(x=30,y=222)
e3 = Entry(root,font=("Arial Black",15),width="10",textvariable=pl,justify='center')
e3.place(x=300,y=228)

l4 = Label(root,text="Petal Width (in cm):",font=("Times New Roman",'20','bold'),fg="OliveDrab1",background='black')
l4.place(x=30,y=292)
e4 = Entry(root,font=("Arial Black",15),width="10",textvariable=pw,justify='center')
e4.place(x=300,y=298)

b1 = Button(root,text="Predict",bg="red",fg="white",font=('Times New Roman',20),relief="raised",command=show)
b1.place(x=140,y=380,height=50,width=200)

e5 = Entry(root,font=("Arial Black",15),width="10",textvariable=z,justify='center',relief='solid',bg="black",fg="yellow")
e5.place(x=470,y=385,height=40,width=300)


root.mainloop()
