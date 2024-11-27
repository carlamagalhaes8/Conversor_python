from PyQt5 import uic, QtWidgets

def opcao_selecionada():
    elemento = janela.resp_moeda.currentText()
    
    valor = float(janela.resposta.text()) 

    if elemento == "Libra":
        taxa = 7.30 
    elif elemento == "Euro":
        taxa = 6.09  
    else:  
        taxa = 5.81   

    result = valor * taxa

    janela.resultado.setText(f"R${result:.2f}")  

#
app = QtWidgets.QApplication([])
janela = uic.loadUi("interface_carla.ui")

janela.resp_moeda.addItems(['Libra', 'Euro', 'Dólar'])
janela.butao_conv.clicked.connect(opcao_selecionada)


janela.show()
app.exec()
