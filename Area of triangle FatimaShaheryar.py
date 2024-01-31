print("You can enter the required information(base, height).")
print('Type xxx to stop')
print('This program gives the area of triangle')
print('USE ONLY LOWERCASE')
length=0
breadth=0
radius=0
area=0
sn='Y'
while sn=='Y' or sn=='y':
        breadth=int(input('Enter the base: '))
        length=int(input('Enter the height: '))
        area=(length*breadth*0.5)
        print('area: ',area)
        sn=input('Do you want to continue(y/n): ')
