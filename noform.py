#
# This program gathers data and calculates an asshole score
#
#

#
# Gather input
#
Bg = input ("BIGOTRY Rating:") 
Of = input ("OFFENSIVENESS Rating:")
Ap = input ("APPEARENCE Rating:")
E = input ("EGO Rating:")
Bl = input ("BODY LANGUAGE Rating:")
M = input ("ME MENTIONS Rating:")
Ag = input ("AGGRESSIVE Rating:")
Pa = input ("PASSIVE AGGRESIVE Rating:")
H = input ("HOSTILITY Rating:") 
S = input ("SMILE Rating:")
C = input ("CREEPY Rating:") 
P = input ("PARANOID Rating:")
B = input ("BRAG Rating:")
L = input ("LIE Rating:")
R = input ("RIGHTEOUSNESS Rating:")
Mn = input ("MANNERS Rating:")


#
# Add calculate the 
#
A = (float(Bg)*3 + float(Of)*2) / float(Ap) + ( float(Ag) / float(Pa) * 3 ) - float(M) * ( float(B) + float(Bl) - float(L) ) - (float(C)+float(P)) + (float(H)*2) + (- float(E) * float(R) ) - float(Mn) - float(S)*.5
#       





# Display the sum

print('The asshole factor is {0}' . format(A)) 