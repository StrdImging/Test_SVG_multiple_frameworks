viewBox = "viewBox=\"0 0 100 100\" "
svgTag = ""

contents = []
f = open("../assets/wl1.svg", "r")
if f.mode == 'r':
    contents = f.readlines()
    svgTag = contents[1]
# endif
f.close()

# TAKE USER INPUTS
x = input("viewBox x:")
y = input("viewBox y:")
x_w = input("viewBox x_w:")
y_h = input("viewBox y_h:")
viewBox = " viewBox=\"" + x + " " + y + " " + x_w + " " + y_h + "\">"

svgTag = svgTag[:len(svgTag)-2] + viewBox
print(svgTag)

contents[1] = svgTag

with open("../assets/cropped/"+x + y +x_w + y_h+".svg", "w") as file:
    for content in contents:
        file.write(content)
    #next
