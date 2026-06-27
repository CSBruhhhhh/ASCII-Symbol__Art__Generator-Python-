

import random
import string

def get_integer(numm):
    while True :
        try:
            n=int(input(numm))
            if n>0:
                return n
            else:
                print("Please put a positive integer.")
        except ValueError:
            print("Please put in a valid, positive integer.")


def valid_input(hey):
    if hey=="A":
        print("\nPlease input a valid option- A or B\n")
    elif hey=="B":
        print("\nPlease input a valid option- A or B or C or D etc.\n")
    



def hollow(hehe):
    while True:
        print(f"\nDo you want the {hehe} to be:", "\nA) Filled\n", "B) Hollow\n", sep="\n")
        ans= input("Enter the corresponding option: ").strip().capitalize()
        if ans=="A"or ans=="B":
            return ans
        else:
            valid_input("A")

def orientation(kaboom):
    while True:
        print(f"\nDo you want the {kaboom} to be:", "\nA) Horizontal\n", "B) Vertical\n", sep="\n")
        abc=input("Enter the corresponding option: ").strip().capitalize()
        if abc=="A" or abc=="B":
            return abc
        else:
            valid_input("A")
     

def length(brh):
     print(f"\nThe length you entered is the length of the side of the {brh} with the distance between 2 consecutive stars on the side of the {brh} being 1 unit\n")

def exit_thanks(useless_miwa):
    exit("\n Thank you for using the programme. :D\n")




def Up_Down(shape,h,side1,side2,ori1,ori2):
    print(f"\nDo you want the {shape} to be:\n\n A) {side1}({h} facing {ori1})\n\n B) {side2} ({h} facing {ori2})\n")
    
    while True:
        up_down=input("Enter the corresponding option: ").strip().title()
        if up_down in ["A","B"]:
            return up_down 
        else:
            valid_input("A")


def leaning_tower(monke):

    while True:
        print(f"\nDo you want the {monke} to be:\n A) Straight\n B) Tilted\n")
        ans=input("Enter your choice(A or B) here: ").strip().capitalize()
        if ans in ["A", "B"]:
            return ans
        else:
            valid_input("A")



def lets_larp():
    
    while True:
        print("Do you want the symbol from which  the shape to be made, to be :\n A) Manually chosen\n B) Randomly chosen\n")
        ans=input("Enter your choice(A or B) here: ").strip().capitalize()
        if ans in ["A", "B"]:
            return ans
        else:
            valid_input("A")




def just_this_once():

    print("\n So, you have chosen the FUN option. This is as choosing control is what LOSERS think.\n")

    the_omniscient_god_allmighty=string.punctuation+string.ascii_letters+string.digits
    
    aizo=random.choice(the_omniscient_god_allmighty)

    print(f'\nThe symbol Fate has decided to grant  you is: "{aizo}"!!\n')

    return aizo



def the_night_cometh():

    while True:    
        jkb = input("\nPlease enter a single symbol, you want to use to draw the shape with: ").strip()
        if len(jkb) == 1:
            return jkb
        else:
            print("Please enter a single symbol.")

def Wheel_of_Fortune(Hakari):
    The_White_tower= {
            "A":Rhombus,
            "B":Square,
            "C":Rectangle,
            "D":Pyramid,
            "E":Hourglass,
            "F":Right_Triangle,

        }  
    ans=random.choice(list(The_White_tower.keys()))
    print(f"\nFate has decided that the shape you will be getting is: {The_White_tower[ans].__name__}!!!\n")     #if you dont put .__name__ it will print the memory address of the function instead of the name of the function
    The_White_tower[ans](Hakari)




def Rhombus(gojo):
    shape="Square"
    length(shape)
    n=(get_integer("Enter the length of side of the "+ shape+": ") + 1)

    ans=hollow(shape)
    if ans=="A":
        for x in range(n):
            print(5*" "+2*(n-x)*" "+ (2*x +1)*f"{gojo} ")
    
        for x in range(n):
            print(5*" "+2*(x +2)*" "+(2*(n-x)-3)*f"{gojo} " )
    else:
        
        print(5*" "+(2*n)*" "+f"{gojo}")

        for x in range(1,n):
            print(5*" "+2*(n-x)*" "+ f"{gojo} "+(2*x -1)*"  "+f"{gojo}")
    
        for x in range(n-2):
            print(5*" "+2*(x +2)*" "+f"{gojo} "+(2*(n-1-x)-3)*"  "+f"{gojo} " )

        print(5*" "+(2*(n))*" "+f"{gojo}")





def Square(sukuna):
    shape="Square"
    tilt=leaning_tower(shape)
    
    

    if tilt=="A":

        length(shape)
        n=(get_integer("Enter the length of side of the "+ shape+": ") + 1)

        ans=hollow(shape)
        if ans=="A":
            for x in range(n):
                print(5*" " + (n)*f"{sukuna} ")
            
        else:
            for x in range (n):
                if x==0 or x==(n-1):
                    print(5*" " + (n)*f"{sukuna} ")
                else:
                    print(5*" "+f"{sukuna}"+ (2*(n-2)+1)*" "+f"{sukuna}")    
    
    else:
        Rhombus(sukuna)




def Rectangle(baka):
     shape="Rectangle"
     length(shape)
     l=(get_integer("Enter the length of the "+ shape+": ") + 1)
     b=(get_integer("Enter the breadth of the "+ shape+": ") + 1)
     ans=hollow(shape)

     if ans=="A":
        if l==b:
            print("This is a square,bruh .__." +"\n")

        for x in range(b):
            print (5*" "+l*f"{baka} ")                                          #filled


     else:
        if l==b:
            print("This is a square,bruh .__." + "\n")
            
        for x in range (b):
            if x==0 or x==(b-1):
                print(5*" "+ l*f"{baka} ")                                       #hollow
            else:
                print(5*" "+f"{baka}"+(2*(l-2)+1)*" "+f"{baka}")
            
     





def Pyramid(yuji):
    shape="Pyramid"
    length(shape)
    n=(get_integer("Enter the length of side of the "+ shape+": ") + 1)

    ans=hollow(shape)

    if ans=="A":
        for x in range(n):
            print(5*" "+2*(n-x)*" "+ (2*x +1)*f"{yuji} ")                   #filled

    else:


        for x in range(n):

            if 0<x<(n-1):
             print(5*" "+2*(n-x)*" " +f"{yuji}"+(4*x -1)*" "+f"{yuji}")         #hollow
            else:
                print(5*" "+2*(n-x)*" "+ (2*x +1)*f"{yuji} ")
    




def Right_Triangle(Yuta):
    shape="Right Triangle"
    length(shape)
    n=(get_integer("\nEnter the length of side of the "+ shape+": ") + 1)
    
    h="Hypotenuse"
    hol=hollow(shape)
    ori_y=Up_Down(shape,h, "Straight","Upside Down","up","down")
    ori_x=Up_Down(shape,h, "Left","Right","left","right")


    if hol=="A":

        if ori_y=="A":
            if ori_x=="A":
                for x in range (n):
                    print(5*" "+(n-x)*"  "+(x+1)*f"{Yuta} ")     #filled,up,left
            
            else:
                for x in range(n):
                    print(5*" "+(x+1)*f"{Yuta } ")              #filled,up,right
        
        else:
            if ori_x=="A":
                for x in range(n):
                    print(5*" "+(x)*"  "+(n-x)*f"{Yuta} ")               #filled,down,left
            else:
                for x in range(n):
                     print(5*" "+(n-x)*f"{Yuta} ")                  #filled,down,right
    
   
    else:
        if ori_y=="A":

           if ori_x=="A":
               print(5*" "+n*"  "+f"{Yuta} ") 
               for x in range(1,n-1):
                   print(5*" "+(n-x)*"  "+f"{Yuta} "+(x-1)*"  "+f"{Yuta} ")         #hollow,up,left
               print(5*" "+"  "+(n)*f"{Yuta} ")
            
           else:
                print(5*" "+f"{Yuta} ")
                for x in range(1,n-1):
                     print(5*" "+f"{Yuta} "+(x-1)*"  "+f"{Yuta} ")              #hollow,up,right
                print(5*" "+n*f"{Yuta} ")

        else:

            if ori_x=="A":
                print(5*" "+n*f"{Yuta} ")
                for x in range(1,n-1):
                    print(5*" "+(x)*"  "+f"{Yuta} "+(n-x-2)*"  "+f'{Yuta} ')           #hollow,down,left 
                print(5*" "+(n-1)*"  "+f"{Yuta} ")
            else:
                print(5*" "+n*f"{Yuta} ")

                for x in range(1,n-1):
                     print(5*" "+f"{Yuta} "+(n-x-2)*"  "+f"{Yuta} ")        #hoolow,down,right  
                print(5*" "+f"{Yuta} ")


def Hourglass(Flins):
    shape="Hourglass"
    print(f"The length you entered is the number of rows/columns in one lobe of a horizontal/vertical {shape} respectively.", end="\n")
    n=(get_integer("Enter the length of side of the "+ shape+": ") + 1)

    ori=orientation(shape)

    if ori=="A":
       ans=hollow(shape) 

       if ans=="A":
           n +=1
           for x in range(n-1):
               print(5*" "+(x+1)*f"{Flins} "+(4*(n-x-2))*" "+(x+1)*f"{Flins} ")
                                     
           for x in range(1,n-1):
               print(5*" "+(n-x-1)*f"{Flins} "+(4*(x))*" "+(n-x-1)*f"{Flins} ")

           
       else:
           
           print(5*" "+f"{Flins} "+ (4*(n-2))*" "+f"{Flins} " )
           for x in range(1,n-1):
               print(5*" "+f"{Flins} "+(x-1)*"  "+f"{Flins} "+(4*(n-x-2))*" "+f"{Flins} "+(x-1)*"  "+f"{Flins} ")

           for x in range(1,n-2):
               print(5*" "+f"{Flins} "+(n-x-3)*"  "+f"{Flins} "+4*(x)*" "+f"{Flins} "+(n-x-3)*'  '+f"{Flins} ")
           print(5*" "+f"{Flins} "+4*(n-2)*" "+f"{Flins} ")

               
       
    
    
    elif ori=="B":
    
        ans=hollow(shape)
 
        if ans=="A":
           for x in range(n):
                print(5*" "+2*(x +2)*" "+(2*(n-x)-1)*f"{Flins} " )
           for x in range(1,n):
               print(5*" "+2*(n-x+1)*" "+ (2*x +1)*f"{Flins} ")


        else:
            
            print("\n"+9*" "+((2*n)-1)*f"{Flins} ")
            for x in range(1,n-1):
                print(5*" "+2*(x +2)*" "+f"{Flins} "+(2*(n-x)-3)*"  "+f"{Flins} ")
            print(7*" "+2*n*" "+f"{Flins} ")
            for x in range(1,n-1):
               print(5*" "+2*(n-x+1)*" "+f"{Flins} "+ (2*x -1)*"  "+f"{Flins} ")
            print(9*" "+ (2*n -1)*f"{Flins} ")




     
    






def main():
    while True:
       
        print("\nFirst, please select the symbol you want to use for the shapes to be made with.")

        gambling=lets_larp()

        if gambling=="A":
            big_mama=the_night_cometh()
        else:
            big_mama=just_this_once()

        print( "\nThe options for shapes you have are: ",
              "a) SQUARE",
              "b) RECTANGLE",
              "c) PYRAMID/ISOSCELES TRIANGLE" ,
              "d) RIGHT TRIANGLE",
              "e) HOURGLASS/INFINITY",
              "f) RANDOM SHAPE",
              "g) QUIT PROGRAMME",
                
                
                sep= "\n")
#Tell the shape options

#Take the shape and assign it
        letter= input("Enter the letter corresponding with the shape: "+'\n').strip().capitalize()

        shapes= {
            "A":Square,
            "B":Rectangle,
            "C":Pyramid,
            "D":Right_Triangle,
            "E":Hourglass,
            "F":Wheel_of_Fortune,
            "G":exit_thanks,

        }  
        print("\n")
        #Build shape
    
        if letter in shapes:
            shapes[letter](big_mama)
            break
        else:
            valid_input("B")




    



if __name__ == "__main__":
    while True:
        main()
        ask=input("Do you want to continue in the programme?\n A) Continue\n B) Exit\n", ).strip().upper()


        while ask not in ["A","B"]:
            print('\nPlease enter "A" or "B"\n')
            
            ask=input("Do you want to continue in the programme?\n A) Continue\n B) Exit\n", ).strip().upper()
            
        if ask=="B":
            exit_thanks("2")



    