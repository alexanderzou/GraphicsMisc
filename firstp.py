def main(x, y, filename):
    f = open(filename, 'w')

    f.write('P3 {} {} 255 '.format(x, y))

    i = 0
    while i < x * y:
        r = 0
        g = 0
        b = 0
        f.write('0 ')#.format(int(float(i / (x*y)) * 255)))
        f.write('0 ')
        f.write('{} '.format(255 - int(float(i) / float(x*y)) * 255))
        i += 1

    f.close()

main(500, 5, 'pic.ppm')
