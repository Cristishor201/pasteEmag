#program de formatare titlu tabel pt nei.ro | emag -> pune pe nei
import pyperclip as copy
listap = [] # principala
listas = []


#inp = input("Copy the description on emag...")

#content_raw = copy.paste()


#bold <p><span style="font-weight: 700; color: rgb(34, 34, 34); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; text-transform: uppercase;"><br></span><span style="font-weight: 700; color: rgb(34, 34, 34); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; text-transform: uppercase;">DETALII FRIGIDER</span></p>
#tabel <table class="table table-bordered"><tbody><tr><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(136, 136, 136); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">Volum net frigider</span><br></span></td><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(34, 34, 34); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">175 l</span><br></span></td></tr><tr><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(136, 136, 136); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">Sistem dezghetare frigider</span><br></span></td><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(34, 34, 34); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">Manual</span><br></span></td></tr><tr><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(136, 136, 136); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">Numar rafturi frigider</span><br></span></td><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(34, 34, 34); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">3</span><br></span></td></tr><tr><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(136, 136, 136); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">Numar rafturi usi</span><br></span></td><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(34, 34, 34); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">4</span><br></span></td></tr><tr><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(136, 136, 136); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">Material rafturi</span><br></span></td><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(34, 34, 34); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">Sticla termorezistenta</span><br></span></td></tr><tr><td><span style="background-color: rgb(255, 255, 255);"><span style="color: rgb(136, 136, 136); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line;">Dozator apa</span><br></span></td><td><span style="color: rgb(34, 34, 34); font-family: &quot;Open Sans&quot;, Helvetica, Arial, sans-serif; font-size: 14px; white-space: pre-line; background-color: rgb(255, 255, 255);">Nu</span><br></td></tr></tbody></table>

content = r'CARACTERISTICI GENERALE\r\n\r\nUtilizat pentru\tBucatarie\r\nCARACTERISTICI GENERALE\r\n\r\nTip incastrare\tIncorporabil\r\nNumar usi\t2\r\nVolum net total\t192 l\r\nSistem racire\tStatic\r\nAgent racire\tEcologic R600a\r\nCuloare\tAlb\r\nDETALII FRIGIDER\r\n\r\nVolum net frigider\t175 l\r\nSistem dezghetare frigider\tManual\r\nNumar rafturi frigider\t3\r\nNumar rafturi usi\t4\r\nMaterial rafturi\tSticla termorezistenta\r\nDozator apa\tNu\r\nDETALII CONGELATOR\r\n\r\nVolum net congelator\t17 l\r\nSistem dezghetare congelator\tManual\r\nNumar compartimente\t1\r\nCARACTERISTICI CHEIE\r\n\r\nFunctii\tControl mecanic al temperaturii\r\nENERGIE & PERFORMANTA\r\n\r\nTensiune alimentare\t230 V\r\nNivel zgomot\t42 dB\r\nEficienta energetica\tA+\r\nConsum anual energie\t206 kWh\r\nDIMENSIUNI\r\n\r\nInaltime\t122.5 cm\r\nLatime\t54 cm\r\nAdancime\t54.5 cm\r\nGreutate\t40 Kg'

lim1 = 0
for i in range(len(content)): # while end
    if content[i:i+8] == r"\r\n\r\n": # titlu bold
        lim2 = i
        listap.append(content[lim1:lim2])
        print(listap)

        # urmeaza imediat tabel
        lim1 = i+8
        
    if content[i:i+2] == r"\t": # casuta impara
        lim2 = i
        listas.append(content[lim1:lim2]) # impara in lista sec
        
