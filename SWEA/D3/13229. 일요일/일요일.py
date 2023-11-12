# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def solution():
    # Use a breakpoint in the code line below to debug your script.
    tc = int(input())
    days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    for t in range(1,tc+1):
        today = input()
        idx = days.index(today)
        if today=='SUN':
            answer = 7
        else:
            answer = 6-idx

        print(f'#{t} {answer}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
