import tkinter #knižka tkinter
canvas=tkinter.Canvas(width=800,height= 200) #velkost okna
canvas.pack() #okno

def budovy(): #funkcia na kreslenie budovy
    subor=open('zastavba_na_ulici.txt') #otvaram textovy subor
    a=int(entry1.get())
    x=10
    y=150

    if vyska >0: #ak plati, urobí sa obdlžnik
        canvas.create_rectangle(x,y-vyska,x+sirka,y,fill='grey') #obdlžnik
    else:
        canvas.create_line(x,y,x+sirka,y,width=3,fill='green') #stavanie
    if vyska !=0 
        canvas.create_line(x,y-vyska,x,y-vyska2,width=3,fill='red') #nakresli sa červena čiara 
    x+=sirka #x sa nafuknesirka
    subor.close() #zatvor subor

entry1=tkinter.Entry() #štvorček na písanie
entry1.pack() #štvorček
button1=tkinter.Button(text='kresli', command=budovy) #spravi sa tlačidlo
button1.pack() #tlačitko
canvas.mainloop() #ide to znova
