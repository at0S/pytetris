## largets common denominator

def lcd(a, b):
    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller+1):
        if((a % i == 0) and (b % i == 0)):
            gcd = i
    return gcd

def main():
    print("Outputs common denominator for a number of screen resolutions")
    print("800x600: ", lcd(800, 600))
    print("1024x768: ", lcd(1024, 768))  
    print("1920x1080: ", lcd(1920, 1080))
    print("3840x2160: ", lcd(3840, 2160))

if __name__ == "__main__":
    main()
