def main(x, y, filename):
    f = open(filename, 'w')

    f.write('P3 {} {} 255 '.format(x, y))

    i = 0
    while i < x * y:
        f.write('{} '.format(int(float(i / (x*y)) * 255)))
        f.write('0 ')
        f.write('0 ')#.format(255 - int(float(i / (x*y)) * 255)))
        i += 1

    f.close()

main(500, 500, 'pic.ppm')
