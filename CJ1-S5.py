import math

def main():
    x = 0.0
    x_goal = 2 * math.pi

    step_size = x_goal / 999 
    
    for i in range(1000):
        temp = x + i * step_size
        temp2 = math.sin(temp)
        print(f'x: {temp} sin(x) = {temp2}')


if __name__ == "__main__":
    main()