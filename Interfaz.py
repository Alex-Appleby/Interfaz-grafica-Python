import tkinter as tk

class InterfazGrafica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interfaz Gráfica")
        self.geometry("600x400")  # Tamaño de la ventana
        self.configure(bg="white")  # Color de fondo

        # Obtener el tamaño de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calcular el tamaño de la ventana centrada
        window_width = int(screen_width * 0.75)
        window_height = int(screen_height * 0.75)

        # Calcular la posición de la ventana centrada
        x = int((screen_width - window_width) / 2)
        y = int((screen_height - window_height) / 2)

        # Establecer el tamaño y la posición de la ventana
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Crear los botones
        button1 = tk.Button(self, text="Configuración general de los routers y las VPC's", command=self.routerConfig)
        button2 = tk.Button(self, text="Protocolos de enrutamiento de los routers", command=self.protocols)
        button3 = tk.Button(self, text="Conectividad Telner y SSH en los routers", command=self.telnetAndSSHConec)
        button4 = tk.Button(self, text="ACL de los routers", command=self.acl)
        button5 = tk.Button(self, text="DHCP en los routers", command=self.dhcp)
        button6 = tk.Button(self, text="NAT en los routers", command=self.nat)
        button8 = tk.Button(self, text="Protocolo DNS", command=self.dns)
        button9 = tk.Button(self, text="Protocolo VPN", command=self.vpn)
        button10 = tk.Button(self, text="Protocolo SNMP", command=self.snmp)
        button11 = tk.Button(self, text="Protocolo RMON", command=self.rmon)
        button12 = tk.Button(self, text="Protocolo STP y Etherchannel", command=self.stpAndEtherchannel)
        button13 = tk.Button(self, text="Protocolo VLAN", command=self.vlan)
        button7 = tk.Button(self, text="Salir", command=self.quit)  # Botón para salir

        # Configurar el tamaño de los botones
        button1.config(width=50)
        button2.config(width=50)
        button3.config(width=50)
        button4.config(width=50)
        button5.config(width=50)
        button6.config(width=50)
        button8.config(width=50)
        button9.config(width=50)
        button10.config(width=50)
        button11.config(width=50)
        button12.config(width=50)
        button13.config(width=50)
        button7.config(width=50)

        # Posicionar los botones en la interfaz
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()
        button8.pack()
        button9.pack()
        button10.pack()
        button11.pack()
        button12.pack()
        button13.pack()
        button7.pack()  # Agregar el botón de salir

        # Crear un label para mostrar el texto
        self.label = tk.Label(self, text="", bg="white")
        self.label.pack()

    def routerConfig(self):
        self.label.config(text="Texto correspondiente a la configuración del Router")

    def protocols(self):
        self.label.config(text="Texto correspondiente a los protocolos")

    def telnetAndSSHConec(self):
        self.label.config(text="Texto correspondiente a la conexión Telnet y SSH")

    def acl(self):
        self.label.config(text="Texto correspondiente a las ACL")

    def dhcp(self):
        self.label.config(text="Texto correspondiente al servidor DHCP")

    def nat(self):
        self.label.config(text="Texto correspondiente al NAT")

    def dns(self):
        self.label.config(text="Texto correspondiente al protocolo DNS")

    def vpn(self):
        self.label.config(text="Texto correspondiente al protocolo VPN")

    def snmp(self):
        self.label.config(text="Texto correspondiente al protocolo SNMP")

    def rmon(self):
        self.label.config(text="Texto correspondiente al protocolo RMON")

    def stpAndEtherchannel(self):
        self.label.config(text="Texto correspondiente al protocolo STP y Etherchannel")

    def vlan(self):
        self.label.config(text="Texto correspondiente al protocolo VLAN")

if __name__ == "__main__":
    interfaz = InterfazGrafica()
    interfaz.mainloop()


