import os

import PyPDF2 as pdf

#file = open("C:\s1.pdf", "rb")
file2 = "C:\\wamp64\\www\\projet_big_data_team2\\file\\morenam.pdf"
pd = pdf.PdfFileReader(file2)
f = []
text = " "
N = pd.getNumPages()
for i in range(1, N):
    f.append(pd.getPage(i))
    text = text + f[i-1].extractText()
#print(text)
print(pd.getPage(pd.getNumPages()-1).extractText())
# if not os.path.isfile('monpdf.txt'):
#         z =open('monpdf.txt','w')
#         z.close()
#
# Fichier = open('monpdf.txt', 'w')
# Fichier.write(text)
# Fichier.close()

# print(len(file2))
#
# N = pd.getNumPages()
# x = pd.getPage(N-1)
# print(x.extractText())
# print(pd.getNumPages())
# f = []
# N = pd.getNumPages()
# for i in range(1, N):
#     f.append(pd.getPage(i))
#     print(f[i-1].extractText())
# for i in len(f):
#     text = text + f[i].extractText()
#
# print(text)

# def nbpagespdf(fichierpdf):
#     """retourne le nombre de pages du fichier pdf"""
#     with open(fichierpdf, "rb") as f:
#         return pdf.PdfFileReader(f).getNumPages()
#
#
# print(nbpagespdf(file2))

