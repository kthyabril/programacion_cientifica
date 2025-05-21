cantidad = int(input("Introduce la cantidad de unidades: "))
gruesas = cantidad // 144  
docenas = (cantidad % 144) // 12 
unidades = cantidad % 12  
print(f"{cantidad} unidades son {gruesas} gruesas, {docenas} docenas y {unidades} unidades.")