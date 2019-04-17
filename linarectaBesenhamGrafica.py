from OpenGL.GL import * #GL, gl
from OpenGL.GLU import * #GLUT, glut
from OpenGL.GLUT import *

def display():
	print("aqui estoy display")
	glClear(GL_COLOR_BUFFER_BIT)



	glColor3f(1,0,0)
	glBegin(GL_POINTS)#dibujo puntos, punto a punto

	glColor3f(0,0,0)
	for i in range(-250,250+1):
		glVertex2i(0,i)
		glVertex2i(i,0)
	#######################################
	
	Xi, Yi = 1,1
	Xf, Yf = 1,100

	dx=Xf-Xi
	dy=Yf-Yi

	x,y = Xi, Yi


	if dx >= dy:

		while x <= Xf:
				glVertex2i(x,y)
				if 2*x*dy+2*dy-2*y*dx+2*Yi*dx-2*Xi*dy-dx >= 0:
					y += 1
				x += 1
	else:
		while y <= Yf:
				glVertex2i(x,y)
				if 2*y*dx+2*dx-2*x*dy+2*Xi*dy-2*Yi*dx-dy >= 0:
					x += 1
				y += 1
	#######################################
	
	glEnd()

	glFlush()
	
def reshape(winW,winH):
	print("aqui hay un reshape",winW,winH)
	glViewport(0,0,winW,winH)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-250,250,-250,250)

	#################################


glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(100,100)
glutInitWindowSize(500,500)
glutCreateWindow(b'b0225')
glClearColor(1,1,1,0) #red, green, blue, alpha
glutDisplayFunc(display) #Evento display
glutReshapeFunc(reshape)
glutMainLoop()