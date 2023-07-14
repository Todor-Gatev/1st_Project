from pyfiglet import Figlet, FigletFont

fig_test = Figlet(font='big')
print(fig_test.renderText('Hello World'))

fig_test = Figlet(font='isometric1')
print(fig_test.renderText('Hello World'))

print(FigletFont.getFonts())

