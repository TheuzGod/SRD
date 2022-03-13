from random import randint
repeat_rolling = True
while repeat_rolling:
    print("Você rolou o seguinte número usando os dados :",randint(-200,200))
    print("Deseja jogar os dados novamente?")
    repeat_rolling = ("s" or "sim") in input().lower()
    