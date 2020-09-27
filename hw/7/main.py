import calc_processor as calc
from figure import triangle
from figure import rectangle
from figure import circle

if __name__ == "__main__":
    proc = calc.Processor({
        circle.Circle().get_id(): circle.Circle(),
        rectangle.Rectangle().get_id(): rectangle.Rectangle(),
        triangle.Triangle().get_id(): triangle.Triangle()
    })
    proc.execute()
