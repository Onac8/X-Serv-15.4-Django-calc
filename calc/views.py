from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseBadRequest

def sum(request, op1, op, op2):
    resultado = int(op1) + int(op2)
    htmlAnswer = "<p> The operation: " + op1 + " " + op \
                + " " + op2 + " = " + str(resultado) + "</p>"
    return HttpResponse(htmlAnswer)

def mul(request, op1, op, op2):
    resultado = int(op1) * int(op2)
    htmlAnswer = "<p> The operation: " + op1 + " " + op \
                + " " + op2 + " = " + str(resultado) + "</p>"
    return HttpResponse(htmlAnswer)

def div(request, op1, op, op2):
    try:
        resultado = int(op1) / int(op2)
        htmlAnswer = "<p> The operation: " + op1 + " " + op \
                    + " " + op2 + " = " + str(resultado) + "</p>"
        return HttpResponse(htmlAnswer)
    except ZeroDivisionError:
        htmlAnswer = "<p> You tried to divide by zero... </p>"
        return HttpResponseBadRequest(htmlAnswer)

def sub(request, op1, operacion, op2):
        resultado = int(op1) - int(op2)
        htmlAnswer = "<p> El resultado--> " + op1 + " " + op \
                    + " " + op2 + " = " + str(resultado) + "</p>"
        return HttpResponse(htmlAnswer)
