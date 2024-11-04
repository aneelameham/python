def reverse(mystring):
    reversed = mystring[::-1]
    return reversed


def for_reverse(mystring):
    reversed = ""
    for char in mystring:
        reversed = char + reversed
    return reversed


print(reverse("amarnath"))
print(for_reverse("amarnath"))
