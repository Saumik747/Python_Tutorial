Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: D:\python savefile\practicals\prctl1.py ==============
Enter the string: hello
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
Continue(y/n)? y
Enter the string: string
{'s': 1, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1}
Continue(y/n)? n
>>> 
============== RESTART: D:\python savefile\practicals\prctl2.py ==============
Enter a String: hello world
Expected Result:  held
want to continue(y/n)y
Enter a String: python programming
Expected Result:  pyng
want to continue(y/n)n
>>> 
============== RESTART: D:\python savefile\practicals\prctl3.py ==============
Enter a String: programming
Result:  programmly
continue(y/n)?y
Enter a String: hello
Result:  helloing
continue(y/n)?y
Enter a String: th
Empty String
continue(y/n)?n
>>> 
============== RESTART: D:\python savefile\practicals\prctl4.py ==============
Enter a String :hello to python and html
Enter a character to replace: @
Result:  hello to pyt@on and @tml
continue(y/n)?y
Enter a String :string strings 
Enter a character to replace: #
Result:  string #tring# 
continue(y/n)?n
>>> 
============== RESTART: D:\python savefile\practicals\prctl5.py ==============
Enter Number of elements: 4
Enter range upper limit3
a
b
c
d
['a1', 'b1', 'c1', 'd1', 'a2', 'b2', 'c2', 'd2']
continue(y/n)? y
Enter Number of elements: 5
Enter range upper limit2
a
b
c
d
e
['a1', 'b1', 'c1', 'd1', 'e1']
continue(y/n)? n
>>> 
============== RESTART: D:\python savefile\practicals\prctl6.py ==============
Enter Number of elements: 5
11
28
97
5
15
[11, 28, 97, 5, 15]
112897515
continue(y/n)? y
Enter Number of elements: 3
11
30
40
[11, 30, 40]
113040
continue(y/n)? n
>>> 
============== RESTART: D:\python savefile\practicals\prctl7.py ==============
enter no of rows 2
enter no of columns 2
element 1
element 2
element 3
element 4
1 2 
3 4 
transposing matrix
1 3 
2 4 
continue(y/n)? y
enter no of rows 3
enter no of columns 3
element 1
element 2
element 3
element 4
element 5
element 6
element 7
element 8
element 9
1 2 3 
4 5 6 
7 8 9 
transposing matrix
1 4 7 
2 5 8 
3 6 9 
continue(y/n)? n
>>> 
============== RESTART: D:\python savefile\practicals\prctl8.py ==============
Enter value of rows and cols for both matrix
enter no of rows 2
enter no of columns 2
Matrix a
element 1
element 2
element 3
element 4
Matrix b
element 5
element 6
element 7
element 8
matrix a
1 2 
3 4 
matrix b
5 6 
7 8 
result matrix c
19 22 
43 50 
continue(y/n)? y
Enter value of rows and cols for both matrix
enter no of rows 3
enter no of columns 3
Matrix a
element 1
element 2
element 3
element 4
element 5
element 6
element 7
element 8
element 9
Matrix b
element 11
element 12
element 13
element 14
element 15
element 16
element 17
element 18
element 19
matrix a
1 2 3 
4 5 6 
7 8 9 
matrix b
11 12 13 
14 15 16 
17 18 19 
result matrix c
90 96 102 
216 231 246 
342 366 390 
continue(y/n)? n
>>> 
============== RESTART: D:\python savefile\practicals\prctl9.py ==============
Enter Expression: (a+b)
Expression is well bracketed
continue (y/n)?y
Enter Expression: (a-b+a(a*b)
Expression is not well bracketed
continue (y/n)?n
>>> 
============= RESTART: D:\python savefile\practicals\prctl10.py =============
Enter size of list: 4
Enter No of rotations: 3
Element: 1
Element: 2
Element: 3
Element: 4
your list:  ['1', '2', '3', '4']
list after rotation 
 ['4', '1', '2', '3']
Continue (y/n)?y
Enter size of list: 5
Enter No of rotations: a
Element: c
Element: d
Element: e
Element: f
Element: g
your list:  ['c', 'd', 'e', 'f', 'g']
Traceback (most recent call last):
  File "D:\python savefile\practicals\prctl10.py", line 15, in <module>
    print("list after rotation \n",rotatelist(lst,int(k)))
ValueError: invalid literal for int() with base 10: 'a'
>>> 
============= RESTART: D:\python savefile\practicals\prctl11.py =============
Enter size of list: 4
Element: 1
Element: 3
Element: 1
Element: 0
list:  [1, 3, 1, 0]
False
Continue (y/n)?y
Enter size of list: 5
Element: 1
Element: 2
Element: 3
Element: 4
Element: 5
list:  [1, 2, 3, 4, 5]
True
Continue (y/n)?n
>>> 
============= RESTART: D:\python savefile\practicals\prctl12.py =============
Enter String: computers
dictoinary 
 {'c': ['computers']}
Continue (y/n)?y
Enter String: hello world and welcome to python
dictoinary 
 {'h': ['hello'], 'w': ['world', 'welcome'], 'a': ['and'], 't': ['to'], 'p': ['python']}
Continue (y/n)?n
>>> 
============= RESTART: D:\python savefile\practicals\prctl13.py =============
Select appropriate option
1. Search for specific item
2. Find the costliest Item
3. Display All items and total cost
Enter choice1
Enter Item name to be searched: pen
Do you wish to continue (y/n)?y
Select appropriate option
1. Search for specific item
2. Find the costliest Item
3. Display All items and total cost
Enter choice
============= RESTART: D:\python savefile\practicals\prctl13.py =============
Select appropriate option
1. Search for specific item
2. Find the costliest Item
3. Display All items and total cost
Enter choice1
Enter Item name to be searched: pen
item not found
item not found
item not found
Do you wish to continue (y/n)?
============= RESTART: D:\python savefile\practicals\prctl13.py =============
Select appropriate option
1. Search for specific item
2. Find the costliest Item
3. Display All items and total cost
Enter choice1
Enter Item name to be searched: pen
item not found
item not found
item not found
Do you wish to continue (y/n)?y
Select appropriate option
1. Search for specific item
2. Find the costliest Item
3. Display All items and total cost
Enter choice2
Costliest Item is : -  30500
ID:  3 || Name:  gpu || Price:  30500 || Quantity:  90
Do you wish to continue (y/n)?n
>>> 
============= RESTART: D:\python savefile\practicals\prctl14.py =============
Enter Directory: D:\python savefile\practicals
Largest File is:  calc.py
Continue (y/n)?y
Enter Directory: D:\python savefile
Traceback (most recent call last):
  File "D:\python savefile\practicals\prctl14.py", line 13, in <module>
    fname[os.stat(i).st_size]=i
FileNotFoundError: [WinError 2] The system cannot find the file specified: '08-02.py'
>>> 
============= RESTART: D:\python savefile\practicals\prctl15.py =============
Enter the Directory: D:\python savefile
08-02.py
09-02.py
16.py
demo.pdf
allpracticals.py
ex1.py
ex2.py
ex3.py
ex4.py
ex5.py
ex6.py
ex7.py
gui
hello.txt
item.dat
march03.py
New folder
practicals
practicals.rar
prbstmt3.py
prbstmt4.py
prbstmt5.py
prctl10.py
prctl11.py
prctl12.py
prctl13.py
prctl14.py
prctl15.py
prctl9.py
prgm1.py
python
Python Problem Statement.docx
savefile
savefile.zip
stmt1.py
stmt10.py
stmt12.py
stmt13.py
stmt6.py
stmt7.py
stmt8.py
stmt9.py
check for another directory (y/n)?y
Enter the Directory: D:\
$RECYCLE.BIN
135_PGB_ITM_SmitNikam
135_PGB_ITM_SmitNikam - Copy
22_dotnet
39-Parth Patel.docx
39-Parth Patel.pdf
43_C#
45_Q41.docx
47_Rushabh_Shah_OpenCV_Projects (1).docx
48_Arbaaz_Shaikh.docx
48_OpenCV_Project_1-10.docx
58_Chetan-Vandha_MCA_SEM 4.pdf.docx
58_chetan_vandha.docx
58_Chetan_Vandha_MCA_SemIV_OpenCV.docx
Alumini_PPT.pptx
AndroidMenu
asp.net
babu.jfif
BlueToothExplicit
Business_Intelligence_-_A_Managerial_App.pdf
C++ final-2.docx
cache
caching multiple responses for a single webform.docx
calculator
Checkbox
circle.jfif
code_cache
CompetitorsBrands-Q2.xlsx
DAA_paper.docx
databases
dg.jpg
dg1.jpg
dg2.png
digi.png
digi1.png
digit-reco-1-in (1).jpg
digit-reco-1-in.jpg
digital-marketing1.jpg
digits.jpg
digits1.jpg
digits1.png
DIP3E_CH03_Original_Images.zip
download.jfif
download.jpg
Downloads
drive-download-20200218T035911Z-001.zip
eula.1028.txt
eula.1031.txt
eula.1033.txt
eula.1036.txt
eula.1040.txt
eula.1041.txt
eula.1042.txt
eula.2052.txt
eula.3082.txt
ex14.6pg734crashingtime cost trade off.xlsx
eye.jfif
eye2.jfif
fds
ggggerggg.txt
Git-2.25.0-64-bit.exe
GitHubDesktopSetup.exe
global_network (1).jpg
global_network.jpg
globdata.ini
GROUP 10.pptx
hardware-wires-technology-wallpaper-preview.jpg
imageCaptioning (1).pdf
imageCaptioning.pdf
ImageProcessingandCV_48
images (1).jfif
images.jfif
img2.jpg
IMG_20200312_140926__01.jpg
IMG_20200312_144211__01.jpg
Implicit
install.exe
install.ini
install.res.1028.dll
install.res.1031.dll
install.res.1033.dll
install.res.1036.dll
install.res.1040.dll
install.res.1041.dll
install.res.1042.dll
install.res.2052.dll
install.res.3082.dll
junit_48
kartik
khushnuma
lena.jfif
lenaTest2.jpg
main_image.jpg
market10.jpg
market2.jpg
market6.jpg
marketing-strategy.jpg
mca
messi.jfif
messi1.jpg
messi1_f.jpg
messiface.jfif
mk_datavis_022217.png
MONITOR CLASS.pptx
MyApplication
MyApplication2
MyApplication3
mysql-connector-net-8.0.19 (1).msi
mysql-connector-net-8.0.19 (2).msi
mysql-connector-net-8.0.19 (3).msi
mysql-connector-net-8.0.19.msi
mysql-installer-web-community-8.0.18.0.msi
mysql-installer-web-community-8.0.19.0.msi
MySql.Data.zip
nemo.jpg
New folder
Nithya
OpenCV48
OpenCv_Project.docx
parth
parth ka part.pptx
photo-1542382257-80dedb725088.jpg
photo-1558494949-ef010cbdcc31.jpg
pracs-4-static analysis.docx
pranav
ProFormaCashFlow-Q3.xlsx
Project No9.docx
python savefile
Radio
Redirect
Registration links.docx
ruchira
Sample - Superstore.xls
sce.jpg
scene.jfif
scene_left.jpg
scene_right.jpg
SE 43
SFB.ppt.pptx
SFB.pptx
shru.jpg
shweta37
SoftwareTesting_48
StudentInformationForm.rar
sudoku.jfif
System Volume Information
T0001-10.1080_21642583.2019.1647576.csv
TableauDesktop-32bit-10-2-24.exe
template.jpg
Unit_3_Analysis_of_Sorting_Searching_Algorithms.ppt
Unit_4_String_Matching_Algorithms.pptx
unnamed.jpg
unnamed.png
UWT4
vcredist.bmp
VC_RED.cab
VC_RED.MSI
VSCodeUserSetup-x64-1.41.1.exe
VSCodeUserSetup-x64-1.42.1.exe
WC PPT
Wealth Manangement   Assignment_Anbarasu_reddy.xlsx
win 7
win 7.rar
xampp
xampp-win32-5.6.35-0-VC11-installer.exe
xampp-windows-x64-7.4.2-0-VC15-installer.exe
Xampp5.6.35
~$oject No8.docx
check for another directory (y/n)?n
>>> 
============= RESTART: D:\python savefile\practicals\prctl16.py =============
Enter value for num1: 21
Enter value for num2: -28
Enter Operator: +
Traceback (most recent call last):
  File "D:\python savefile\practicals\prctl16.py", line 54, in <module>
    funop(x,y,op)
  File "D:\python savefile\practicals\prctl16.py", line 19, in funop
    chkres(d1,d2,d3,d4,d5)
  File "D:\python savefile\practicals\prctl16.py", line 40, in chkres
    raise Exception("Negative result Exception")
Exception: Negative result Exception
>>> 
============== RESTART: D:\python savefile\practicals\regex.py ==============
Enter Your String: HElloworld@123
Valid Password
continue (y/n)?y
Enter Your String: hello
Password length min=6 and max = 16 characters
continue (y/n)?y
Enter Your String: Hello123
Passsword must contain 1 uppercase,1 lowecase alphabets,1 numeric and 1 special character
continue (y/n)?y
Enter Your String: Hello1234@1
Valid Password
continue (y/n)?n
>>> 
============= RESTART: D:\python savefile\practicals\rainbow.py =============
Enter Character: V
voilet
Continue(y/n)? y
Enter Character: I
indigo
Continue(y/n)? y
Enter Character: B
blue
Continue(y/n)? y
Enter Character: G
green
Continue(y/n)? y
Enter Character: Y
yellow
Continue(y/n)? y
Enter Character: O
orange
Continue(y/n)? y
Enter Character: R
red
Continue(y/n)? Y
Enter Character: a
Traceback (most recent call last):
  File "D:\python savefile\practicals\rainbow.py", line 22, in <module>
    color1.displaycolor(str1)
  File "D:\python savefile\practicals\rainbow.py", line 14, in displaycolor
    raise Exception("Color not found")
Exception: Color not found
>>> 
=============== RESTART: D:\python savefile\practicals\gui1.py ===============

=============== RESTART: D:\python savefile\practicals\abs1.py ===============
Traceback (most recent call last):
  File "D:\python savefile\practicals\abs1.py", line 1, in <module>
    from ABC import *
ModuleNotFoundError: No module named 'ABC'
>>> 
=============== RESTART: D:\python savefile\practicals\abs1.py ===============
Traceback (most recent call last):
  File "D:\python savefile\practicals\abs1.py", line 3, in <module>
    class shape(abc):
NameError: name 'abc' is not defined
>>> 
=============== RESTART: D:\python savefile\practicals\abs1.py ===============
Select option to search from below 

1. rectangle 
2. triangle
3. circle
4. rhombus
5. show all
Traceback (most recent call last):
  File "D:\python savefile\practicals\abs1.py", line 68, in <module>
    d2=traingle()
NameError: name 'traingle' is not defined
>>> 
=============== RESTART: D:\python savefile\practicals\abs1.py ===============
Select option to search from below 

1. rectangle 
2. triangle
3. circle
4. rhombus
5. show all
Enter option1
Enter length of rectangle: 12
Enter breadth of rectangle: 15
area of rectangle:  180
perimeter: 54
continue (y/n)?y
Select option to search from below 

1. rectangle 
2. triangle
3. circle
4. rhombus
5. show all
Enter option5
please select suitable option
continue (y/n)?n
>>> 
=============== RESTART: D:\python savefile\practicals\abs1.py ===============
Select option to search from below 

1. rectangle 
2. triangle
3. circle
4. rhombus
5. show all
Enter option5
Enter length of rectangle: 12
Enter breadth of rectangle: 15
Enter base of triangle: 12
Enter height of traingle: 5
Enter radius of circle: 45
Enter d1 of rhombus: 4
Enter d2 of rhombus: 5
Enter side of rhombus: 3
area of rectangle:  180
perimeter: 54
area of triangle:  30.0
Enter Length for third side32
perimeter: 34
area of circle:  6358.500000000001
perimeter: 282.6
area of rhombus:  10.0
perimeter: 12
continue (y/n)?n
>>> 
