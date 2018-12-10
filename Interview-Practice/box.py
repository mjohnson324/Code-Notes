# You have an image represented by a 2-D array of 1s and 0s. The 0s represent a box.
# Find the coordinates of the box
# There is only one box.
# The box and array are rectangular and can vary in size.
# sample input: [
#     [1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 0, 0, 0, 1],
#     [1, 1, 1, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1]
# ]
# sample output: { "start": (2, 3), "end": (4, 5) }

def get_box_coordinates(image):
    # Define needed variables
    start = None
    end = None
    # We must check every number
    for i, row in enumerate(image):
        for j, num in enumerate(row):
            if start is None and num == 0:
                start = (i, j)
            if num == 0:
                end = check_end(i, j, image, end)
    return { "start": start, "end": end } if start else None

def check_end(i, j, image, end=None):
    # The last 0 will be bordered by 1s in the next row and column, or
    # the edge of the image. Check these conditions.
    if end is not None:
        return end
    last_row = len(image) - 1
    last_column = len(image[0]) - 1
    next_row_num = None
    next_column_num = None
    if i != last_row:
        next_row_num = image[i + 1][j]
    if j != last_column:
        next_column_num = image[i][j + 1]
    if next_row_num == 1 and next_column_num == 1:
        end = (i, j)
    elif next_row_num == 1 and j == last_column:
        end = (i, j)
    elif i == last_row and next_column_num == 1:
        end = (i, j)
    elif i == last_row and j == last_column:
        end = (i, j)
    return end