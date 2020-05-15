import wpf
from System.Windows import Application, Window, MessageBox

class MyWindow(Window):
    
    def __init__(self, hitung, barang):
        self.barang = []
        self.hitung = []
        wpf.LoadComponent(self, 'TUGAS_AKHIR.xaml')

    #JACKET
    def onclick(self, sender, e):
        def error() : 
            MessageBox.Show("There is an empty box")
            return 0
        y= self.jumlah1.Text.ToString()
        o = 0
        stack = []
        n = 0
        if y== "" or y== "ENTER NUMBERS"  or self.combo1.Text == "" or (self.rb1.IsChecked == False and self.rb2.IsChecked == False and self.rb3.IsChecked == False and self.rb4.IsChecked == False) : 
            error()
        
        else:
        #menentukan jenis dan harga
            if self.combo1.Text == self.combo1.Items.GetItemAt(0).ToString():
                jenis = "Jeans Jacket"
                harga = "450000"

                j = int(self.jumlah1.Text)
                jml = str(j*450000)
                
            elif self.combo1.Text == self.combo1.Items.GetItemAt(1).ToString():
                jenis = "Hoodie Jacket"
                harga = "350000"

                j = int(self.jumlah1.Text)
                jml = str(j*350000)

            elif self.combo1.Text == self.combo1.Items.GetItemAt(2).ToString():
                jenis = "Bomber Jacket"
                harga = "250000"

                j = int(self.jumlah1.Text)
                jml = str(j*250000)

            elif self.combo1.Text == self.combo1.Items.GetItemAt(3).ToString():
                jenis = "Coach Jacket"
                harga = "410000"

                j = int(self.jumlah1.Text)
                jml = str(j*410000)

            #menentukan ukuran
            if self.rb1.IsChecked:
                 ukuran="M"
            elif self.rb2.IsChecked:
                ukuran="L"
            elif self.rb3.IsChecked:
                ukuran="XL"
            elif self.rb4.IsChecked:
                ukuran="XXL"
            
            self.hitung.append(int(jml))
            self.barang.append(int(j))
            stack.append(jenis+" ("+ukuran+") x"+y+" -- Rp."+jml)            
            self.list1.Items.Add(stack[n])
            n = n + 1

        pass
    #mengganti isi textbox    
    def clear(self, sender, e):
        self.jumlah1.Text = "ENTER NUMBERS"
        self.combo1.Text = " "
        self.rb1.IsChecked = False
        self.rb2.IsChecked = False
        self.rb3.IsChecked = False
        self.rb4.IsChecked = False
        pass

#CART    
    

    
    def hit(self, sender, e):
        x= self.TextNama.Text.ToString()
        bra = sum(self.barang)
        brb = str(bra)

        hita = sum(self.hitung)
        hitb = str(hita)
        def error() : 
            MessageBox.Show("Enter your name")
            return 0
        if x== "" :
            error()
        else:
            anonim_func = lambda pembeli: str(pembeli)
            ty= anonim_func("~~TERIMAKASIH SUDAH MEMBELI DI TOKO KAMI~~")
            MessageBox.Show("Hallo "+x+" anda telah membeli "+brb+" item pada toko kami"+"\n"
                            +"dengan total biaya Rp."+hitb)
            MessageBox.Show(ty)
        
        
        
        
        pass
     
        
#AKSESORIS       
    def clear4(self, sender, e):
        self.jumlah4.Text = "ENTER NUMBERS"
        self.combo4.Text = " "
        pass
    
    def onclick4(self, sender, e):
        def error() : 
            MessageBox.Show("There is an empty box")
            return 0
        y= self.jumlah4.Text.ToString()
        stack = []
        n = 0
        if y== "" or self.combo4.Text == "" :
            error()
        
        else:
        #menentukan jenis dan harga
            if self.combo4.Text == self.combo4.Items.GetItemAt(0).ToString():
                jenis = "STICKER PACK"
                harga = "50000"

                j = int(self.jumlah4.Text)
                jml = str(j*50000)
                
            elif self.combo4.Text == self.combo4.Items.GetItemAt(1).ToString():
                jenis = "ENAMEL PIN"
                harga = "40000"

                j = int(self.jumlah4.Text)
                jml = str(j*40000)

            elif self.combo4.Text == self.combo4.Items.GetItemAt(2).ToString():
                jenis = "KEY CHAINS"
                harga = "30000"

                j = int(self.jumlah4.Text)
                jml = str(j*30000) 

            self.hitung.append(int(jml))
            self.barang.append(int(j))
            stack.append(jenis+" x"+y+" -- Rp."+jml) 
            self.list1.Items.Add(stack[n])
            n = n + 1
    
        pass

#HEADWEAR     
    def clear3(self, sender, e):
        self.jumlah3.Text = "ENTER NUMBERS"
        self.combo3.Text = " "
        pass
    
    def onclick3(self, sender, e):
        def error() : 
            MessageBox.Show("There is an empty box")
            return 0
        y= self.jumlah3.Text.ToString()
        stack = []
        n = 0
        if y== "" or self.combo3.Text == "" :
            error()
        
        else:
        #menentukan jenis dan harga
            if self.combo3.Text == self.combo3.Items.GetItemAt(0).ToString():
                jenis = "POLO CAP-BLACK"
                harga = "120000"

                j = int(self.jumlah3.Text)
                jml = str(j*120000)
                
            elif self.combo3.Text == self.combo3.Items.GetItemAt(1).ToString():
                jenis = "TRUCKER CAP-BLACK"
                harga = "115000"

                j = int(self.jumlah3.Text)
                jml = str(j*115000)

            elif self.combo3.Text == self.combo3.Items.GetItemAt(2).ToString():
                jenis = "BEANIE HAT-BLACK"
                harga = "100000"

                j = int(self.jumlah3.Text)
                jml = str(j*100000) 
            self.hitung.append(int(jml))
            self.barang.append(int(j))
            stack.append(jenis+" x"+y+" -- Rp."+jml)
            self.list1.Items.Add(stack[n])
            n = n + 1

        pass

#T-SHIRTS    
    def clear2(self, sender, e):
        self.jumlah2.Text = "ENTER NUMBERS"
        self.combo2.Text = " "
        self.rb11.IsChecked = False
        self.rb22.IsChecked = False
        self.rb33.IsChecked = False
        self.rb44.IsChecked = False
        pass
    
    def onclick2(self, sender, e):
        def error() : 
            MessageBox.Show("There is an empty box")
            return 0
        y= self.jumlah2.Text.ToString()
        stack = []
        n = 0
        if y== "" or self.combo2.Text == "" or (self.rb11.IsChecked == False and self.rb22.IsChecked == False and self.rb33.IsChecked == False and self.rb44.IsChecked == False) :
            error()
        
        else:
        #menentukan jenis dan harga
            if self.combo2.Text == self.combo2.Items.GetItemAt(0).ToString():
                jenis = "BASIC-BLACK-SS"
                harga = "110000"

                j = int(self.jumlah2.Text)
                jml = str(j*110000)
                
            elif self.combo2.Text == self.combo2.Items.GetItemAt(1).ToString():
                jenis = "BASIC-BLACK-LS"
                harga = "150000"

                j = int(self.jumlah2.Text)
                jml = str(j*150000)

            elif self.combo2.Text == self.combo2.Items.GetItemAt(2).ToString():
                jenis = "BASIC-WHITE-SS"
                harga = "110000"

                j = int(self.jumlah2.Text)
                jml = str(j*110000)

            elif self.combo2.Text == self.combo2.Items.GetItemAt(3).ToString():
                jenis = "LOGO BOX-BLACK-SS"
                harga = "120000"

                j = int(self.jumlah2.Text)
                jml = str(j*120000)

            elif self.combo2.Text == self.combo2.Items.GetItemAt(4).ToString():
                jenis = "LOGO BOX-WHITE-SS"
                harga = "120000"

                j = int(self.jumlah2.Text)
                jml = str(j*120000)

            #menentukan ukuran
            if self.rb11.IsChecked:
                 ukuran="S"
            elif self.rb22.IsChecked:
                ukuran="M"
            elif self.rb33.IsChecked:
                ukuran="L"
            elif self.rb44.IsChecked:
                ukuran="XL"

            self.hitung.append(int(jml))
            self.barang.append(int(j))
            stack.append(jenis+" ("+ukuran+") x"+y+" -- Rp."+jml) 
            self.list1.Items.Add(stack[n])
            n = n + 1 

        pass 
if __name__ == '__main__':
    Application().Run(MyWindow([],[]))