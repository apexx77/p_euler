import math

def main():
    for x in range (1, 1000):
        for y in range (1, 1000):
            for z in range(1, 1000):
                if x*x == y*y + z*z:
                    print(y, z, x)
                    print('-'*50)

if __name__ == '__main__':
    main()