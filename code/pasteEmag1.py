#program de formatare titlu tabel pt nei.ro | emag -> pune pe nei
import pyperclip as copy
listap = [] # principala
listas = []


inp = input("START - Copy the description on emag...")

content_raw = copy.paste()


#bold <p><span style="font-weight: 700; color: rgb(34, 34, 34); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; text-transform: uppercase;"><br></span><span style="font-weight: 700; color: rgb(34, 34, 34); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; text-transform: uppercase;">DETALII FRIGIDER</span></p>
#tabel <table class="table table-bordered"><tbody><tr><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(136, 136, 136); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">Volum net frigider</span><br></span></td><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(34, 34, 34); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">175 l</span><br></span></td></tr><tr><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(136, 136, 136); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">Sistem dezghetare frigider</span><br></span></td><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(34, 34, 34); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">Manual</span><br></span></td></tr><tr><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(136, 136, 136); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">Numar rafturi frigider</span><br></span></td><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(34, 34, 34); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">3</span><br></span></td></tr><tr><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(136, 136, 136); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">Numar rafturi usi</span><br></span></td><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(34, 34, 34); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">4</span><br></span></td></tr><tr><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(136, 136, 136); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">Material rafturi</span><br></span></td><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(34, 34, 34); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">Sticla termorezistenta</span><br></span></td></tr><tr><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(136, 136, 136); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">Dozator apa</span><br></span></td><td><span style="color: rgb(34, 34, 34); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line; background-color: rgb(255, 255, 255);">Nu</span><br></td></tr></tbody></table>

content = "%r"%content_raw

lim1 = 0
for i in range(len(content)): # while end
    if content[i:i+8] == r"\r\n\r\n": # titlu bold

        #inchide lista secundara daca e deschisa
        if len(listas) > 0:
            listap.append(listas)
            listas = []
        
        lim2 = i
        listap.append(content[lim1:lim2])

        # urmeaza imediat tabel
        lim1 = i+8
        
    if content[i:i+2] == r"\t": # casuta impara
        lim2 = i
        listas.append(content[lim1:lim2]) # impara in lista sec

        lim1 = i+2 ; j=i+2
        while True:
            if (content[j:j+4] == r'\r\n') or (j+4 == len(content)):
                lim2= j
                break
            j=j+1
        listas.append(content[lim1:lim2])
        lim1 = j+4
listap.append(listas) ; listas = []

#format tabel
titlu_in = '<p><span style="font-weight: 700; color: rgb(34, 34, 34); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; text-transform: uppercase;"><br></span><span style="font-weight: 700; color: rgb(34, 34, 34); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; text-transform: uppercase;">'
titlu_out = '</span></p>'
tabel_in = '<table class="table table-bordered"><tbody>'
tabel_out = '</tbody></table>'
tr_in = '<tr>'
tr_out = '</tr>'
td_in = '<td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(136, 136, 136); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">'
td_out = '</span><br></span></td>'
content_out = '' #html out

# fac tabel
for i in listap:
    if type(i) == str:
        content_out += titlu_in + i + titlu_out + '\n' 
        
    elif type(i) == list: # lista = tabel
        content_out += tabel_in
        
        for j in range(len(i)):
            if j % 2 == 0: # impar
                content_out += tr_in

            content_out += td_in + i[j] + td_out

            if j % 2 != 0: # par
                content_out += tr_out
                
        content_out += tabel_out
        
    else:
        print("error - fac tabel")

#copy
copy.copy(content_out)
print("\nGATA!")







