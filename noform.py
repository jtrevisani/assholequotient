# Script Name    : noform.py
# Author         : johnny trevisani
# Created        : 20 Dec 2016
# Last Modified  : 21 Dec 2016
# Version        : 1.0

# Modifications	: documentation for initial version



# Description	: Prompt user for ratings 

Bg = input ("BIGOTRY Rating (1-5):") 
Of = input ("OFFENSIVENESS Rating (1-5):")
Ap = input ("APPEARENCE Rating (1-5):")
E = input ("EGO Rating (1-5):")
Bl = input ("BODY LANGUAGE Rating (1-5):")
M = input ("ME MENTIONS Rating (1-5):")
Ag = input ("AGGRESSIVE Rating (1-5):")
Pa = input ("PASSIVE AGGRESIVE Rating (1-5):")
H = input ("HOSTILITY Rating (1-5):") 
S = input ("SMILE Rating (1-5):")
C = input ("CREEPY Rating (1-5):") 
P = input ("PARANOID Rating (1-5):")
B = input ("BRAG Rating (1-5):")
L = input ("LIE Rating (1-5):")
R = input ("RIGHTEOUSNESS Rating (1-5):")
Mn = input ("MANNERS Rating (1-5):")




#  Perform calculated asshole score based on the following formula
#
# A = Bg(3)+Of(2)/Ap+((Ag/Pa)*3)-M*(B+Bl-L)-(C+P)+H(2)+(-E*R)-Mn-S(.5)

A = (float(Bg)*3 + float(Of)*2) / float(Ap) + ( float(Ag) / float(Pa) * 3 ) - float(M) * ( float(B) + float(Bl) - float(L) ) - (float(C)+float(P)) + (float(H)*2) + (- float(E) * float(R) ) - float(Mn) - float(S)*.5
      





# Display the asshole factor

print('The asshole factor is {0}' . format(A)) 