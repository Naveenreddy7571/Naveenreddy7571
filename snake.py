import os
import random

def generate_snake():
    snake_length = 25
    snake_color = "#4CAF50"

    days = [random.randint(0, 1) for _ in range(snake_length)]
    days_str = "".join(map(str, days))

    snake_svg = f"""
    <svg width="495" height="195" viewBox="0 0 495 195" xmlns="http://www.w3.org/2000/svg">
      <g id="grid" stroke="{snake_color}" stroke-width="2">
        <rect x="0" y="0" width="495" height="195" fill="#212121"/>
        {days_str}
      </g>
    </svg>
    """

    with open("snake.svg", "w") as file:
        file.write(snake_svg)

if __name__ == "__main__":
    generate_snake()
