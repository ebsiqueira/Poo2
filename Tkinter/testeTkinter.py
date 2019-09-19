from tkinter import *

janelaPrincipal = Tk()
stringEmail = StringVar(value='Email')
email = Entry(janelaPrincipal, textvariable=stringEmail)
email.pack(pady=15, side=TOP)
stringUsername = StringVar(value='Username')
username = Entry(janelaPrincipal, textvariable=stringUsername)
username.pack(pady=15, side=TOP)
stringPassword = StringVar(value="********")
password = Entry(janelaPrincipal, textvariable=stringPassword, show='*')
password.pack(pady=15, side=TOP)
submit = Button(janelaPrincipal, text='SUBMIT', command= lambda:
enviarFormulario())
submit.pack(pady=15, side=TOP)
janelaPrincipal.mainloop()