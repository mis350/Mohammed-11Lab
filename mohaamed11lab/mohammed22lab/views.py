from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Mohaamed11lab_view(request):
    x = HttpResponse("""<html>
                     <head> Welcome to my web page. </head>
                     <body> <p> <tt> My name is Mohammed Alajmi. And I'm 22 years old.</tt> </p>
                     <p> My Friends:</p>
                     <p> <li> Mohammed </li> 
                     <li> Ali </li>
                     <li> Saad </li> </p>
                     <p> Watch video <a href="www.youtube.com"> HER </a> </p>
                     
                     
                     
                      </body>
                     
                     
                     
                     
                     
                     
                     
                       </htmal>""")

    return x 