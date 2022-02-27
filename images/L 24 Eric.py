from tkinter import HIDDEN, NORMAL,Tk, Canvas 

def toggle_eyes():
    current_color=c.itemcget(eye_right,'fill')
    if current_color=='white':
        new_color=c.body_color
    else:
        new_color='white'
    current_state=c.itemcget(pupil_left,'state')
    new_state=NORMAL if current_state==HIDDEN else HIDDEN
    c.itemconfigure(pupil_left,state=new_state)
    c.itemconfigure(pupil_right,state=new_state)
    c.itemconfigure(eye_left,fill=new_color)
    c.itemconfigure(eye_right,fill=new_color)
    c.itemconfigure(pupil2_left,state=new_state)
    c.itemconfigure(pupil2_right,state=new_state)

def blink():
    toggle_eyes()
    root.after(250,toggle_eyes)
    root.after(3000,blink)
    
def toggle_tongue():
    if not c.tongue_out:
        c.itemconfigure(tongue_tip,state=NORMAL)
        c.itemconfigure(tongue_main,state=NORMAL)
        c.tougue_out=True
    else:
        c.itemconfigure(tongue_tip,state=HIDDEN)
        c.itemconfigure(tongue_main,state=HIDDEN)
        c.tongue_out=False

    
def my_test(event):
#    if(event.x>=20 and event.x<=350)and(enent.y>=20 and event.y<=350):
    c.itemconfigure(arm_right,state=HIDDEN)
    c.itemconfigure(wave_arm,state=NORMAL)
    c.itemconfigure(hands_right,state=HIDDEN)
    c.itemconfigure(wave_hand,state=NORMAL)
#    return

def stop_wave_hand(event):
    c.itemconfigure(arm_right,state=NORMAL)
    c.itemconfigure(wave_arm,state=HIDDEN)
    c.itemconfigure(hands_right,state=NORMAL)
    c.itemconfigure(wave_hand,state=HIDDEN)
    return

def sad():
    if c.happy_level==0:
        c.itemconfigure(arm_right,state=NORMAL)
        c.itemconfigure(wave_arm,state=HIDDEN)
        c.itemconfigure(hands_right,state=NORMAL)
        c.itemconfigure(wave_hand,state=HIDDEN)
    else:
        c.happy_level=c.happy_level-1
    root.after(500,sad)

        

root=Tk()
c=Canvas(root,width=600,height=600)
c.configure(bg='white',highlightthickness=0)
c.body_color='deepskyblue'
#head
head=c.create_oval(150,100,450,400,outline="black",fill='deepskyblue')
#face
face=c.create_oval(175,150,425,400,fill='white')
#eyes
eye_right=c.create_oval(250,115,300,180,fill="white")
eye_left=c.create_oval(300,115,350,180,fill="white")

pupil_right=c.create_oval(280,136,295,160,fill="black")
pupil_left=c.create_oval(305,136,320,160,fill="black")

pupil2_right=c.create_oval(286,142,290,152,fill="white")
pupil2_left=c.create_oval(310,142,314,152,fill="white")
#nose
nose=c.create_oval(290,170,310,190,fill="red")
nose=c.create_line(300,190,300,300,fill="black")
#mouth
mouth=c.create_arc(175,50,425,300,width=1,style="arc",start=240,extent=60)
#beard
beard1_left=c.create_line(200,240,280,240,fill='black',width=1.5)
beard1_right=c.create_line(320,240,400,240,fill='black',width=1.5)

beard2_left=c.create_line(210,280,280,260,fill='black',width=1.5)
beard2_right=c.create_line(320,260,390,280,fill='black',width=1.5)

beard3_left=c.create_line(210,200,280,220,fill='black',width=1.5)
beard3_right=c.create_line(320,220,390,200,fill='black',width=1.5)
#arm
arm_left=c.create_arc(-75, 325,265,665,width=1,start=35,extent=20,style="pieslice",outline='black',fill='deepskyblue')
arm_right=c.create_arc(335, 325,675,665,width=1,start=125,extent=20,style="pieslice",outline='black',fill='deepskyblue',state=NORMAL) 
arm2_right=c.create_arc(50, 450,140,540,width=1,start=35,extent=20,style="pieslice",outline='white',fill='white')
arm2_left=c.create_arc(460, 450,550,540,width=1,start=125,extent=20,style="pieslice",outline='white',fill='white')
wave_arm=c.create_polygon(410,360,460,320,470,350,410,415,width=1,fill='deepskyblue',outline='black',state=HIDDEN)

#hands
hands_left=c.create_oval(120, 430,160,470,outline="black",fill="white")
hands_right=c.create_oval(440, 430,480,470,outline="black",fill="white",state=NORMAL)
wave_hand=c.create_oval(445,313,485,353,outline='black',fill='white',state=HIDDEN)
#body
body=c.create_rectangle(190,350,410,550,fill='deepskyblue')
#belly
belly=c.create_oval(215,340,385,500,outline='',fill="white")
#treasure bag
treasurebag=c.create_arc(240,360,360,480,start=180,width=1,extent=180,fill="white")
#bells
bells=c.create_line(190,355,410,355,width=15,capstyle='round',fill="red")

bells2=c.create_oval(286,353,314,381,fill="yellow")
bell_left=c.create_line(288,362,313,362,fill="black")
bell_right=c.create_line(287,366,314,366,fill="black")
bell3=c.create_oval(297,369,303,375,fill="red")
bell4=c.create_line(300,375,300,381,fill="black")
#abdomen
abdomen=c.create_oval(280,535,320,575,outline='',fill="white")
#feets
feet_right=c.create_oval(180,537,290,573,fill="white")
feet_left=c.create_oval(310,537,420,573,fill="white")

c.pack()
c.bind('<Motion>',my_test)
c.bind('<Leave>',stop_wave_hand)
c.bind_all('<Double-1>',my_test)
c.happy_level=10
root.after(5000,sad)
root.after(1000,blink)
root.mainloop()
