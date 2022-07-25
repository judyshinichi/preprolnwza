""" Tascha Kod Hod """
def main():
    """ Tascha Kod Good """ #guy liar mak mak Tascha code mai pen!
    grade = float(input())
    answer = 4.00 - grade
    if grade < 1.00:
        print("I'm so sad.")
    elif grade >= 2.00:
        print("I'm so happy.")
    elif 1.00 <= grade < 2.00:
        print("%.2f" %(answer))
main()
