# Current read level test
# 0 = blank
# 1 = wall
# 2 = locker
# 3 = door
# 4 = stair

def read_level (num):
    screen = open('Levels/level' + str(num) + '.txt')
    lines = []
    for line in screen:
        for ch in line:
            if ch != '\n':
                ch = int(ch)
                lines.append(ch)
    return lines

def main ():
    num = raw_input('Which level? ')
    print read_level(num)

if __name__ == '__main__':
	main()