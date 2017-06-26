fact = 1.0/255.0
fact = 1
gradient = {'red':  [(0.0,   10*fact,  22*fact),
                   (0.25, 20*fact, 133*fact),
                   (0.5,  30*fact, 191*fact),
                   (0.75, 20*fact, 151*fact),
                   (1.0,   10*fact,  25*fact)],
         'green': [(0.0,   20*fact,  65*fact),
                   (0.25, 30*fact, 182*fact),
                   (0.5,  40*fact, 217*fact),
                   (0.75, 30*fact, 203*fact),
                   (1.0,   20*fact,  88*fact)],
         'blue':  [(0.0,  30*fact, 153*fact),
                   (0.25, 40*fact, 222*fact),
                   (0.5,  40*fact, 214*fact),
                   (0.75, 20*fact, 143*fact),
                   (1.0,   10*fact,  40*fact)]} 

for i in range(5):
	red = gradient['red'][i][1]
	green = gradient['green'][i][1]
	blue = gradient['blue'][i][1]
	print(red, green, blue, '\x1b[{};{};{}m \x1b[0m'.format( red , green, blue ))

