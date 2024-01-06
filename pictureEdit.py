from typing import List


def mirror(raw: List[List[List[int]]])-> None:
    for row in raw:
        row[:] = row[::-1]
    """
    Assume raw is image data. Modifies raw by reversing all the rows
    of the data.

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 255]],
               [[199, 201, 116], [1, 9, 0], [255, 255, 255]]]
    >>> mirror(raw)
    >>> raw
    [[[255, 255, 255], [0, 0, 0], [233, 100, 115]],
     [[255, 255, 255], [1, 9, 0], [199, 201, 116]]]
    """



def grey(raw: List[List[List[int]]])-> None:
    for row in range(len(raw)):
        for pixel in range(len(raw[row])):
                total = 0
                count = 0
                for rgb in range(len(raw[row][pixel])):
                    total += raw[row][pixel][rgb]
                    count += 1
                average = total//count
                raw[row][pixel] = [average,average,average]
    """
    Assume raw is image data. Modifies raw "averaging out" each
    pixel of raw. Specifically, for each pixel it totals the RGB
    values, integer divides by three, and sets the all RGB values
    equal to this new value

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 255]],
               [[199, 201, 116], [1, 9, 0], [255, 255, 255]]]
    >>> grey(raw)
    >>> raw
    [[[149, 149, 149], [0, 0, 0], [255, 255, 255]],
     [[172, 172, 172], [3, 3, 3], [255, 255, 255]]]
    """
    


def invert(raw: List[List[List[int]]])-> None:
    for row in range(len(raw)):
        for pixel in range(len(raw[row])):
            maxx = max(raw[row][pixel])
            minn = min(raw[row][pixel])
            for rgb in range(len(raw[0][0])):
                if raw[row][pixel][rgb] == maxx:
                    raw[row][pixel][rgb] = minn
                elif raw[row][pixel][rgb] == minn:
                    raw[row][pixel][rgb] = maxx
    """
    Assume raw is image data. Modifies raw inverting each pixel.
    To invert a pixel, you swap all the max values, with all the
    minimum values. See the doc tests for examples.

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 0]],
               [[199, 201, 116], [1, 9, 0], [255, 100, 100]]]
    >>> invert(raw)
    >>> raw
    [[[100, 233, 115], [0, 0, 0], [0, 0, 255]],
     [[199, 116, 201], [1, 0, 9], [100, 255, 255]]]
    """
  


def merge(raw1: List[List[List[int]]], raw2: List[List[List[int]]])-> List[List[List[int]]]:
    max_height = max(len(raw1), len(raw2))
    raw1_width = len(raw1[0]) if raw1 else 0
    raw2_width = len(raw2[0]) if raw2 else 0
    max_width = max(raw2_width, raw1_width)
    black_pix = [255, 255, 255]
    merged = []
   
    for i in range(max_height):
        row = [[255, 255, 255] for _ in range(max_width)]
       
        for j in range(max_width):
            if i < len(raw1) and i % 2 == 0 and j < len(raw1[i]) and row[j] == [255, 255, 255]:
                row[j] = raw1[i][j]
            elif i < len(raw2) and i % 2 != 0 and j < len(raw2[i]) and row[j] == [255, 255, 255]:
                row[j] = raw2[i][j]
               
        merged.append(row)
   

    for i in range(max_height):
         for j in range(max_width):
             if merged[i][j] == black_pix:
                if i < len(raw1) and j < len(raw1[i]):
                    merged[i][j] = raw1[i][j]
                if i < len(raw2) and j < len(raw2[i]):
                    merged[i][j] = raw2[i][j]
 
    return merged

    """
    Merges raw1 and raw2 into new raw image data and returns it.
    It merges them using the following rule/procedure.
    1) The new raw image data has height equal to the max height of raw1 and raw2
    2) The new raw image data has width equal to the max width of raw1 and raw2
    3) The pixel data at cell (i,j) in the new raw image data will be (in this order):
       3.1) a black pixel [255, 255, 255], if there is no pixel data in raw1 or raw2
       at cell (i,j)
       3.2) raw1[i][j] if there is no pixel data at raw2[i][j]
       3.3) raw2[i][j] if there is no pixel data at raw1[i][j]
       3.4) raw1[i][j] if i is even
       3.5) raw2[i][j] if i is odd
    """
    """
        >>> raw1 size = [1][4]
        >>> raw2 size = [3][1]
        >>> merge size is [3][4]
        
        merge = [[[raw1[0,0], raw1[0,1], raw1[0,2], raw1[0,3], raw1[0,4]],
                 [[raw2[1,0], blackPixel, blackPixel, blackPixel, blackPixel],
                 [[raw2[2,0], blackPixel, blackPixel, blackPixel, blackPixel]]
                 
        i.e.
        raw1 = [[[233, 100, 115], [0, 0, 0], [255, 255, 0], [1,2,3]]]
        raw2 = [[[199, 201, 116]],
                [[1, 9, 0]],
                [[255, 100, 100]]]
        merge = [[[233, 100, 115], [0, 0, 0], [255, 255, 0], [1,2,3]],
                 [[1, 9, 0], [255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255]],
                 [[255, 100, 100], [255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255]]]
                 
        >>> raw1 size = [2][4]
        >>> raw2 size = [3][3]
        >>> merge size is [3][4]
        
        i.e.
        raw1 = [[[233, 100, 115], [0, 0, 0], [255, 255, 0], [1,2,3]],
                [[200, 200, 200], [1, 9, 0], [255, 100, 100], [99, 99, 0]]]
                
        raw2 = [[[199, 201, 116], [2, 3, 4], [4, 5, 5]],
                [[1, 9, 0], [5, 6, 6], [7, 7, 8]],
                [[255, 100, 100], [8, 9, 10], [11, 12, 12]]]
                
        merge = [[[233, 100, 115], [0, 0, 0], [255, 255, 0], [1,2,3]],
                 [[1, 9, 0], [5, 6, 6,], [7, 7, 8], [99, 99, 0]],
                 [[255, 100, 100], [8 ,9 ,10], [11 ,12 , 12], [255 ,255 ,255]]]
    """
  
    
    


def compress(raw: List[List[List[int]]])-> List[List[List[int]]]:
    if raw == []:
        return []
    if raw == [[], []]:
        return [[]]

    output = []
    length_raw = len(raw)
    length_raw_row = len(raw[0])
    
    
    for row in range(0, length_raw,2):
        new_row = []
        for pixel in range(0, length_raw_row, 2):
            new_pixel = [0,0,0]
           
            for rgb in range(len(raw[0][0])):
                pixel_count = 1
                new_pixel[rgb] += raw[row][pixel][rgb]
                if (pixel + 1) < len(raw[0]):
                    new_pixel[rgb] += raw[row][pixel + 1][rgb]
                    pixel_count += 1
                if (row + 1) < len(raw):
                    new_pixel[rgb] += raw[row + 1][pixel][rgb]
                    pixel_count += 1
                    if (pixel + 1) < len(raw[0]):
                        new_pixel[rgb] += raw[row + 1][pixel + 1][rgb]
                        pixel_count += 1
                new_pixel[rgb] = new_pixel[rgb]//pixel_count

            new_row.append(new_pixel)
        output.append(new_row)
    return output
    """
    Compresses raw by going through the pixels and combining a pixel with
    the ones directly to the right, below and diagonally to the lower right.
    For each RGB values it takes the average of these four pixels using integer
    division. If is is a pixel on the "edge" of the image, it only takes the
    relevant pixels to average across. See the second doctest for an example of
    this.

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 0], [3, 6, 7]],
               [[199, 201, 116], [1, 9, 0], [255, 100, 100], [99, 99, 0]],
               [[200, 200, 200], [1, 9, 0], [255, 100, 100], [99, 99, 0]],
               [[50, 100, 150], [1, 9, 0], [211, 5, 22], [199, 0, 10]]]
    >>> compress(raw)
    >>> compressed_raw
    [[[108, 77, 57], [153, 115, 26]],
     [[63, 79, 87], [191, 51, 33]]]

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 0]],
               [[199, 201, 116], [1, 9, 0], [255, 100, 100]],
               [[123, 233, 151], [111, 99, 10], [0, 1, 1]]]
    >>> compress(raw)
    >>> compressed_raw
    [[[108, 77, 57], [255, 177, 50]],
     [[117, 166, 80], [0, 1, 1]]]
    """
 


"""
**********************************************************

Do not worry about the code below. However, if you wish,
you can us it to read in images, modify the data, and save
new images.

**********************************************************
"""

def get_raw_image(name: str)-> List[List[List[int]]]:
    
    image = Image.open(name)
    num_rows = image.height
    num_columns = image.width
    pixels = image.getdata()
    new_data = []
    
    for i in range(num_rows):
        new_row = []
        for j in range(num_columns):
            new_pixel = list(pixels[i*num_columns + j])
            new_row.append(new_pixel)
        new_data.append(new_row)

    image.close()
    return new_data


def image_from_raw(raw: List[List[List[int]]], name: str)->None:
    image = Image.new("RGB", (len(raw[0]),len(raw)))
    pixels = []
    for row in raw:
        for pixel in row:
            pixels.append(tuple(pixel))
    image.putdata(pixels)
    image.save(name)
                      
                      




