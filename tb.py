import wget
import glob
from fpdf import FPDF
import os
#1
x = 408
y = '01. Edexcel AS and A level Mathematics Pure Mathematics Year 1 ActiveBook.pdf'

for i in range(1,x+1):
    url = 'https://resources.pearsonactivelearn.com/r00/r0066/r006623/r00662374/current/OPS/images/Pure_Maths_1-%s.jpg' % ('{0:0>3}'.format(i))
    wget.download(url)
    print ('%s pages downloaded' % (i))


imagelist = glob.glob('*.jpg')

pdf = FPDF()

for i in imagelist:
    pdf.add_page()
    pdf.image(i,x=0,y=0, w = 209, h = 300)
pdf.output(y, "F")

direct = os.getcwd()

for i in glob.iglob(os.path.join(direct, '*.jpg')):
    os.remove(i)

print (' Finished downloading %s' % (y))

#2
x = 240
f = '02. Edexcel AS and A level Mathematics Statistics and Mechanics Year 1 ActiveBook.pdf'

for i in range(1,x+1):
    url = 'https://resources.pearsonactivelearn.com/r00/r0067/r006740/r00674039/current/OPS/stats_and_mech_1_combined-%s.jpg' % ('{0:0>3}'.format(i))
    wget.download(url)
    print ('%s pages downloaded' % (i))


imagelist = glob.glob('*.jpg')

pdf = FPDF()

for i in imagelist:
    pdf.add_page()
    pdf.image(i,x=0,y=0, w = 209, h = 300)
pdf.output(f, "F")

direct = os.getcwd()

for i in glob.iglob(os.path.join(direct, '*.jpg')):
    os.remove(i)

print (' Finished downloading %s' % (y))

#3
j = 408
k = '03. Edexcel A level Mathematics Pure Mathematics Year 2 ActiveBook'

for i in range(1,j+1):
    url = 'https://resources.pearsonactivelearn.com/r00/r0068/r006800/r00680025/current/OPS/pure_maths_2-%s.jpg' % ('{0:0>3}'.format(i))
    wget.download(url)
    print ('%s pages downloaded' % (i))


imagelist = glob.glob('*.jpg')

pdf = FPDF()

for i in imagelist:
    pdf.add_page()
    pdf.image(i,x=0,y=0, w = 209, h = 300)
pdf.output(k, "F")

direct = os.getcwd()

for i in glob.iglob(os.path.join(direct, '*.jpg')):
    os.remove(i)

print (' Finished downloading %s' % (y))

#4
h = 216
b = '04. Edexcel A level Mathematics Statistics and Mechanics Year 2 ActiveBook.pdf'

for i in range(1,h+1):
    url = 'https://resources.pearsonactivelearn.com/r00/r0070/r007037/r00703733/current/OPS/SM2-%s.jpg' % ('{0:0>3}'.format(i))
    wget.download(url)
    print ('%s pages downloaded' % (i))


imagelist = glob.glob('*.jpg')

pdf = FPDF()

for i in imagelist:
    pdf.add_page()
    pdf.image(i,x=0,y=0, w = 209, h = 300)
pdf.output(b, "F")

direct = os.getcwd()

for i in glob.iglob(os.path.join(direct, '*.jpg')):
    os.remove(i)

print (' Finished downloading %s' % (y))

#5
q = 256
w = '05. Edexcel AS and A level Further Mathematics Core Pure Mathematics Book 1 ActiveBook'

for i in range(1,q+1):
    url = 'https://resources.pearsonactivelearn.com/r00/r0070/r007037/r00703734/current/OPS/CP1%s.jpg' % ('{0:0>3}'.format(i))
    wget.download(url)
    print ('%s pages downloaded' % (i))


imagelist = glob.glob('*.jpg')

pdf = FPDF()

for i in imagelist:
    pdf.add_page()
    pdf.image(i,x=0,y=0, w = 209, h = 300)
pdf.output(w, "F")

direct = os.getcwd()

for i in glob.iglob(os.path.join(direct, '*.jpg')):
    os.remove(i)

print (' Finished downloading %s' % (y))

#6
z = 408
a = '07. Edexcel AS and A level Further Mathematics Further Mechanics 1 ActiveBook.pdf'

for i in range(1,z+1):
    url = 'https://resources.pearsonactivelearn.com/r00/r0070/r007037/r00703736/current/OPS/FM1-%s.jpg' % ('{0:0>3}'.format(i))
    wget.download(url)
    print ('%s pages downloaded' % (i))


imagelist = glob.glob('*.jpg')

pdf = FPDF()

for i in imagelist:
    pdf.add_page()
    pdf.image(i,x=0,y=0, w = 209, h = 300)
pdf.output(a, "F")

direct = os.getcwd()

for i in glob.iglob(os.path.join(direct, '*.jpg')):
    os.remove(i)

print (' Finished downloading %s' % (y))

#7
t = 222
d = '06. Edexcel AS and A level Further Mathematics Further Statistics 1 ActiveBook.pdf'

for i in range(1,t+1):
    url = 'https://resources.pearsonactivelearn.com/r00/r0070/r007037/r00703737/current/OPS/FS1%s.jpg' % ('{0:0>3}'.format(i))
    wget.download(url)
    print ('%s pages downloaded' % (i))


imagelist = glob.glob('*.jpg')

pdf = FPDF()

for i in imagelist:
    pdf.add_page()
    pdf.image(i,x=0,y=0, w = 209, h = 300)
pdf.output(d, "F")

direct = os.getcwd()

for i in glob.iglob(os.path.join(direct, '*.jpg')):
    os.remove(i)

print (' Finished downloading %s' % (y))