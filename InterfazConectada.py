import tkinter as tk
import pexpect 

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
        devices = {'R1': {'prompt': 'R1', 'ip': '192.168.9.1'}, 'R2': {'prompt': 'R2', 'ip': '192.168.2.1'},'R3': {'prompt': 'R3', 'ip': '192.168.4.1'},'R4': {'prompt': 'R4', 'ip': '192.168.6.1'},'R5': {'prompt': 'R5', 'ip': '192.168.8.1'},}
        username = 'cisco'
        password = 'cisco'

        for device in devices.keys(): 
            device_prompt = devices[device]['prompt']
            child = pexpect.spawn('telnet ' + devices[device]['ip'])
        
            child.expect('Username:')
            child.sendline(username)
            child.expect('Password:')
            child.sendline(password)
            child.expect(device_prompt)
            
            #child.sendline('show version | i V')
            child.expect('#')
            child.sendline('terminal length 0')
            child.expect('#')
            child.sendline('show running-config')
            child.expect(device_prompt)
            child.expect('#')

            configuration = child.before.decode('utf-8')
            self.label.config(text = '--------------------------------------------------------------------------')    
            self.label.config(text = f">>>>>>>Configuration of {device}<<<<<<<<<")
            self.label.config(text = configuration)
            self.label.config(text = '------------------------------------------------------------------------\n\n')
            child.sendline('exit')

    def protocols(self):
        devices = {'R1': {'prompt': 'R1', 'ip': '192.168.9.1'}, 'R2': {'prompt': 'R2', 'ip': '192.168.2.1'},'R3': {'prompt': 'R3', 'ip': '192.168.4.1'},'R4': {'prompt': 'R4', 'ip': '192.168.7.1'},'R5': {'prompt': 'R5', 'ip': '192.168.8.1'},}
        username = 'cisco'
        password = 'cisco'
        for device in devices.keys(): 
            device_prompt = devices[device]['prompt']
            child = pexpect.spawn('telnet ' + devices[device]['ip'])
        
            child.expect('Username:')
            child.sendline(username)
            child.expect('Password:')
            child.sendline(password)
            child.expect(device_prompt)
            
            if(device=='R4'):
                #child.sendline('terminal length 0')
                child.sendline('show ip route')
                child.expect('#')
                child.sendline(' ')            
                child.expect(device_prompt)
                
                
            else:
                child.sendline('show ip route')
                child.expect(device_prompt)

            configuration = child.before.decode('utf-8')
            self.label.config(text = '--------------------------------------------------------------------------')    
            self.label.config(text = f">>>>>>>>>>Protocols of the device {device}<<<<<<<<<<")
            self.label.config(text = configuration)
            self.label.config(text = '------------------------------------------------------------------------\n\n')
            child.sendline('exit')

    def telnetAndSSHConec(self):
        devices = {'R1': {'prompt': 'R1', 'ip': '192.168.9.1'}, 'R2': {'prompt': 'R2', 'ip': '192.168.2.1'},'R3': {'prompt': 'R3', 'ip': '192.168.4.1'},'R4': {'prompt': 'R4', 'ip': '192.168.6.1'},'R5': {'prompt': 'R5', 'ip': '192.168.8.1'},}
        username = 'cisco'
        password = 'cisco'
        for device in devices.keys(): 
            device_prompt = devices[device]['prompt']
            child = pexpect.spawn('telnet ' + devices[device]['ip'])
        
            child.expect('Username:')
            child.sendline(username)
            child.expect('Password:')
            child.sendline(password)
            child.expect(device_prompt)
            
            #child.sendline('show version | i V')
            child.sendline('show running-config | include telnet')
            child.expect(device_prompt)
            

            configuration = child.before.decode('utf-8')
            self.label.config(text = '--------------------------------------------------------------------------')    
            self.label.config(text = f">>>>>>>>>>SSH and Telnet connectivity of the device {device}<<<<<<<<<<")
            self.label.config(text = configuration)
            self.label.config(text = '------------------------------------------------------------------------\n\n')
            child.sendline('exit')

    def acl(self):
        devices = {'R1': {'prompt': 'R1', 'ip': '192.168.9.1'}, 
            'R2': {'prompt': 'R2', 'ip': '192.168.2.1'},
            'R3': {'prompt': 'R3', 'ip': '192.168.4.1'},
            'R4': {'prompt': 'R4', 'ip': '192.168.6.1'},
            'R5': {'prompt': 'R5', 'ip': '192.168.8.1'},
            }
        username = 'cisco'
        password = 'cisco'
        for device in devices.keys(): 
            device_prompt = devices[device]['prompt']
            child = pexpect.spawn('telnet ' + devices[device]['ip'])
        
            child.expect('Username:')
            child.sendline(username)
            child.expect('Password:')
            child.sendline(password)
            child.expect(device_prompt)
            
            #child.sendline('show version | i V')
            child.sendline('show access-lists')
            child.expect(device_prompt)
            

            configuration = child.before.decode('utf-8')
            self.label.config(text = '--------------------------------------------------------------------------')    
            self.label.config(text = f"ACLs of the device {device}:")
            self.label.config(text = configuration)
            self.label.config(text = '------------------------------------------------------------------------\n\n')
            child.sendline('exit')

    def dhcp(self):
        devices = {'R1': {'prompt': 'R1', 'ip': '192.168.9.1'}, 'R2': {'prompt': 'R2', 'ip': '192.168.2.1'},'R3': {'prompt': 'R3', 'ip': '192.168.4.1'},'R4': {'prompt': 'R4', 'ip': '192.168.6.1'},'R5': {'prompt': 'R5', 'ip': '192.168.8.1'},}
        username = 'cisco'
        password = 'cisco'
        for device in devices.keys(): 
            device_prompt = devices[device]['prompt']
            child = pexpect.spawn('telnet ' + devices[device]['ip'])
        
            child.expect('Username:')
            child.sendline(username)
            child.expect('Password:')
            child.sendline(password)
            child.expect(device_prompt)
            
            #child.sendline('show version | i V')
            child.sendline('show running-config | include dhcp')
            child.expect(device_prompt)

            configuration = child.before.decode('utf-8')
            self.label.config(text = '--------------------------------------------------------------------------')    
            self.label.config(text = f">>>>>>>>>>DHCP in the device {device}<<<<<<<<<<")
            self.label.config(text = configuration)
            self.label.config(text = '------------------------------------------------------------------------\n\n')
            child.sendline('exit')

    def nat(self):
        devices = {'R1': {'prompt': 'R1', 'ip': '192.168.9.1'}, 'R2': {'prompt': 'R2', 'ip': '192.168.2.1'},'R3': {'prompt': 'R3', 'ip': '192.168.4.1'},'R4': {'prompt': 'R4', 'ip': '192.168.6.1'},'R5': {'prompt': 'R5', 'ip': '192.168.8.1'},}
        username = 'cisco'
        password = 'cisco'
        for device in devices.keys(): 
            device_prompt = devices[device]['prompt']
            child = pexpect.spawn('telnet ' + devices[device]['ip'])
        
            child.expect('Username:')
            child.sendline(username)
            child.expect('Password:')
            child.sendline(password)
            child.expect(device_prompt)
            
            
            child.sendline('show running-config | include nat')
            #child.sendline('show ip nat translations')
            child.expect(device_prompt)
            

            configuration = child.before.decode('utf-8')
            self.label.config(text = '--------------------------------------------------------------------------')    
            self.label.config(text = f">>>>>>>>>>NAT in the device {device}<<<<<<<<<<")
            self.label.config(text = configuration)
            self.label.config(text = '------------------------------------------------------------------------\n\n')
            child.sendline('exit')

    def dns(self):
        self.label.config(text="Texto correspondiente al protocolo DNS") #Modificar aquí Johan por el código del método correspondiente al protocolo que implementaste. Puedes basarte en los métodos anteriores.

    def vpn(self):
        self.label.config(text="Texto correspondiente al protocolo VPN") #Modificar aquí Johan por el código del método correspondiente al protocolo que implementaste. Puedes basarte en los métodos anteriores.

    def snmp(self):
        self.label.config(text="Texto correspondiente al protocolo SNMP") #Modificar aquí Johan por el código del método correspondiente al protocolo que implementaste. Puedes basarte en los métodos anteriores.

    def rmon(self):
        self.label.config(text="Texto correspondiente al protocolo RMON") #Modificar aquí Johan por el código del método correspondiente al protocolo que implementaste. Puedes basarte en los métodos anteriores.

    def stpAndEtherchannel(self):
        self.label.config(text="Texto correspondiente al protocolo STP y Etherchannel") #Modificar aquí Johan por el código del método correspondiente al protocolo que implementaste. Puedes basarte en los métodos anteriores.

    def vlan(self):
        self.label.config(text="Texto correspondiente al protocolo VLAN") #Modificar aquí Johan por el código del método correspondiente al protocolo que implementaste. Puedes basarte en los métodos anteriores.

if __name__ == "__main__":
    interfaz = InterfazGrafica()
    interfaz.mainloop()


