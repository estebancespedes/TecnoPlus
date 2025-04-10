from gestorPrincipal import gestorPrincipal
gp= gestorPrincipal()

gp.agregarAInventario("2156","A33 5G","Celular",250,280,20,10,2)
gp.registrarEntradaMercancia("2156",5)

gp.generarVenta()