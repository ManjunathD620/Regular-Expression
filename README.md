# Regular-Expression
An implementation of regular expressions for Finite Automata in Python . It will generate String for the given Regular Expression | Regular Expression in FAFL or TOC

**1.Regular Exprssion GUi :**

![Screenshot (23)](https://user-images.githubusercontent.com/82793670/148493187-927c835e-b8bc-47b4-9302-cccf5ad5a79d.png)


**2.How to give Input to Regular Expression Program :**

1. If you have simple RE or without * Closure or + Closure :--  i.e, L={a|a belongs to a} or L={a+b}<br>
  ----> Input Format :- a+b,a,b,bcc,etc..
  
2. If you Have * Operation in RE i.e, L= (w|w belongs to {a,b}) ,Re=(a+b)^*, <br>
  ----> Input Format :- use this symbol "^" to add * Operation <br>
     &ensp;&ensp;&ensp;&ensp;Ex:(a+b)^*,(a+b+xw)^* ,(anz)^*(b)^* or (a+b)^*055(8+9)^*56  etc..
  
3. If you Have * Operation within the same block i.e, L= (w*1b*| w belongs to {a}) then, <br>
  ----> Input Format :- Don't use this symbol "^"<br>
  &ensp;&ensp;&ensp;&ensp;Ex:(a*1b*) , Other Ex:- (0*+10*)
  
**3.Output :**
<br>
![Screenshot (22)](https://user-images.githubusercontent.com/82793670/148495048-59beabe4-0b24-40ce-97a6-44a5178bef95.png)
