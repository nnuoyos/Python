from circle import ci_circle as cc
"""  def ci_circle(rad):
    return rad*2*PI """

def ci_circle(rad):
    print("둘레: ", rad*2*3.14)


def main():
    r=float(input("반지름 입력: "))
    ci_circle(r) #circle_simple2.py
    cc(r) #circle.py


main()