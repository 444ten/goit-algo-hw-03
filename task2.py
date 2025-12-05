import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Koch Snowflake Fractal (click fo exit)")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.left(-120)

    window.exitonclick()

def main():
    try:
        user_input = input("Enter recursion level (recommended 0-5): ")
        order = int(user_input)
        
        if order < 0:
            print("Level cannot be negative. Setting to 0.")
            order = 0
            
        print(f"Drawing Koch Snowflake with recursion level {order}...")
        draw_snowflake(order)
        
    except ValueError:
        print("Invalid input! Please enter an integer number.")

if __name__ == "__main__":
    main()
    