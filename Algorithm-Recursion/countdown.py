def countdown(i):
    print(i)
    if i < 1:
        return
    else:
        countdown(i - 1)


def countdown_formal(i):
    while i >= 0:
        print(i)
        i -= 1


countdown(10)
countdown_formal(10)
